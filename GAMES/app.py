from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
     return render_template("Home.html")

#CREATION DE NOS JEUX

games = []

@app.route("/saisie")
def displayGameCreationForm():
     return render_template("Saisie.html")

@app.route("/ajout", methods=['POST'])
def postNewGame():
   game = {"name": request.form["name"], "price" : request.form["price"], "desc": request.form["desc"]}
   games.append(game)
   return redirect("/jeux")

@app.route("/edit", methods=['POST'])
def editGame():
   game = {"name": request.form["name"], "price" : request.form["price"], "desc": request.form["desc"]}
   games[int(request.form["name_id"])] = game
   return redirect("/jeux")

@app.route("/jeux")
def displayGamesList():
   return render_template("Liste.html", games = games)

@app.route("/delete/<id>", methods=['GET'])
def removeGameList(id):
     games.pop(int(id))
     return redirect("/jeux")

@app.route("/update/<id>", methods=['GET'])
def updateGameList(id):
     return render_template("Edit.html", edit_id = id)