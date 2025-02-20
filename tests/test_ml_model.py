import unittest
import numpy as np
from ml_model.inference import predict_cpu_usage

class TestMLModel(unittest.TestCase):
    
    def test_prediction(self):
        input_data = np.random.rand(10).tolist()
        prediction = predict_cpu_usage(input_data)
        self.assertTrue(0 <= prediction <= 1)

if __name__ == '__main__':
    unittest.main()