import unittest
from modules.dns_checker import check_dns
from modules.connectivity import check_ping

class ToolkitTests(unittest.TestCase):
    def test_dns_returns_dict(self):
        result = check_dns("localhost")
        self.assertIsInstance(result, dict)
        self.assertIn("status", result)

    def test_empty_ping_host_is_handled(self):
        result = check_ping("")
        self.assertEqual(result["status"], "UNKNOWN")

if __name__ == "__main__":
    unittest.main()
