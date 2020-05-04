#!/usr/bin/env python3

import os.path as path
import csv

FILENAME = "history.csv"
HISTORY = []

class SaveUserEntries():

    def saveFileLocation():
        history = HISTORY

        while True:
            if path.exists(FILENAME):
                with open (FILENAME, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(history)
                    break
            else:
                with open("history.csv", "wb") as file:
                    writer = csv.writer(file)
                    continue