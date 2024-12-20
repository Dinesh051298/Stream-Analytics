import numpy as np

class VFDTClassifier:
    """Classifier that categorizes data into predefined numeric ranges.

    Attributes:
        ranges (list of tuples): Numeric ranges defining the classification thresholds.
    """
    def __init__(self):
        self.ranges = [
            (0, 10),       # Very Low
            (10, 100),     # Low
            (100, 500),    # Medium
            (500, 1000),   # High
            (1000, float('inf'))  # Very High
        ]

    def classify(self, data):
        """Classify data points based on the predefined ranges.

        Args:
            data (np.array): Array of data points to classify.

        Returns:
            np.array: Array of class indices corresponding to the ranges.
        """
        classes = np.zeros(len(data), dtype=int)
        for index, (low, high) in enumerate(self.ranges):
            mask = (data >= low) & (data < high)
            classes[mask] = index
        return classes
