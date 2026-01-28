import math, time

N = 10000000
x = 1

start = time.perf_counter()

for _ in range(N):
    math.sqrt(x)

end = time.perf_counter()

seconds = end - start
print("Square roots per second:", int(N / seconds))