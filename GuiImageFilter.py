#!/usr/bin/env python3
import cv2
import numpy as np
import csv
import os
import json
import tkinter as tk
import tkinter.ttk as ttk

from tkinter import Toplevel
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from tkinter import Label, Text, Frame, Scrollbar
from tkinter import END, TOP, HORIZONTAL, VERTICAL, BOTTOM, RIGHT, Y, X, W, SE, NW, NO, S


from datalayer import SaveUserEntries as SUE
from datalayer import HISTORY as saving
from datalayer import FILENAME as fName


class GetFileLocation(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.withdraw = master.withdraw

    def createWidgets(self):
        self.bGetImage = tk.Button(self, text = "Get Image Path", fg="black", command=self.getImagePath)
        self.bGetImage.pack(side="left")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="left")
    
    def getImagePath(self):
        global IMAGE_PATH
        files = [('jpg files', '*.jpg'),  
             ('png files', '*.png'), 
             ('jpeg files', '*.jpeg')] 
        try:
            file = askopenfile(mode ='r', filetypes = files)
            IMAGE_PATH = file.name
            self.withdraw()
        
        except AttributeError:
            messagebox.showerror("Error", "No File Selected")

class ResizeImage(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.image = None

    def createWidgets(self):
        self.lImageSize = tk.Label(self, text="Image Size (1-200): ")
        self.lImageSize.pack(side="left") 
        self.eImageSize = tk.Entry(self)
        self.eImageSize.pack(side="left")

        self.EditSize = tk.Button(self, text = "Submit", fg="green", command=self.resizeImage)
        self.EditSize.pack(side="left")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="left")

    def resizeImage(self):
        #Initializing global values
        global IMAGE
        global WIDTH
        global HEIGHT
        global CHANNELS
        global iScale_percent

        try:
            SCALE_PERCENT = self.eImageSize.get()
            iScale_percent = int(SCALE_PERCENT)
            if iScale_percent <= 200:
                IMAGE = cv2.imread(IMAGE_PATH) 
                WIDTH, HEIGHT, CHANNELS = IMAGE.shape
                WIDTH = int(IMAGE.shape[1] * iScale_percent / 100)
                HEIGHT = int(IMAGE.shape[0] * iScale_percent / 100)
                IMAGE = cv2.resize(IMAGE, (WIDTH, HEIGHT), interpolation = cv2.INTER_AREA)
            else:
                raise Exception
        except (NameError, ValueError, Exception):
            messagebox.showerror("Error", "Either no image is selected or invalid input has been entered.\nFor more information see instructions")

class FilterImage(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.lRedRGB = tk.Label(self, text="Red RGB Value (0-255): ")
        self.lRedRGB.pack(side="left") 
        self.eRedRGB = tk.Entry(self)
        self.eRedRGB.pack(side="left")

        self.lGreenRGB = tk.Label(self, text="Green RGB Value (0-255): ")
        self.lGreenRGB.pack(side="left") 
        self.eGreenRGB = tk.Entry(self)
        self.eGreenRGB.pack(side="left")

        self.lBlueRGB = tk.Label(self, text="Blue RGB Value (0-255): ")
        self.lBlueRGB.pack(side="left") 
        self.eBlueRGB = tk.Entry(self)
        self.eBlueRGB.pack(side="left")

        self.lOpacity = tk.Label(self, text="Opacity RGB Value (.001-1.0): ")
        self.lOpacity.pack(side="left") 
        self.eOpacity = tk.Entry(self)
        self.eOpacity.pack(side="left")


        self.bSubmit = tk.Button(self, text = "Submit", fg="green", command=self.setRGBValues)
        self.bSubmit.pack(side="left")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="left")

    def setRGBValues(self):
        #Initializing global values
        global FINAL_IMAGE
        global SIDE_BY_SIDE
        global iRed
        global iGreen
        global iBlue
        global fOpacity

        #Gui produces strings, taking the string values and making them correct variable types
        try:
            RED = self.eRedRGB.get()
            iRed = int(RED)
            GREEN = self.eGreenRGB.get()
            iGreen = int(GREEN)
            BLUE = self.eBlueRGB.get()
            iBlue = int(BLUE)
            OPACITY = self.eOpacity.get()
            fOpacity = float(OPACITY)

            if iRed >= 0 and iGreen >= 0 and iBlue >= 0 and fOpacity >= .001 and iRed <= 255 and iGreen <= 255 and iBlue <= 255 and fOpacity <= 1.0:
                #Buidlng and Adding the filter
                filteredImage =  np.full((HEIGHT, WIDTH, CHANNELS), (iBlue, iGreen, iRed), np.uint8)           
                FINAL_IMAGE = cv2.addWeighted(IMAGE, 1, filteredImage, fOpacity, 0)

                #For Comparing the Images
                SIDE_BY_SIDE = np.concatenate((FINAL_IMAGE, IMAGE), axis = 1)
            else:
                raise Exception
        except (NameError, ValueError, Exception):
            messagebox.showerror("Error", "Please ensure all steps were followed and try again.\nFor more information see instructions")

