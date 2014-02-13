
import unittest

from mock import patch
from jujuplugin.helpers import ext, exit


class JujuPluginHelpersTest(unittest.TestCase):
    def test_exit_linux(self):
        self.assertEqual('', ext())
