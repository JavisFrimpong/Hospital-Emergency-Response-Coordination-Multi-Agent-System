import random

class DoctorAgent:

    def __init__(self, name):
        self.name = name
        self.available = True
        self.workload = 0

    def evaluate_case(self, patient, severity, detection_time):
        # Doctor only states willingness, does not commit until assigned
        decision = random.choice(["accept", "reject"])
        
        if decision == "accept":
            # Just stating they can handle it
            return True

        return False

    def assign_case(self, patient, severity):
        self.available = False
        self.workload += 1
        print(f"Dr. >> {self.name} has been ASSIGNED to {patient} ({severity}). Workload: {self.workload}")

    def release(self):
        if not self.available:
            self.available = True
            print(f"SUCCESS: {self.name} has finished their case and is now available.")