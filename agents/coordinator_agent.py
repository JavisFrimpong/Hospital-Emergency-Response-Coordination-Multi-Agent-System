import datetime

class CoordinatorAgent:

    def __init__(self, doctors, database, notifier):
        self.doctors = doctors
        self.database = database
        self.notifier = notifier

    def decide_and_act(self, patient, severity, detection_time):
        print("\nCoordinatorAgent analyzing emergency and coordinating with doctors...")

        # 1. Ask all available doctors if they can take the case
        willing_doctors = []
        for doctor in self.doctors:
            if doctor.available:
                print(f"  - Asking {doctor.name}...")
                if doctor.evaluate_case(patient, severity, detection_time):
                    print(f"    * {doctor.name} is willing to accept the case.")
                    willing_doctors.append(doctor)
                else:
                    print(f"    X {doctor.name} rejected the case (busy/unavailable).")

        # 2. Pick the best doctor (e.g., sorting by lowest workload)
        if willing_doctors:
            willing_doctors.sort(key=lambda d: d.workload)
            best_doctor = willing_doctors[0]
            
            # 3. Assign the case
            best_doctor.assign_case(patient, severity)
            self.notifier.notify(best_doctor.name, patient)
            
            assignment_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 4. Save to database
            record = {
                "patient": patient,
                "severity": severity,
                "detection_time": detection_time,
                "doctor_assigned": best_doctor.name,
                "assignment_time": assignment_time,
                "status": "Assigned"
            }
            self.database.update_record(record)
            
        else:
            print("WARNING: No doctor available! Escaping to external emergency services.")
            record = {
                "patient": patient,
                "severity": severity,
                "detection_time": detection_time,
                "doctor_assigned": "None (Escalated)",
                "assignment_time": "N/A",
                "status": "Escalated"
            }
            self.database.update_record(record)