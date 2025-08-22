import sys
import os
import threading
import time
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QTextEdit, QListWidget, QMessageBox
)
from PyQt5.QtCore import pyqtSignal, QObject

# Directory for saving chat logs
os.makedirs("chat_logs", exist_ok=True)

# Simulated user database
users = {
    "habib": "habib11",
    "sahil": "123",
    "shoban": "456"
}

class SignalHandler(QObject):
    message_received = pyqtSignal(str)

signal_handler = SignalHandler()

def log_message(sender, recipient, message):
    filename = f"chat_logs/{sender}_to_{recipient}.txt"
    with open(filename, "a") as file:
        file.write(f"{sender} → {recipient}: {message}\n")

class ChatWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle(f"Habib's Chat App - Logged in as {username}")
        self.username = username

        self.layout = QVBoxLayout()
        self.recipient_list = QListWidget()
        self.recipient_list.addItems([u for u in users if u != self.username])

        self.layout.addWidget(QLabel("Select user to message:"))
        self.layout.addWidget(self.recipient_list)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.message_input = QLineEdit()
        self.layout.addWidget(self.message_input)

        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_message)
        self.layout.addWidget(send_button)

        self.setLayout(self.layout)

        signal_handler.message_received.connect(self.display_message)

        threading.Thread(target=self.simulate_messages, daemon=True).start()

    def send_message(self):
        selected = self.recipient_list.currentItem()
        if not selected:
            QMessageBox.warning(self, "Error", "Select a user to send message.")
            return

        recipient = selected.text()
        message = self.message_input.text().strip()
        if not message:
            return

        full_msg = f"You → {recipient}: {message}"
        self.display_message(full_msg)
        log_message(self.username, recipient, message)
        self.message_input.clear()

    def display_message(self, message):
        self.chat_display.append(message)

    def simulate_messages(self):
        while True:
            time.sleep(random.randint(10, 20))
            sender = random.choice([u for u in users if u != self.username])
            fake_msg = f"{sender} → You: Hi {self.username}, this is an automated message."
            log_message(sender, self.username, fake_msg)
            signal_handler.message_received.emit(fake_msg)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habib's Secure Login")
        self.setGeometry(300, 300, 350, 150)

        self.layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.authenticate)
        self.layout.addWidget(login_button)

        self.setLayout(self.layout)

    def authenticate(self):
        username = self.username_input.text().strip().lower()
        password = self.password_input.text().strip()

        if username in users and users[username] == password:
            self.hide()
            self.chat_window = ChatWindow(username)
            self.chat_window.show()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password.")

def main():
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
