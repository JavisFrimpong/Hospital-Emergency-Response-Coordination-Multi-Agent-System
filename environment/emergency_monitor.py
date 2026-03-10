import random

class EmergencyMonitor:

    def detect_emergency(self):

        patients = ["Patient_A", "Patient_B", "Patient_C"]

        severity_levels = ["Low", "Medium", "High"]

        patient = random.choice(patients)
        severity = random.choice(severity_levels)

        print("\nEmergency Alert Detected")
        print("Patient:", patient)
        print("Severity:", severity)

        return patient, severity