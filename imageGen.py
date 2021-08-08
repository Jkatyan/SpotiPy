import os
import sys
import io

import urllib.request
import tkinter as tk
from tkinter import filedialog
from PIL import Image

url = ""
uri = ""
imagePath = ""
outputPath = ""
outputName = ""

window = tk.Tk()

urlEntryFrame = tk.Frame()
urlLabel = tk.Label(master=urlEntryFrame, text="Spotify Track URL:")
urlEntry = tk.Entry(master=urlEntryFrame, width=100)

imgEntryFrame = tk.Frame()
imgLabel = tk.Label(master=imgEntryFrame, text="Album Art:")
imgButton = tk.Button(master=imgEntryFrame, text="Upload File")

outputDirectoryFrame = tk.Frame()
outputLabel = tk.Label(master=outputDirectoryFrame, text="Output Directory:")
outputButton = tk.Button(master=outputDirectoryFrame, text="Select Folder")

outputLabelFrame = tk.Frame()
outputNameLabel = tk.Label(master=outputLabelFrame, text="Output File Name:")
outputNameEntry = tk.Entry(master=outputLabelFrame, width=50)

submitButton = tk.Button(text="Generate Image")

def handle_upload(event=None):
    global imagePath
    imagePath = str(filedialog.askopenfilename())
    print("Selected: " + imagePath)

def handle_search(event=None):
    global outputPath
    outputPath = str(filedialog.askdirectory())
    print("Selected: " + outputPath)
    
def handle_submit(event):
    url = urlEntry.get()
    print("URL: " + url)
    indexStart = url.find("/", 30)
    indexEnd = url.find("?", 30)
    uri = "https://scannables.scdn.co/uri/plain/jpeg/000000/white/1200/spotify:track:" + url[indexStart + 1 : indexEnd]
    print("URI: " + uri)
    urlEntry.delete(0, tk.END)
    outputName = outputNameEntry.get()
    print("Output File: " + outputPath + "/" + outputName + ".png")
    outputNameEntry.delete(0, tk.END)

    print(imagePath)
    print(outputPath)

    new = Image.new("RGBA", (1200,1590))

    art = Image.open(str(imagePath))
    art = art.resize((1200,1200))

    urllib.request.urlretrieve(uri, "code.jpeg")
    code = Image.open("code.jpeg")
    code = code.resize((1200,300))

    rect = Image.new('RGB', (1200,45), "black")

    new.paste(art, (0,0))
    new.paste(rect, (0,1200))
    new.paste(code, (0,1245))
    new.paste(rect, (0,1545))
    new.save(outputPath + "/" + outputName + ".png")

    imgButton.configure(relief= 'groove')
    outputButton.configure(relief= 'groove')
    submitButton.configure(relief= 'groove')


def loadUI():
    urlEntryFrame.grid(row=0, column=0, pady=10)
    urlLabel.grid(row=0)
    urlEntry.grid(row=1, column=0)

    imgEntryFrame.grid(row=1, column=0, pady=10)
    imgLabel.grid(row=0, column=0, padx=10)
    imgButton.configure(relief= 'groove')
    imgButton.bind("<Button-1>", handle_upload)
    imgButton.grid(row=0, column=1)

    outputDirectoryFrame.grid(row=2, column=0, pady=10)
    outputLabel.grid(row=0, column=0, padx=10)
    outputButton.configure(relief= 'groove')
    outputButton.bind("<Button-1>", handle_search)
    outputButton.grid(row=0, column=1)

    outputLabelFrame.grid(row=3, column=0)
    outputNameLabel.grid(row=0, column=0, sticky="w")
    outputNameEntry.grid(row=0, column=1)

    submitButton.bind("<Button-1>", handle_submit)
    submitButton.grid(row=4, column=0, pady=20)
    submitButton.configure(relief= 'groove')

def run():
    loadUI()
    window.mainloop()

run()