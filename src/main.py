import PyPDF2
import os
# create the variable that contains the merger of pdf's
merger = PyPDF2.PdfMerger

#create the variable that contains the pdf files and order it
filesList = os.listdir("pdf")
filesList.sort()

#create the loop that run the pdf directory and merge all the pdf files
for file in filesList:
    if ".pdf" in file:
        merger.append(f"pdf/{file}")

#create the final pdf file
merger.write("Merger PDF.pdf")