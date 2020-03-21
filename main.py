#!/usr/bin/env python3
import importing as imp

def main():
    image_path = imp.get_file()
    image = imp.conv_image(image_path)
    imp.get_parseImage(image)
    print("\nCreated by:\tDillon Bartram, Edward Aylott, Sorrel Paris, Taylor Dean")            #Credits
   

if __name__ == "__main__":
    main()
