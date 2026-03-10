import datetime
from simulation.emergency_cases import get_random_patient, get_random_severity

class EmergencyMonitor:

    def detect_emergency(self):
        patient = get_random_patient()
        severity = get_random_severity()
        detection_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n" + "="*40)
        print("!!! EMERGENCY ALERT DETECTED !!!")
        print("="*40)
        print(f"Time:     {detection_time}")
        print(f"Patient:  {patient}")
        print(f"Severity: {severity}\n")

        return patient, severity, detection_time
