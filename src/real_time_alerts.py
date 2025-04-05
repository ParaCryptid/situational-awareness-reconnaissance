import time
import random
import threading
import logging
from typing import List, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class AIEnhancedAlerts:
    def __init__(self, monitored_entities: List[str]):
        """
        Initialize the alert system with monitored entities.
        :param monitored_entities: List of entities to monitor (e.g., devices, regions, or systems).
        """
        self.monitored_entities = monitored_entities
        self.running = False
        self.thread: Optional[threading.Thread] = None

    def generate_alert(self, entity: str) -> str:
        """
        Generate a mock AI-enhanced alert for a given entity.
        :param entity: The entity being monitored.
        :return: An alert message with risk level.
        """
        risk_level = random.choice(["Low", "Medium", "High", "Critical"])
        return f"Alert for {entity}: Risk Level {risk_level}"

    def _monitor_loop(self, interval: int):
        """
        Internal loop that runs in a separate thread to monitor entities.
        :param interval: Time interval (in seconds) between checks.
        """
        self.running = True
        while self.running:
            for entity in self.monitored_entities:
                alert = self.generate_alert(entity)
                logging.info(alert)
            time.sleep(interval)

    def start_monitoring(self, interval: int = 5):
        """
        Start monitoring in a separate thread.
        :param interval: Time interval (in seconds) between checks.
        """
        if not self.running:
            self.thread = threading.Thread(target=self._monitor_loop, args=(interval,))
            self.thread.start()
            logging.info("Monitoring started.")

    def stop_monitoring(self):
        """
        Stop the monitoring thread gracefully.
        """
        self.running = False
        if self.thread:
            self.thread.join()
            logging.info("Monitoring stopped.")