class ShowFilteredImage(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        self.bShowFiltered = tk.Button(self, text = "Filtered Image", fg="black", command=self.onlyFilteredImage)
        self.bShowFiltered.pack(side="left")

        self.bShowCompared = tk.Button(self, text = "Comparing Images", fg="black", command=self.comparedImages)
        self.bShowCompared.pack(side="left")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="left")

    def onlyFilteredImage(self):
        try:
            filteredImageWinName = "Filtered Image"
            cv2.imshow(filteredImageWinName,  FINAL_IMAGE)                                                       
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except NameError:
            messagebox.showerror("Error", "Looks like you skipped a step?")
    
    def comparedImages(self):
        try:
            comparisonImageWinName = "Comparison"
            cv2.imshow(comparisonImageWinName, SIDE_BY_SIDE)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except NameError:
            messagebox.showerror("Error", "Looks like you skipped a step?")

class SaveFilteredImage(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.withdraw = master.withdraw
    
    def createWidgets(self):
        self.bFilter = tk.Button(self, text = "Save", fg="black", command=self.saveFilteredImage)
        self.bFilter.pack(side="left")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="left")

    def saveFilteredImage(self):
        files = [('jpg files', '*.jpg'),  
             ('png files', '*.png'), 
             ('jpeg files', '*.jpeg')]
        try:
            file = asksaveasfile(filetypes = files, defaultextension = files)
            path = file.name

            cv2.imwrite(path, FINAL_IMAGE)
            cv2.waitKey(0)

            saving.extend((IMAGE_PATH, iScale_percent, iRed, iGreen, iBlue, fOpacity, path))
            SUE.saveFileLocation()
            self.withdraw()
        except(AttributeError, NameError):
            messagebox.showerror("Error", "Failed to save image. Please try again.")

class InstructionsForUser(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.withdraw = master.withdraw

    def createWidgets(self):
        self.bIntruc = tk.Button(self, text = "Instructions", fg="black", command=self.instructions)
        self.bIntruc.pack(side="left")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="left")

    def instructions(self):
        self.withdraw()
        instructionsString = ("To run the filtering program, note all options must be done in order. \n\n" + 
                              "The order is signified through numerical notations of 1 – 5. The steps are as follows:\n\n" +
                              "1) An image must be selected. \n" + 
                              "2) The image must be resized between a value of 1 and 200.\n3) Filter parameters must be entered as follows:\n" + 
                              "\t3.1)RGB values must be 0 and 255 and Opacity value \t\t      between .001 and 1.0. \n" +
                              "4) The filtered image can now be opened.\n" + "5) The filtered image can now be saved.\n\n" +
                              "NOTE: Step 5 can wait till after the desired image filter and size have been selected. Backtracking is possible. " + 
                              "The interface will remain open until the main \"Quit\" option is selected.")
        messagebox.showinfo("Instructions", instructionsString)

