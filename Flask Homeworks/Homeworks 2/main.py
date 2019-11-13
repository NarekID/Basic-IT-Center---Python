# Պրոյեկտի նկարագրություն
# / - GET, index.html էջը պիտի ցույց տա բոլոր օգտագործողներին ու իրենց արած տնայինները։
# / - POST-ով պետք է ավելացնենք օգտագործող(ուղարկում ենք օգտագործողի անունը)
# /<userName> GET - պիտի վերադարձնի տվյալ օգտագործողի արած տնայինները
# /<userName> POST էդ user-ի համար պիտի ավելացնի արված տնային աշխատանքը
# Usern—ներին կարաք պահեք dict-ի մեջ,
# {"username1":{"hometask1", "hometask2"}}
# key-ը string է, իսկ value—ն set,

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import jsonify

app = Flask(__name__)
users = {"Alex": {"Ex 10, 12, 15", "Learn something new in Python"},
         "John": {"Learn something new in Python"},
         "Sara": {"Ex 10, 11, 12, 15, 19, 20", "Read a book"}
         }


@app.route("/", methods=["GET", "POST"])
def main_page():
    print(users)
    if request.method == "POST":
        if len(request.form["new_user"]) > 1:
            users.update({request.form["new_user"]: {""}})
    return render_template("index.html", users=users)


@app.route("/<userName>", methods=["GET", "POST"])
def user_page(userName):
    print(users)
    if request.method == "POST":
        if len(request.form["new_homework"]) > 0:
            if "" in users[userName]:
                users[userName].remove("")
            users[userName].add(request.form["new_homework"])
    else:
        if userName not in users.keys():
            return redirect("/")
    return render_template("index.html", homeworks=list(users[userName]), user=userName)

app.run()
