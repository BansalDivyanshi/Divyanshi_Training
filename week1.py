import random
import time
from datetime import datetime

sensor_data = []
for i in range(5):
    for j in range (10):
        reading = {
            "sensor" : "sensor" + str(i + 1),
            "timestamp" : datetime.now().isoformat(),
            "temperature": (random.uniform(20.0, 40.0))
        }
        sensor_data.append(reading)

for entry in sensor_data:
    print(entry['timestamp'] + " | " + entry['sensor'] + " | " + str(entry['temperature']) + "°C")

summary = {}

for entry in sensor_data:
    sensor_name = entry["sensor"]
    temperature = entry["temperature"]

    if sensor_name not in summary:
        summary[sensor_name] = []

    summary[sensor_name].append(temperature)


for sensor_name in summary:
    temperatures = summary[sensor_name]

    avg_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    
    print(sensor_name + ":")
    print("  Avg Temperature: " + str((avg_temp)) + "°C")
    print("  Max Temperature: " + str((max_temp)) + "°C")
    print("  Min Temperature: " + str((min_temp)) + "°C")



 