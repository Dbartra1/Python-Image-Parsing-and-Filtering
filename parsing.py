#!/usr/bin/env python3
import importing as imp
import csv
import os.path as path

FILENAME = "history.csv"


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
