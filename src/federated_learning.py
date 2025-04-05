import numpy as np
import logging
from typing import List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class FederatedLearningModel:
    def __init__(self):
        """Initialize the federated learning model."""
        self.global_model = None
        self.client_models: List[np.ndarray] = []

    def add_client_model(self, model_weights: np.ndarray):
        """
        Add client model weights for aggregation.
        :param model_weights: Weights of the client model.
        """
        if not isinstance(model_weights, np.ndarray):
            raise TypeError("Model weights must be a numpy array.")
        self.client_models.append(model_weights)
        logging.info(f"Added client model with shape {model_weights.shape}")

    def aggregate_models(self) -> np.ndarray:
        """
        Aggregate all client models to update the global model.
        :return: Aggregated model weights.
        """
        if not self.client_models:
            raise ValueError("No client models available for aggregation.")
        self.global_model = np.mean(self.client_models, axis=0)
        logging.info(f"Global model updated with shape {self.global_model.shape}")
        return self.global_model
