class HospitalDatabase:

    def __init__(self):
        self.records = []

    def update_record(self, record_dict):
        self.records.append(record_dict)
        print(f"Database Updated: New record added for {record_dict.get('patient')}.")

    def generate_report(self):
        print("\n" + "="*50)
        print("*** HOSPITAL EMERGENCY RESPONSE FINAL REPORT ***")
        print("="*50)
        
        if not self.records:
            print("No emergencies handled during this simulation.")
            return

        for idx, r in enumerate(self.records, 1):
            print(f"\nCase #{idx}")
            print(f"  Patient:        {r.get('patient')}")
            print(f"  Severity:       {r.get('severity')}")
            print(f"  Detected At:    {r.get('detection_time')}")
            print(f"  Assigned To:    {r.get('doctor_assigned')}")
            print(f"  Action Time:    {r.get('assignment_time')}")
            print(f"  Status:         {r.get('status')}")

        print("="*50 + "\n")
