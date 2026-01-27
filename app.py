import math, time

start_time = time.monotonic()
duration = 1
number = 0

with open("output_simple.txt", "w") as file:
    while(time.monotonic() - start_time) < duration:
        sqrt_value = math.sqrt(number)
        number = number + 1
        file.write(str(sqrt_value) + "\n")

print("Ammount of square roots calculated in one second:", number)