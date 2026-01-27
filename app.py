import math, time

start_time = time.monotonic()
duration = 1
number = 0

end_time = start_time + duration

while time.monotonic() < end_time:
    sqrt_value = math.sqrt(number)
    number = number + 1

print("Ammount of square roots calculated in one second:", number)