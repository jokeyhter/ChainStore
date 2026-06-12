# test_chainstore.py
"""
Tests for ChainStore module.
"""

import unittest
from chainstore import ChainStore

class TestChainStore(unittest.TestCase):
    """Test cases for ChainStore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainStore()
        self.assertIsInstance(instance, ChainStore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainStore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
