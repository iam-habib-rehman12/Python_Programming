import numpy as np
import time

arr=np.arange(1_000_000)

#vectorized
start = time.time()
squared= arr**2
end=time.time()
vect_time = end - start
print("Vectorized : ", vect_time)

#Loop
start=time.time()
squared_loop = [x**2 for x in arr]
end = time.time()
loop_time = end - start
print("loop : ", loop_time)

print("Time ratio : ", (loop_time/vect_time))

a = np.array([1,2,3,4])
view_a = a[1:3]
view_a[0] = 99
print(a)

arr=np.arange(10,110,10)
print(np.shape(arr))
print(arr[2:7])
arr[arr>50]=-1
print(arr)

scores= np.array([55,72,67,48,90,83,60])
print(scores[scores>70])
scores[scores<60]=0
print(scores)

M=np.array([[5,10,15],
            [20,25,30],
            [35,40,45]])

print(np.sum(M, axis=0))
print(np.mean(M, axis=1))
print(np.std(M))

a= np.arange(12).reshape(3,4)
print(a)

for x in np.nditer(a):
    print(x, end=" ")

print()

with np.nditer(a, op_flags=['readwrite']) as it:
    for x in it:
        x[...] = x**2
print(a)

