import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(unittest.TestCase):
    def test_set_attr(self):
        hardware = Hardware('test', 'Power', 200, 16)
        self.assertEqual(hardware.name, 'test')
        self.assertEqual(hardware.type, 'Power')
        self.assertEqual(hardware.capacity, 200)
        self.assertEqual(hardware.memory, 16)
        self.assertEqual(hardware.software_components, [])

    def test_install_with_bigger_memory(self):
        game = ExpressSoftware('game', 100, 32)
        hardware = Hardware('test', 'Power', 200, 16)

        with self.assertRaises(Exception) as content:
            hardware.install(game)

        self.assertEqual(str(content.exception), "Software cannot be installed")

    def test_with_bigger_capacity(self):
        game = ExpressSoftware('game', 300, 8)
        hardware = Hardware('test', 'Power', 200, 16)

        with self.assertRaises(Exception) as content:
            hardware.install(game)

        self.assertEqual(str(content.exception), "Software cannot be installed")

    def test_install(self):
        game = ExpressSoftware('game', 50, 4)
        hardware = Hardware('test', 'Power', 200, 16)
        hardware.install(game)

        self.assertEqual(hardware.software_components, [game])

    def test_uninstall(self):
        game = ExpressSoftware('game', 50, 4)
        hardware = Hardware('test', 'Power', 200, 16)
        hardware.install(game)

        self.assertEqual(hardware.software_components, [game])

        hardware.uninstall(game)

        self.assertEqual(hardware.software_components, [])