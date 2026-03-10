class EmergencyAgent:

    def __init__(self, monitor):
        self.monitor = monitor

    def perceive(self):
        return self.monitor.detect_emergency()