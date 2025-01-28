import numpy as np

class FederatedLearningModel:
    def __init__(self):
        """
        Initialize the federated learning model.
        """
        self.global_model = None
        self.client_models = []

    def add_client_model(self, model_weights):
        """
        Add client model weights for aggregation.
        :param model_weights: Weights of the client model.
        """
        self.client_models.append(model_weights)

    def aggregate_models(self):
        """
        Aggregate client models into the global model.
        """
        if not self.client_models:
            raise ValueError("No client models to aggregate.")
        
        # Compute average weights
        self.global_model = np.mean(self.client_models, axis=0)
        self.client_models = []  # Reset for next round

        return self.global_model

# Example usage
# federated_model = FederatedLearningModel()
# client_weights1 = np.array([0.1, 0.2, 0.3])
# client_weights2 = np.array([0.2, 0.3, 0.4])
# federated_model.add_client_model(client_weights1)
# federated_model.add_client_model(client_weights2)
# global_weights = federated_model.aggregate_models()
# print("Aggregated Global Weights:", global_weights)
