#!/usr/bin/env python3
import importing as imp
import csv
import os.path as path

FILENAME = "history.csv"
HISTORY = []


def saveFileLocation(image_path):
    history = []

    while True:
        if path.exists(FILENAME):
            with open (FILENAME, "a", newline="") as file:
                writer = csv.writer(file)
                history.append(image_path)
                writer.writerow(history)
                break
        else:
            with open("history.csv", "wb") as file:
                writer = csv.writer(file)
                continue

def saveUsrInput(inputs):
    filename = FILENAME
    with open (filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer = writer.writerow(inputs)

#Reading in the CSV to memory.
def readInHistory():
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            HISTORY.append(row)
    str(HISTORY).replace('[','').replace(']','')

#Format list to a string and then strip unwanted characters.
def removeCharacters():
    return str(HISTORY).replace('[','\n').replace(']','\n').replace('\'', '').replace(',', '')
