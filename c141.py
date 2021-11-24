from flask import Flask, request, jsonify
import csv

allMovies = []
with open("csv files/c141-1.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]
liked = []
disliked = []
notWatched = []

@app.route("/get-movie")

def getMovie():
    return jsonify({
    "data":allMovies[0],
    "status":"success"
    })

movieChoice = input("do you like this movie? ", allMovies["original_title"], "y if yes, n if no, and 0 for not seen.")
if movieChoice == "y":
    liked.append(movieChoice)
print(liked)

if __name__ == "__main__":
    app.run()
