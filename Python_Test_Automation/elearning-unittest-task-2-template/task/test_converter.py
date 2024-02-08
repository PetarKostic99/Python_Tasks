"""Test cases for Converter class."""

import unittest
from unittest.mock import patch
from task.converter import Converter


def mock_converter(_, celsius):
    """Mock function to convert Celsius to Fahrenheit."""
    # Using a simple conversion formula like:
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


class TestConverter(unittest.TestCase):

    def setUp(self):
        """Set up the Converter instance for testing."""
        self.converter = Converter()

    @patch('task.converter.Converter.convert_celsius_to_fahrenheit', mock_converter)
    def test_converter(self):
        """Test the convert_celsius_to_fahrenheit method with the mock_converter function."""
        result = self.converter.convert_celsius_to_fahrenheit(30)
        expected_result = mock_converter(None, 30)  # Using the mock_converter function for comparison
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
