# test_sharddrift.py
"""
Tests for ShardDrift module.
"""

import unittest
from sharddrift import ShardDrift

class TestShardDrift(unittest.TestCase):
    """Test cases for ShardDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShardDrift()
        self.assertIsInstance(instance, ShardDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShardDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
