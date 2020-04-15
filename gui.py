#!/usr/bin/env python3
# importing libraries 
import parsing as parse
import importing as imp

def displayMenu():
    print("COMMAND MENU")
    listOfOptions = """
    list - Display prior converstions
    edit - Modify Image
    """
def listPaths(history):
    if len(history) == 0:
        print("The file contains no paths.\n")
        return
    else:
        i = 0
        for path in history:
            print(str(i+1) + ". " + path[0])
            i += 1
        print()

def edit(image_path):
