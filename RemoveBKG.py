import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image
import os
import time

#Get path using windows
root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
print("Folder path: "+file_path)

res = []
resBackup = []
resWithoutExt=res
separator="."

# Iterate directory
for path in os.listdir(file_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(file_path, path)):
        res.append(path)
        resBackup.append(path)

# Remove extension
for j in range(len(res)):
    resWithoutExt[j]=res[j].split(separator, 1)[0]

# Get length from vector files
length=len(resBackup)
porcent=round(100/length)
jump=round(20/length)

print("Ready for start removing background")
for j in range(0,20,1):
    time.sleep(0.25)
    print("-",end=" ")

print("Progress:\n")

for i in range(len(res)):
    input_path = file_path+"/"+resBackup[i]
    output_path = file_path+"/"+"CLEARED_"+resWithoutExt[i]+".png"
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    # Status bar
    if i==length-1:
        print("["+"#"*jump*(i+1)+"]"+"100%")
    else:
        print("["+"#"*jump*(i+1)+"]"+str(porcent*(i+1))+"%")

print("---------------------------------")

print("Remove background succesfully")