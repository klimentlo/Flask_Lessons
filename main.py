"""
title: flask Lessons
author: kliment lo
date: december 1, 2022
"""
import csv
from flask import Flask, render_template, request

# --- GLOBAL VARIABLES --- #
FILENAME = "flask.csv"

# --- FLASK --- #
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    readFile(FILENAME)
    if request.form:
        FIRSTNAME = request.form.get("first_name")
        LASTNAME = request.form.get("last_name")
        EMAIL = request.form.get("email")
        if checkContent(EMAIL):
            createContact(FIRSTNAME, LASTNAME, EMAIL)
        else:
            pass
    return render_template("index.html")

# --- CSV --- #
def readFile(FILENAME):
    '''
    opens out csv vile and erads the contents to an array. IF the file has not been created yet, create it now
    :param FILENAME:
    :return: HEADER, DATA: Our CSV header and the
    '''

    try:
        with open(FILENAME, newline="") as FILE:
            READER = csv.reader(FILE)
            HEADER = next(READER)
            DATA = []
            for row in READER:
                DATA.append(row)
        return HEADER, DATA
    except:
        with open(FILENAME, "w",newline="") as FILE:
            WRITER = csv.writer(FILE)
            HEADER = ["First Name", "Last Name", "Email"]
            WRITER.writerow(HEADER)
        return readFile(FILENAME)

def createContact(FIRSTNAME, LASTNAME, EMAIL):
    '''
    creates a contact and adds it to our csv file using the data received from our flask application
    :param FIRSTNAME:
    :param LASTNAME:
    :param EMAIL:
    :return:
    '''
    CONTACT = [FIRSTNAME, LASTNAME, EMAIL]
    with open(FILENAME, "a", newline="") as FILE:
        WRITER = csv.writer(FILE)
        WRITER.writerow(CONTACT)

def checkContent(EMAIL):
    '''
    checks to see if the email esxists in the CSV already
    :param EMAIL:
    :return:
    '''
    with open(FILENAME, newline="") as FILE:
        READER = csv.reader(FILE)
        for ROW in READER:
            if ROW[2] == EMAIL:
                return False
        return True

if __name__ == "__main__":
    app.run(debug=True)
