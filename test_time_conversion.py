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

    def test_the_split_of_sentence(self):

hour = '07:05:45PM'
result = Time_conversion(hour)