#!/usr/bin/env python3
import importing as imp
import parsing as parse
import color_space as cs
import gui

def main():
    gui.displayMenu()

    while True:
        parse.readInHistory()
        while True:
            selection = input("Please select a Menu Item to begin: ")
            try:
                if selection.casefold() == "new":

                    image_path = imp.get_file()
                    parse.saveFileLocation(image_path)
                    image = cs.modifyImageSize(image_path)
                    inputs = cs.modifyImageColor(image)
                    parse.saveUsrInput(inputs)

                    result = input("Go back to the main menu? (y/n): ")                                                  #Allowing for the program to run as many times as needed.
                    print()
                    if result.casefold() == "y":
                        parse.readInHistory()                                                                            #Read in csv for updated list.
                        gui.displayMenu()
                        continue
                    else:
                        break
        
                elif selection.casefold() == "history":

                    history1 = parse.removeCharacters()
                    print(history1)

                    result = input("Go back to the main menu? (y/n): ")                                                  #Allowing for the program to run as many times as needed.
                    print()
                    if result.casefold() == "y":
                        gui.displayMenu()
                        continue
                    else:
                        break
        
                elif selection.casefold() == "quit":
                    break

                else:
                    print("Invalid Input, Try again\n")
                    continue

            except ValueError:
                print("Invalid Input, Try again\n")

        break
    print("\nCreated by: Dillon Bartram, Edward Aylott, Sorrel Paris, Taylor Dean")            #Credits
   

if __name__ == "__main__":
    main()
