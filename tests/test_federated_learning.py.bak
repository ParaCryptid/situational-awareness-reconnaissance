
from src.federated_learning import FederatedLearningModel
import numpy as np

def test_federated_learning_aggregation():
    model = FederatedLearningModel()
    model.add_client_model(np.array([0.1, 0.2, 0.3]))
    model.add_client_model(np.array([0.2, 0.3, 0.4]))
    global_weights = model.aggregate_models()
    assert global_weights is not None
