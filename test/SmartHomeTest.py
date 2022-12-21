import unittest
from unittest.mock import patch, PropertyMock

import mock.adafruit_dht as adafruit_dht
import mock.GPIO as GPIO
from SmartHome import SmartHome
from SmartHomeError import SmartHomeError


class SmartHomeTest(unittest.TestCase):
    """
    Your test cases go here
    """
    def setUp(self) -> None:
        self.sh = SmartHome()

    @patch.object(GPIO, 'input')
    def test_occupancy(self, mock_input):
        mock_input.return_value = 0
        occ = self.sh.check_room_occupancy()
        self.assertTrue(occ)

    @patch.object(GPIO, 'input')
    def test_ligh_level1(self, mock_input):
        mock_input.side_effect = [0, 495]
        self.sh.manage_light_level()
        ligh = self.sh.light_on
        self.assertTrue(ligh)

    @patch.object(GPIO, 'input')
    def test_ligh_level2(self, mock_input):
        mock_input.side_effect = [0, 505]
        self.sh.manage_light_level()
        ligh = self.sh.light_on
        self.assertFalse(ligh)

    @patch('mock.adafruit_dht.DHT11.temperature', new_callable=PropertyMock)
    def test_manage_window1(self, mock_input_temperature):
        mock_input_temperature.side_effect = [20, 26] #[indoorT, outdoorT]
        self.sh.manage_window()
        window = self.sh.window_open
        self.assertTrue(window)

    @patch('mock.adafruit_dht.DHT11.temperature', new_callable=PropertyMock)
    def test_manage_window2(self, mock_input_temperature):
        mock_input_temperature.side_effect = [25, 20]  # [indoorT, outdoorT]
        self.sh.manage_window()
        window = self.sh.window_open
        self.assertFalse(window)

    @patch.object(GPIO, 'input')
    def test_gas_detection1(self, mock_input):
        mock_input.return_value = 0
        self.sh.monitor_air_quality()
        buzzer = self.sh.buzzer_on
        self.assertTrue(buzzer)

    @patch.object(GPIO, 'input')
    def test_gas_detection2(self, mock_input):
        mock_input.return_value = 1
        self.sh.monitor_air_quality()
        buzzer = self.sh.buzzer_on
        self.assertFalse(buzzer)







