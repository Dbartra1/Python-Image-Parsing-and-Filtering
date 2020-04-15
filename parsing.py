#!/usr/bin/env python3
import importing as imp
import csv
import os.path as path

FILENAME = "savedLocation.csv"

def saveFileLocation(image_path):
    savedLocations = []
    while True:
        if path.exists(FILENAME):
            with open (FILENAME, "a", newline="") as file:
                writer = csv.writer(file)
                savedLocations.append(image_path)
                writer.writerow(savedLocations)
                break
        else:
            with open("savedLocation.csv", "wb") as file:
                writer = csv.writer(file)
                writer.writerow(savedLocations)
                continue
