import random

class DoctorAgent:

    def __init__(self, name):
        self.name = name
        self.available = True

    def evaluate_case(self, patient, severity):

        print(f"{self.name} evaluating case for {patient}")

        decision = random.choice(["accept", "reject"])

        if decision == "accept":
            print(f"{self.name} accepted the emergency case")
            self.available = False
            return True

        print(f"{self.name} rejected the emergency case")
        return False