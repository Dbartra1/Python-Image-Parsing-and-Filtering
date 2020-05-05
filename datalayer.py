#!/usr/bin/env python3

import os.path as path
import csv

FILENAME = "history.csv"
HISTORY = []

class SaveUserEntries():


    def saveFileLocation():
        history = HISTORY
        header = ["File Path", "Resize Paramter", "Red Filter Level", "Green Filter Level", "Blue Filter Level", "Opacity Scale", "Saved Image Path"]

        while True:
            if path.exists(FILENAME):
                with open (FILENAME, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(history)
                    HISTORY.clear()
                    break
            else:
                with open('history.csv', 'w', newline='') as outcsv:
                    writer = csv.writer(outcsv)
                    writer.writerow(header)
                    continue
