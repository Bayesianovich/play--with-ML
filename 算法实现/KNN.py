def distance(a,b):
    return np.sqrt(np.sum((a-b)**2))


class KNN:
    """
    K-Nearest Neighbors (KNN) classifier.

    Parameters:
    - k (int): The number of nearest neighbors to consider.
    - label_num (int): The number of unique labels in the training data.

    Methods:
    - fit(x_train, y_train): Fit the KNN model with training data.
    - get_knn_indices(x): Get the indices of the k nearest neighbors for a given input.
    - get_label(x): Get the predicted label for a given input based on the k nearest neighbors.
    - predict(x_test): Predict the labels for a given set of test data.

    """

    def __init__(self, k, label_num):
        self.k = k    
        self.label_num = label_num
    
    def fit(self, x_train, y_train):
        """
        Fit the KNN model with training data.

        Parameters:
        - x_train (array-like): The training data features.
        - y_train (array-like): The training data labels.

        """
        self.x_train = x_train
        self.y_train = y_train
        
    def get_knn_indices(self, x):
        """
        Get the indices of the k nearest neighbors for a given input.

        Parameters:
        - x (array-like): The input data.

        Returns:
        - knn_indices (array-like): The indices of the k nearest neighbors.

        """
        distance = list(map(lambda a: distance(a, x), self.x_train))
        knn_indices = np.argsort(distance)
        knn_indices = knn_indices[:self.k]
        return knn_indices
    
    def get_label(self, x):
        """
        Get the predicted label for a given input based on the k nearest neighbors.

        Parameters:
        - x (array-like): The input data.

        Returns:
        - label (int): The predicted label.

        """
        knn_indices = self.get_knn_indices(x)
        label_stat = np.zeros(shape=[self.label_num])
        for index in knn_indices:
            label = int(self.y_train[index])
            label_stat[label] += 1
        return np.argmax(label_stat)
    
    def predict(self, x_test):
        """
        Predict the labels for a given set of test data.

        Parameters:
        - x_test (array-like): The test data.

        Returns:
        - predicted_test_labels (array-like): The predicted labels for the test data.

        """
        predicted_test_labels = np.zeros(shape=[len(x_test)], dtype=np.int32)
        for i, x in enumerate(x_test):
            predicted_test_labels[i] = self.get_label(x)
        return predicted_test_labels