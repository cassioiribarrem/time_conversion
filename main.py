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
            military_time = str(hour + 120000)
            return military_time

        elif self.only_numbers()[0] == '1' and self.only_numbers()[1] == '2':
            hour = int(self.list_into_number())
            military_time = hour - 120000
            military_time = '000' + str(military_time)
            return military_time

        else:
            military_time = self.list_into_number()
            return military_time



""" hour = ''
     if 'P' in self.s:
         del(list[2])
         del(list[4])
         del(list[6])
         del(list[6])

         for i in range(0, len(list)):
             hour += list[i]

         list =[]
         military_time = int(hour) + 120000

         for i in range(0, len(str(military_time))):
             list.append(str(military_time)[i])
         list.insert(2,':')
         list.insert(5,':')
         hour = ''

         for i in range(0, len(list)):
             hour+= list[i]

         if int(hour) == 24:


     else:
         del(list[8])
         del(list[8])

         hour = ''
         for i in range(0, len(list)):
             hour += list[i]

     print(hour)"""

result = Time_conversion('11:05:45AM')
result.day_or_night()