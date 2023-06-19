class Dates:
    def __init__(self,date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/","-")

if __name__ == '__main__':
    date = Dates("13-6-2023")
    date1 = "13/6/2023"

    dateWithDash = Dates.toDashDate(date1)

    dateWithObj = date.getDate()

    if dateWithDash == dateWithObj:
        print("They are equal")
    else:
        print("They are not equal")