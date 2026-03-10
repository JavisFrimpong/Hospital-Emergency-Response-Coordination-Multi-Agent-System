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


# Simulation Loop
for i in range(3):

    patient, severity = emergency_agent.perceive()

    coordinator.decide_and_act(patient, severity)


database.display_records()