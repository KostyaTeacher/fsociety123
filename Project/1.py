from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)

@app.get("/home/")
def home():
    name ="Gleb"
    dictionary ={
    "Ім'я":"gleb",
        "Вік":"16",
        "хобі":"Люблю в вільний час займатися програмуванням та грати в відеоігри",
        "місто яке я хотів відвідати":"Канада",
    }
    return render_template("index.html", dictionary=dictionary)
if __name__ == '__main__':
    app.run(debug=True,port=5000)