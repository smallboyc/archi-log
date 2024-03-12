from flask import Flask, render_template, request
import random

random_number = random.randint(0,100)
app = Flask(__name__)

@app.route("/")
def hello_world():
     return render_template("test.html", el = random_number)

@app.route("/result", methods=['POST'])
def display():
     return render_template("test.html", el = request.form["name"])


# @app.route("/form/<name>")
# def test(name):
#     return render_template("form.html", el = name)

# @app.route("/appli")
# def appliPage():
#     return "<p>Bienvenue dans mon application</p>"


#LE JEU DU PLUS OU MOINS

@app.route("/moreorless")
def LoadGamePage():
     return render_template("MoreOrLess.html")

@app.route("/game", methods=['POST'])
def CheckGameResponse():
    number = int(request.form["number"])
    response = ""
    if (number < random_number):
        response = "C'est plus !"
    elif (number > random_number):
        response = "C'est moins !"
    else :
        response = f"bing vous avez trouvé {random_number} qui était la target !"
    return render_template("MoreOrLess.html", response = response)



