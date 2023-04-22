import unittest
import rip


class TestVersion(unittest.TestCase):
    def test_module_version(self):
        self.assertRegex(rip.version.__version__, r"^[0-9]*\.[0-9]*\.[0-9]*$")


if __name__ == "__main__":
    unittest.main()
