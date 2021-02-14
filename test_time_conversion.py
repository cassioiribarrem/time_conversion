from unittest import TestCase
from main import Time_conversion

class TestTimeConversion(TestCase):
    def tests_if_Time_Conversion_exists(self):
        if Time_conversion('07:05:45PM'):
            return

    def tests_if_Time_Conversion_receivies_parameter(self):
        assert result.s == '07:05:45PM'

    def tests_if_exploding_exists(self):
        if result.exploding():
            return

    def test_exploding_output(self):
        hour = '07:05:45PM'
        result = Time_conversion(hour)
        assert result.exploding() == ['0','7',':','0','5',':','4','5','P','M']

    def test_if_only_numbers_exist(self):
        if result.only_numbers():
            return

    def test_only_numbers_output(self):
        hour = '07:05:45PM'
        result = Time_conversion(hour)
        assert result.only_numbers() == ['0','7','0','5','4','5']

    def test_if_list_into_number_exists(self):
        if result.list_into_number():
            return

    def tests_list_into_number_output(self):
        hour = '07:05:45PM'
        result = Time_conversion(hour)
        assert result.list_into_number() == '070545'

    def tests_if_day_or_night_exists(self):
        if result.day_or_night():
            return

    def tests_day_or_night_output(self):
        hour = '12:05:45AM'
        result = Time_conversion(hour)
        if 'P' in result.s:
            assert result.day_or_night() == 190545
        elif result.only_numbers()[0] == '1' and result.only_numbers()[1] == '2':
            assert result.day_or_night() == '000545'



hour = '07:05:45PM'
result = Time_conversion(hour)