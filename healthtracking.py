import datetime

class HealthTracker:
    def __init__(self):
        self.weight = []
        self.steps = []
        self.sleep = {}

    def track_weight(self, weight):
        self.weight.append((datetime.datetime.now(), weight))

    def track_steps(self, steps):
        self.steps.append((datetime.datetime.now(), steps))

    def track_sleep(self, date, hours):
        self.sleep[date] = hours

    def get_weight(self):
        return self.weight

    def get_steps(self):
        return self.steps

    def get_sleep(self):
        return self.sleep


# Example usage
tracker = HealthTracker()

# Track weight
tracker.track_weight(70)
tracker.track_weight(69.5)

# Track steps
tracker.track_steps(5000)
tracker.track_steps(7000)

# Track sleep
tracker.track_sleep("2023-06-01", 7)
tracker.track_sleep("2023-06-02", 8)

# Get weight data
weight_data = tracker.get_weight()
for data in weight_data:
    print(f"Date: {data[0]}, Weight: {data[1]}")

# Get step data
step_data = tracker.get_steps()
for data in step_data:
    print(f"Date: {data[0]}, Steps: {data[1]}")

# Get sleep data
sleep_data = tracker.get_sleep()
for date, hours in sleep_data.items():
    print(f"Date: {date}, Sleep Hours: {hours}")

