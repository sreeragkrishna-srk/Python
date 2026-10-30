# Variables and Data Types
driver_name = "Jordan"
vehicle_speed = 65
fuel_level = 82.5
is_engine_on = True

print(f"Driver: {driver_name}, Speed: {vehicle_speed} mph, Fuel: {fuel_level}%, Active: {is_engine_on}")

# Math Operators
distance = 180
time_hours = 3

average_speed = distance / time_hours
remaining_fuel = fuel_level - (distance * 0.1)
fuel_chunks = distance // 50

print(f"Avg Speed: {average_speed}, Remaining Fuel: {remaining_fuel}, Fuel Checkpoints: {fuel_chunks}")

# Control Flow
speed_limit = 60

if vehicle_speed > speed_limit + 15:
    status = "Reckless Driving"
elif vehicle_speed > speed_limit:
    status = "Speeding Warning"
else:
    status = "Safe Speed"

print(f"Vehicle Status: {status}")

# Loops
print("Pre-trip Check:")
for step in range(1, 4):
    print(f"Checking module {step}... OK")

fuel_count = 3
while fuel_count > 0:
    print(f"Refueling... step {fuel_count}")
    fuel_count -= 1