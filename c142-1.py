import csv

allMovies = []
with open("csv files/c142-1.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]
likedMovies = []
dislikedMovies = []
didNotWatch = []
