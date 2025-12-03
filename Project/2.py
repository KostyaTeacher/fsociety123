from flask import Flask, render_template, request
import random as r
from datetime import datetime

app = Flask(__name__)

list1 = ["Сьогодні у вас", "Завтра на вас", "Незабаром"]
list2 = ["чекає", "буде", "зустріне"]
list3 = ["гарна новина", "погана звіска", "гарний день", "поганий день"]
books =["Гаррі потер","Breaking Bad","Шахи"]
fruits_list = [
{"name": "Яблуко", "color": "red"},
{"name": "Банан", "color": "yellow"},
{"name": "Груша", "color": "green"},
{"name": "Вишня", "color": "red"},
{"name": "Ківі", "color": "green"},
{"name": "Апельсин", "color": "orange"}
]

@app.get('/')
def hello_world():
    return 'Привіт, світе!'

@app.post("/")
def get_fruits():
    action = request.form.get("action")
    name = request.form.get("name")
    color = request.form.get("color")
    if action == "add_fruit":
        fruits_list.append({"name":name, "color":color})
    if action == "delete_fruit":
        for fruit in fruits_list:
            if fruit["name"] == name:
                fruits_list.remove(fruit)

    return render_template("fruits.html", fruits=fruits_list)
@app.get("/horoskop/")
def horoskop():
    return f"{
    datetime.now
    ()} - {r.choice(list1)} {r.choice(list2)} {r.choice(list3)}"


@app.get("/home/")
def home():
    user = request.args.get('user')
    if user is None:
        user = "Anonim"
    age = request.args.get('age')
    if age is None:
        age = 0
    return render_template("index.html", name=user,age =int(age),
                           data=datetime.now
                           ())


@app.get("/submit/")
def get_submit():
    return render_template("submit.html")

@app.get("/books/")
def get_books():
    return render_template("books.html", books=books)
@app.post("/submit/")
def post_submit():
    name = request.form.get("name")
    return render_template("index.html", name=name)


if __name__ == '__main__':

    app.run(debug=True, port=5001)