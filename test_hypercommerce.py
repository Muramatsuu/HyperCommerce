# test_hypercommerce.py
"""
Tests for HyperCommerce module.
"""

import unittest
from hypercommerce import HyperCommerce

class TestHyperCommerce(unittest.TestCase):
    """Test cases for HyperCommerce class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HyperCommerce()
        self.assertIsInstance(instance, HyperCommerce)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HyperCommerce()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
