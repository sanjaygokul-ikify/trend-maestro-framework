import unittest
from cli.main import main

class TestRuntime(unittest.TestCase):
    def test_cli(self):
        main()