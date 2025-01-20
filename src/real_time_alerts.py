import time
import random

class AIEnhancedAlerts:
    def __init__(self, monitored_entities):
        """
        Initialize the alert system with monitored entities.
        :param monitored_entities: List of entities to monitor (e.g., devices, regions, or systems).
        """
        self.monitored_entities = monitored_entities

    def generate_alert(self, entity):
        """
        Generate a mock AI-enhanced alert for a given entity.
        :param entity: The entity being monitored.
        :return: An alert message with risk level.
        """
        risk_level = random.choice(["Low", "Medium", "High", "Critical"])
        return f"Alert for {entity}: Risk Level {risk_level}"

    def monitor_and_alert(self, interval=5):
        """
        Continuously monitor entities and generate alerts.
        :param interval: Time interval (in seconds) between checks.
        """
        while True:
            for entity in self.monitored_entities:
                alert = self.generate_alert(entity)
                print(alert)
            time.sleep(interval)

# Example usage
# entities = ["Device A", "Region B", "System C"]
# alert_system = AIEnhancedAlerts(entities)
# alert_system.monitor_and_alert(interval=10)
