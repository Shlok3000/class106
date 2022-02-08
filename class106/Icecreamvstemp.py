import csv
import plotly.express as px

with open("Data1.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x = "Temperature", y = "Cold drink sales")
    fig.show()