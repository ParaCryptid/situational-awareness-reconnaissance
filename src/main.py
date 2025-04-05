import logging
from src.real_time_alerts import AIEnhancedAlerts
from src.blockchain_collaboration import Blockchain
from src.federated_learning import FederatedLearningModel
from src.geospatial_monitor import GeospatialMonitor
from src.post_quantum_encryption import PostQuantumEncryptor

def run_demo():
    logging.info("Launching OSINT Toolkit Demo")

    # Real-Time Alerts
    alerts = AIEnhancedAlerts(["Device A", "Sector B"])
    alerts.start_monitoring(interval=1)
    
    # Blockchain
    chain = Blockchain()
    chain.create_block(data="Surveillance Event")

    # Federated Learning
    fl = FederatedLearningModel()
    fl.add_client_model([1.0, 2.0, 3.0])
    fl.add_client_model([2.0, 3.0, 4.0])
    fl.aggregate_models()

    # Geospatial Monitoring
    geo = GeospatialMonitor({
        "lat_min": 50.0, "lat_max": 52.0,
        "lon_min": -1.0, "lon_max": 1.0
    })
    geo.simulate_collection(3)

    # Post-Quantum Encryption
    pqe = PostQuantumEncryptor()
    pub = pqe.export_public_key()
    shared = pqe.generate_shared_key(pub)

    alerts.stop_monitoring()
    logging.info("Toolkit demo complete.")

if __name__ == "__main__":
    run_demo()
