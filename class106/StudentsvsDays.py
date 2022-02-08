import csv
import numpy as np

def getDataSource(data_path):
    size_of_TV = []
    average_time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_TV.append(float(row["Marks In Percentage"]))
            average_time_spent.append(float(row["Days Present"]))
    return {"x": size_of_TV, "y": average_time_spent}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between Student Marks and Days students attended school: ", correlation[0,1])

def setup():
    data_path = "Data4.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()