class ViewHistory(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.geometry = master.geometry
        self.resizable = master.resizable
        self.withdraw = master.withdraw

    def createWidgets(self):
        self.bHistory = tk.Button(self, text = "View History", fg="black", command=self.viewHistory)
        self.bHistory.pack(side="left")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="left")

    def viewHistory(self):

        try:
            width = 500
            height = 400
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            self.geometry("%dx%d+%d+%d" % (width, height, x, y))
            self.resizable(0, 0)

            TableMargin = Frame(self, width=500)
            TableMargin.pack(side=TOP)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin, columns=("File Path", "Resize Paramter", "Red Filter Level", "Green Filter Level",
                                                     "Blue Filter Level", "Opacity Scale", "Saved Image Path"), height=400, selectmode="extended", 
                                                     yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('File Path', text="File Path", anchor=W)
            tree.heading('Resize Paramter', text="Resize Paramter", anchor=W)
            tree.heading('Red Filter Level', text="Red Filter Level", anchor=W)
            tree.heading('Green Filter Level', text="Green Filter Level", anchor=W)
            tree.heading('Blue Filter Level', text="Blue Filter Level", anchor=W)
            tree.heading('Opacity Scale', text="Opacity Scale", anchor=W)
            tree.heading('Saved Image Path', text="Saved Image Path", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=350)
            tree.column('#2', stretch=NO, minwidth=0, width=100)
            tree.column('#3', stretch=NO, minwidth=0, width=100)
            tree.column('#4', stretch=NO, minwidth=0, width=100)
            tree.column('#5', stretch=NO, minwidth=0, width=100)
            tree.column('#6', stretch=NO, minwidth=0, width=100)
            tree.column('#7', stretch=NO, minwidth=0, width=350)
            tree.pack()

            with open(fName) as file:
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    filePath = row['File Path']
                    reParamter = row['Resize Paramter']
                    rLevel = row['Red Filter Level']
                    gLevel = row['Green Filter Level']
                    bLevel = row['Blue Filter Level']
                    oScale = row['Opacity Scale']
                    savedPath = row['Saved Image Path']
                    tree.insert("", 0, values=(filePath, reParamter, rLevel, gLevel, bLevel, oScale, savedPath))
        
        except FileNotFoundError:
            self.withdraw()
            messagebox.showerror("Error", "No history available. Please try again.")

            
class MainMenuApp(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        self.bImageCapture = tk.Button(self, text="View Instructions", command = self.instructionsForUser)
        self.bImageCapture.pack(side="top")

        self.bImageCapture = tk.Button(self, text="[1] Select an Image", command = self.imagePathCapture)
        self.bImageCapture.pack(side="top")
        
        self.bResize = tk.Button(self, text="[2] Resize the Image", command = self.resizeImage)
        self.bResize.pack(side="top")
        
        self.bfilter = tk.Button(self, text="[3] Enter Filter Paramters", command = self.filterImage)
        self.bfilter.pack(side="top")
        
        self.bShow = tk.Button(self, text="[4] View Filtered Image", command = self.showImage)
        self.bShow.pack(side="top")

        self.bSave = tk.Button(self, text="[5] Save Filtered Image", command = self.saveFile)
        self.bSave.pack(side="top")

        self.bSave = tk.Button(self, text="View Previous Filter Settings", command = self.viewHistory)
        self.bSave.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command= self.master.destroy)
        self.QUIT.pack(side="bottom")


    def imagePathCapture(self):
        print("Getting Image Path...")
        root2 = tk.Toplevel()
        buildApp = GetFileLocation(master = root2)
        
    def resizeImage(self):
        print("Resizing...")
        root3 = tk.Toplevel()
        buildApp2 = ResizeImage(master = root3)

    def filterImage(self):
        print("Loading color sync...")
        root4 = tk.Toplevel()
        buildApp3 = FilterImage(master = root4)

    def showImage(self):
        print("Loading Filtered Image...")
        root5 = tk.Toplevel()
        buildApp4 = ShowFilteredImage(master = root5)

    def saveFile(self):
        print("Saving...")
        root6 = tk.Toplevel()
        buildApp5 = SaveFilteredImage(master = root6)

    def instructionsForUser(self):
        print("Loading...")
        root7 = tk.Toplevel()
        buildApp6 = InstructionsForUser(master = root7)

    def viewHistory(self):
        print("Loading...")
        root8 = tk.Toplevel()
        buildApp7 = ViewHistory(master = root8)

root = tk.Tk()
app = MainMenuApp(master=root)
app.master.title("The Filter Image Program")

app.mainloop()
