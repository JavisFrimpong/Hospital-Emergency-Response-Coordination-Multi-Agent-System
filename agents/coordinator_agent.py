class CoordinatorAgent:

    def __init__(self, doctors, database, notifier):

        self.doctors = doctors
        self.database = database
        self.notifier = notifier

    def decide_and_act(self, patient, severity):

        print("\nCoordinatorAgent analyzing emergency...")

        for doctor in self.doctors:

            if doctor.available:

                accepted = doctor.evaluate_case(patient, severity)

                if accepted:

                    self.notifier.notify(doctor.name, patient)

                    self.database.update_record(
                        f"{doctor.name} assigned to {patient} ({severity})"
                    )

                    return

        print("No doctor available! Escalating emergency.")