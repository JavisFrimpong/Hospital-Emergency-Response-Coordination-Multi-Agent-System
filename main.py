import time
import random

from agents.emergency_agent import EmergencyAgent
from agents.coordinator_agent import CoordinatorAgent
from agents.doctor_agent import DoctorAgent

from environment.emergency_monitor import EmergencyMonitor
from environment.hospital_database import HospitalDatabase
from environment.notification_system import NotificationSystem


monitor = EmergencyMonitor()
database = HospitalDatabase()
notifier = NotificationSystem()

doctor1 = DoctorAgent("Dr. Mensah")
doctor2 = DoctorAgent("Dr. Owusu")
doctor3 = DoctorAgent("Dr. Asante")

doctors = [doctor1, doctor2, doctor3]

emergency_agent = EmergencyAgent(monitor)

coordinator = CoordinatorAgent(doctors, database, notifier)


print("\n" + "="*50)
print("*** STARTING HOSPITAL MULTI-AGENT SIMULATION ***")
print("="*50 + "\n")

# Simulation Loop
for i in range(5):
    print(f"\n--- Simulation Cycle {i+1} ---")

    # 1. Perception
    patient, severity, detection_time = emergency_agent.perceive()
    time.sleep(1) # Add slight delay for realistic output

    # 2. Coordination & Action
    coordinator.decide_and_act(patient, severity, detection_time)
    
    # 3. Simulate passage of time and doctor releases
    time.sleep(1)
    for doc in doctors:
        if not doc.available:
            # 50% chance a busy doctor finishes their case each cycle
            if random.random() > 0.5:
                doc.release()

# Display Final Report
database.generate_report()
print("Simulation Complete.")
