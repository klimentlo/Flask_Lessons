"""
title: flask Lessons
author: kliment lo
date: december 1, 2022
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.form:
        print(request.form.get("first_name"))
        print(request.form.get("last_name"))
        print(request.form.get("email"))
    return render_template("index.html")



app.run(debub=True)
