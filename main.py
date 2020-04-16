#!/usr/bin/env python3
import importing as imp
import parsing as parse
import color_space as cs

def main():
    while True:
        image_path = imp.get_file()
        history = parse.saveFileLocation(image_path)
        image = cs.modifyImageSize(image_path)
        inputs = cs.modifyImageColor(image)
        parse.saveUsrInput(inputs)

        result = input("Continue? (y/n): ")                                                    #Allowing for the program to run as many times as needed.
        print()
        if result.lower () != "y":
            break
    print("\nCreated by: Dillon Bartram, Edward Aylott, Sorrel Paris, Taylor Dean")            #Credits
   

if __name__ == "__main__":
    main()
