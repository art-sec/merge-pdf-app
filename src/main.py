import PyPDF2
import os
# create the variable that contains the merger of pdf's
merger = PyPDF2.PdfMerger()

#create the variable that contains the pdf files and order it
filesList = os.listdir("pdf")
filesList.sort()

#create the loop that run the pdf directory and merge all the pdf files
for file in filesList:
    if file.endswith(".pdf"): #verify if the file it's really a pdf file
        merger.append(os.path.join("pdf", file))

#create the final pdf file
merger.write("Merged_PDF.pdf")
merger.close()

print("all the pdf are merged with sucess!")