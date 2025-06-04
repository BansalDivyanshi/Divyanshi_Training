import random
from datetime import datetime
import csv

def generate_sensor_data(sensor_id, num_readings=10):
    readings = []
    for _ in range(num_readings):
        reading = {
            "sensor": "sensor" + str(sensor_id),
            "timestamp": datetime.now().isoformat(),
            "temperature": (random.uniform(20.0, 40.0))
        }
        readings.append(reading)
    return readings

def print_readings(sensor_data):
    for reading in sensor_data:
        print(reading['timestamp'] + " | " + reading['sensor'] + " | " + str(reading['temperature']) + "C")

def print_summary(sensor_data):
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
        print("\n" + sensor_name + ":")
        print("  Avg Temperature: " + str((avg_temp)) + "C")
        print("  Max Temperature: " + str((max_temp)) + "C")
        print("  Min Temperature: " + str((min_temp)) + "C")

def write_to_csv(sensor_data, filename="sensor_data.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["sensor_id", "timestamp", "temperature"])
            for entry in sensor_data:
                writer.writerow([entry["sensor_id"], entry["timestamp"], entry["temperature"]])
    except (FileNotFoundError) as e:
        print("Error writing to file:", e)

import csv

def process_sensor_data(filename):
    valid = []
    faulty = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            temperature = float(row["temperature"])
            if temperature < 0 or temperature > 50:
                faulty.append(row)
            else:
                valid.append(row)
    with open("valid_readings.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["sensor_id", "timestamp", "temperature"])
        writer.writeheader()
        writer.writerows(valid)

    with open("faulty_readings.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["sensor_id", "timestamp", "temperature"])
        writer.writeheader()
        writer.writerows(faulty)

class SensorDevice:
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location
        self.readings = []

    def generate_readings(self, n=10):
        for i in range(n):
            reading = {
                "sensor_id": self.sensor_id,
                "timestamp": datetime.now().isoformat(),
                "temperature": random.uniform(10.0, 60.0)
            }
            self.readings.append(reading)

    def save_to_file(self, filename):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["sensor_id", "timestamp", "temperature"])
                writer.writeheader()
                writer.writerows(self.readings)
        except Exception as e:
            print("Error writing to file:", e)

class SmartSensor(SensorDevice):
    def detect_anomaly(self):
        anomalies = []
        for reading in self.readings:
            temperature = reading["temperature"]
            if temperature < 0.0 or temperature > 50.0:
                anomalies.append(reading)
        return anomalies
    

