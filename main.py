class Time_conversion():
    def __init__(self, s):
        self.s = s
        return

    def exploding(self):
        list = []
        for i in range(0, len(self.s)):
            list.append(self.s[i])
        return list

    def only_numbers(self):
        list = self.exploding().copy()
        del (list[2])
        del (list[4])
        del (list[6])
        del (list[6])
        return list

    def list_into_number(self):
        list = self.only_numbers()
        hour = ''
        for i in range(0, len(list)):
            hour += list[i]
        return hour

    def day_or_night(self):
        if 'P' in self.s:
            hour = int(self.list_into_number())
            if self.only_numbers()[0] == '1' and self.only_numbers()[1] == '2':
                military_time = str(hour)
            else:
                military_time = str(hour + 120000)
            return military_time

        elif self.only_numbers()[0] == '1' and self.only_numbers()[1] == '2':
            hour = int(self.list_into_number())
            military_time = hour - 120000
            military_time = str(military_time)
            zeros = 6 - len(military_time)
            military_time = '0'*zeros + military_time
            return military_time

        else:
            military_time = self.list_into_number()
            return military_time

    def string_into_list(self):
        list = []
        for i in range(0, len(self.day_or_night())):
            list.append(self.day_or_night()[i])
        return list

    def formatation(self):
        list = []
        list = self.string_into_list().copy()
        list.insert(2, ':')
        list.insert(5, ':')
        return list

    def list_into_string(self):
        hour_in_military_time = ''
        for i in range(0, len(self.formatation())):
            hour_in_military_time += self.formatation()[i]
        return hour_in_military_time

    def conversion(self):
        conversion = self.list_into_string()
        print(conversion)
        return conversion

result = Time_conversion('12:45:54PM')
result.conversion()