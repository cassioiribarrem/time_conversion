from unittest import TestCase
from main import Time_conversion

class TestTimeConversion(TestCase):
    def tests_if_Time_Conversion_exists(self):
        if Time_conversion('07:05:45PM'):
            return

    def tests_if_Time_Conversion_receivies_parameter(self):
        assert result.s == '07:05:45PM'

    def tests_if_day_or_night_exists(self):
        if result.day_or_night():
            return

    def tests_if_exploding_exists(self):
        if result.exploding():
            return

    def test_exploding_output(self):
        assert result.exploding() == ['0','7',':','0','5',':','4','5','P','M']

    def test_if_only_numbers_exist(self):
        if result.only_numbers():
            return

    def test_only_numbers_output(self):
        assert result.only_numbers() == ['0','7','0','5','4','5']

hour = '07:05:45PM'
result = Time_conversion(hour)