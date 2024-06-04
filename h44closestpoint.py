#name: victoria inahuazo
#date: 04/18/24
#email: victoria.inahuazo11@myhunter.cuny.edu


#Enter CSV file name: cunyLocations.csv
#Enter column name for latitude: Latitude
#Enter column name for longitude: Longitude
#Enter current latitude: 40.7021
#Enter current longitude: -73.9708
#Enter output file: closestCUNY.html#


import pandas as pd
import matplotlib as pyplot



def getData():
    csvF = input("Enter CSV file name:")
    return pd.read_csv(csvF)
    

def getColumnNames():
    laC = input("Enter column name for latitude:")
    longC = input("Enter column name for longitude:")
    return (laC, longC)


def getLocale():
    latX = float(input("Enter current latitude:"))
    longY = float(input("Enter current longitude:"))

def computeDist(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

def main():
    outF = input("Enter output file:")


if __name__ == "__main__":
    main()