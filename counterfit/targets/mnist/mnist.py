# Generated by counterfit #

import pickle
import numpy as np
from counterfit.core.targets import ArtTarget


class Mnist(ArtTarget):
    model_name = "mnist"
    model_data_type = "image"
    model_endpoint = "counterfit/targets/tutorial/mnist_sklearn_pipeline.pkl"
    model_input_shape = (1, 28, 28)
    model_output_classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    X = []

    def __init__(self):
        self.clip_values = (0, 255)
        with open(self.model_endpoint, "rb") as f:
            self.model = pickle.load(f)

        self.data_file = "counterfit/targets/tutorial/mnist_784.npz"
        self.sample_data = np.load(self.data_file, allow_pickle=True)

        self.X = self.sample_data["X"]

    def __call__(self, x):
        scores = self.model.predict_proba(x.reshape(x.shape[0], -1))
        return scores.tolist()

'''
    def __init__(self):
        self.clip_values = (0, 255)
        with open(self.model_endpoint, "rb") as f:
            self.model = pickle.load(f)
        self.model = self.train_model(self.X, self.y)

    def train_model(self, X, y):
    model.fit(X, y)
    return model

    def __call__(self, x):
        scores = self.model.predict_proba(x.reshape(x.shape[0], -1))
        return scores.tolist()
'''