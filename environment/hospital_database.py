class HospitalDatabase:

    def __init__(self):
        self.records = []

    def update_record(self, record):
        self.records.append(record)
        print("Database Updated:", record)

    def display_records(self):

        print("\nHospital Emergency Records")

        for r in self.records:
            print(r)