# 🏥 Hospital Emergency Response Coordination Multi-Agent System

This project is an intelligent **Multi-Agent System (MAS)** designed to simulate and manage an emergency hospital response scenario. It automates the detection of emergencies and optimally assigns them to available hospital doctors based on workload and availability.

This was developed as the **DCIT 403 – Intelligent Agents Individual Semester Project**.

---

## 🏗️ Architecture

The system mimics a real-world hospital workflow by utilizing three distinct intelligent agents that coordinate through a centralized environment:

1. **EmergencyAgent (Perceptor)**: Scans the hospital environment (via the `EmergencyMonitor`) for incoming emergency cases. When an alert triggers, it captures the patient's identity, case severity, and exact timestamp, passing them down the pipeline.
2. **CoordinatorAgent (Decision Maker)**: Acts as the brain of the workflow. It receives an emergency case and queries all hospital doctors for their availability and willingness to accept the case. It evaluates their current workload, selects the optimal doctor for assignment, and balances the hospital's resources gracefully. If no doctor is available, it escalates the emergency externally.
3. **DoctorAgent (Actor)**: Represents the hospital's medical professionals. Each doctor maintains a personal schedule, accepts or rejects cases based on random dynamic availability, and keeps a track record of their workload.

The environment connects everything together seamlessly:
* **EmergencyMonitor**: Generates mock emergency situations dynamically using randomized patient profiles and varying severity levels (Low, Medium, High, Critical).
* **NotificationSystem**: Dispatches communication alerts to individual doctors once assigned.
* **HospitalDatabase**: Persists every single system action, tracking exactly when a case was detected, which doctor was assigned, workloads, and finally compiling a beautiful formatted final report at the end of the simulation.

## 🚀 Features
* **Dynamic Time Tracking**: Fully records `datetime` elements corresponding to the precise emergency detection and dispatch times.
* **Workload Balancing**: Advanced Coordination logic that queries available doctors and assigns cases to the one with the lowest workload, ensuring no doctor is overburdened.
* **Dynamic Doctor Availability**: Doctors simulate busy cycles upon assignment. Their status dynamically frees up at probabilistic intervals down the simulation loop.
* **Intelligent Escalation**: A fallback safety net gracefully transitions emergencies to external departments when all hospital resources are maxed out.
* **End-of-Run Automated Reporting**: Generates a visually appealing hospital status report detailing patient tracking matrices.

---

## 🛠️ Project Structure

```bash
Hospital-Emergency-Response-Coordination-Multi-Agent-System/
│
├── agents/ 
│   ├── coordinator_agent.py   # Code for CoordinatorAgent decision-making
│   ├── doctor_agent.py        # Code for DoctorAgent workload and evaluations
│   └── emergency_agent.py     # Code for EmergencyAgent perception
│
├── environment/ 
│   ├── emergency_monitor.py   # Generates emergency interrupts
│   ├── hospital_database.py   # Records state transitions and final reporting
│   └── notification_system.py # Simulates alert outputs to actors
│
├── simulation/ 
│   └── emergency_cases.py     # Mock data decoupling for patient simulation
│
├── main.py                    # Core execution loop & system integration
└── README.md                  # Project documentation
```

## ⚙️ How to Run

### Prerequisites
* Requires **Python 3.x** installed on your system.
* No external libraries (e.g. `pip install`) are required. The project relies entirely on standard built-in Python libraries (`random`, `datetime`, `time`).

### Execution
To run the simulation and monitor the agents coordinating in real-time, launch the main module from your terminal:

```bash
python main.py
```

### Saving the Output
If you want to save the final report to a text file rather than simply printing it to the console, redirect the standard output (`stdout`) to a file in your terminal:

**Windows Command Prompt / PowerShell:**
```bash
python main.py > test_output.txt
```
*(Note: By default, Python's `print()` outputs directly to the console. The above command instructs the operating system to intercept the console display and write it securely into `test_output.txt`.)*

---

**Developed for DCIT 403.**
