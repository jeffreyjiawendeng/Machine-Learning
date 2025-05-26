"""K Nearest Neighbors (KNN) Classifier Implementation"""

class KNN:
    def __self__(self, k=1, weights="uniform", metric="minkowski", p=2):
        self.k = k
        self.weights = weights
        self.metric = metric
        self.p = p
        self.X_train = None
        self.y_train = None