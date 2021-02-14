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

    def day_or_night(self):
        pass
