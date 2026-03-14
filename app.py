from flask import Flask, render_template, request
from datetime import datetime
import pytz
import time
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    greeting = ""
    name = ""
    thought = ""
    bg = "day"

    thoughts = [
        "Your presence has a beautiful way of making every moment feel special.",
        "Some people make the world brighter just by being in it, and you are one of them.",
        "A beautiful day becomes even better when you are part of it.",
        "Little moments become unforgettable with the right person around.",
        "Your smile has a way of making everything feel lighter."
    ]

     if request.method == "POST":

     name = request.form["name"]

     india = pytz.timezone("Asia/Kolkata")
      timestamp = datetime.now(india).hour

  if 6 <= timestamp < 12:
    greeting = "Good Morning"
    bg = "morning"

elif 12 <= timestamp < 18:
    greeting = "Good Afternoon"
    bg = "afternoon"

elif 18 <= timestamp < 22:
    greeting = "Good Evening"
    bg = "evening"

else:
    greeting = "Good Night"
    bg = "night"

thought = random.choice(thoughts)

return render_template("index.html", greeting=greeting, name=name, thought=thought, bg=bg)


import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
