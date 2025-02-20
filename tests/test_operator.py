import unittest
from unittest.mock import patch
from kaiscaler_operator import predict_scaling

class TestOperator(unittest.TestCase):
    
    @patch('kaiscaler_operator.get_metrics', return_value=[0.2, 0.3, 0.5, 0.6, 0.8])
    def test_predict_scaling(self, mock_metrics):
        prediction = predict_scaling()
        self.assertTrue(0 <= prediction <= 1)

if __name__ == '__main__':
    unittest.main()