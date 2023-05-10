import datetime as dt


class Python1:

    def __init__(self, name):
        self.name = name

    def todaysTime(self):
        dated = str(dt.datetime.today())
        return "today's date and time is " + dated + "__ and the sent name is " + self.name


if __name__ == "__main__":
    print(Python1("shiva").todaysTime())
