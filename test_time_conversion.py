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

    def tests_day_or_night_output_when_PM(self):
        hour = '07:05:45PM'
        result = Time_conversion(hour)
        assert result.day_or_night() == '190545'

    def tests_day_or_night_output_when_AM(self):
        hour = '07:05:45AM'
        result = Time_conversion(hour)
        assert result.day_or_night() == '070545'

    def test_day_or_night_output_when_12AM(self):
        hour = '12:05:45AM'
        result = Time_conversion(hour)
        assert result.day_or_night() == '000545'

    def tests_if_strings_into_list_exists(self):
        if result.string_into_list():
            return

    def tests_strings_into_list_output(self):
        assert result.string_into_list() == ['1', '9', '0', '5', '4', '5']

    def test_formatation_existence(self):
        if result.formatation():
            return

    def test_formatation_output(self):
        assert result.formatation() == ['1', '9', ':', '0', '5', ':', '4', '5']

    def test_list_into_string_existence(self):
        if result.list_into_string():
            return

    def test_list_into_string_output(self):
        assert result.list_into_string() == '19:05:45'

    def test_if_conversion_exists(self):
        if result.conversion():
            return

    def test_conversion_output(self):
        assert result.conversion() == '19:05:45'



hour = '07:05:45PM'
result = Time_conversion(hour)