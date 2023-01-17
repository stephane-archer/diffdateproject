import sys
import datetime

def printusage():
    print("usage is: diffdate 12-01-2023 22-12-2022")

def main():
    if len(sys.argv) != 3:
        printusage()
        exit()

    dates = []
    for date in sys.argv[1:]:
        s = date.split('-')
        if len(s) != 3:
            printusage()
            exit()
        dates.append(datetime.date(int(s[2]),int(s[1]),int(s[0])))

    if len(dates) != 2:
        printusage()
        exit()

    print(abs((dates[0] - dates[1]).days))

if __name__ == "__main__":
    main()
