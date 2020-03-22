#!/usr/bin/env python3
import importing as imp

def main():
    while True:
        image_path = imp.get_file()
        image = imp.conv_image(image_path)
        imp.get_parseImage(image)

        result = input("Continue? (y/n): ")                                                    #Allowing for the program to run as many times as needed.
        print()
        if result.lower() != "y":
            break
    print("\nCreated by: Dillon Bartram, Edward Aylott, Sorrel Paris, Taylor Dean")            #Credits
   

if __name__ == "__main__":
    main()
