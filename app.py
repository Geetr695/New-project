import math, time

N = 10000000        # do 10 million square roots
x = 123.456           # always the same number

start = time.perf_counter()

for _ in range(N):
    math.sqrt(x)

end = time.perf_counter()

seconds = end - start
print("Square roots per second:", int(N / seconds))