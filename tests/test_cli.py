import unittest
import rip


class TestCliArgParser(unittest.TestCase):
    def test_parser_help(self):
        with self.assertRaises(SystemExit):
            parser = rip.cli.arg_parser(["-h"])

    def test_status_help(self):
        with self.assertRaises(SystemExit):
            parser = rip.cli.arg_parser(["status", "-h"])


if __name__ == "__main__":
    unittest.main()
