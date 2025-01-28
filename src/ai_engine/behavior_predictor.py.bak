from sklearn.ensemble import RandomForestClassifier
import numpy as np

class BehaviorPredictor:
    def __init__(self):
        # Initialize a RandomForestClassifier model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.is_trained = False

    def train_model(self, features, labels):
        """
        Train the prediction model with historical data.
        :param features: A 2D array of input features.
        :param labels: A 1D array of corresponding labels.
        """
        self.model.fit(features, labels)
        self.is_trained = True

    def predict_behavior(self, new_features):
        """
        Predict future behavior based on input features.
        :param new_features: A 2D array of features to predict.
        :return: Predicted labels.
        """
        if not self.is_trained:
            raise ValueError("Model is not trained. Train the model before prediction.")
        return self.model.predict(new_features)

# Example usage
# predictor = BehaviorPredictor()
# predictor.train_model([[0.1, 0.2], [0.4, 0.6]], [0, 1])
# result = predictor.predict_behavior([[0.3, 0.5]])
# print("Predicted Behavior:", result)
