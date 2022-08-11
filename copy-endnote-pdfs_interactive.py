#! python3
# copy-endnote-pdfs_interactive.py

"""
Background:
In the desktop application, EndNote libraries include multiple files:
    The main library file has an .enl extension, but it is connected
    to a .Data folder, which includes other files. The desktop
    application is able to automatically retrieve the full texts of some
    references. Users can upload additional full-text files they have
    access to. Full texts can include PDF files, which are saved in
    separate folders within the .Data folder. Without something like
    this program, users need to manually go into each .Data subfolder
    and copy the PDFs.

Description:
This program copies all PDFs from an EndNote library's .Data subfolders
    to one single folder.

Sample Use Cases:
(1) A researcher wants to share PDFs with collaborators who do not have
    access to the EndNote library.
(2) A patron wants full-text access to the articles a librarian included
    in a literature search.

Instructions:
Users do not need to edit any of the code; simply run the program and
    provide the needed information upon request."""

# Import libraries.
import shutil
import os
import glob
from pathlib import Path

# Introduce the program.
print("Welcome! This program copies all PDFs from an EndNote library's .Data")
print("    subfolders to one single folder. It will run much more efficiently")
print("    if the library is saved to your hard drive instead of a network")
print("    drive. If your library is saved to a network drive, please")
print("    consider saving a copy to your hard drive before proceeding.")

print("\nPress \"Enter\" to continue.")

proceed = input()

print("The program requires some information to proceed.")

# Request the source path.
print("\nPlease type the path of the folder your EndNote library is saved in")
print("    and press \"Enter.\"")
print("\nFor example: C:\\Users\\rastley\\Documents\\EndNote Libraries")

source_path = input()

# Request the EndNote library name.
print("\nThank you. Please type the name of your EndNote library, NOT")
print("    including the .enl extension.")
print("\nFor example: Predictors of Relationship Persistence")

library_name = input()

# Request the destination path.
print("\nThank you. Please type the path of the folder to which you want to")
print("    copy the PDF files and press \"Enter.\" Again, note that using a")
print("    location on your hard drive will mak")
print("\nFor example: C:\\Users\\rastley\\Documents\\PDFs")
print("\n(Again, note that using a location on your hard drive will make this")
print("    program much more efficient.)")

destination_path = input()

print("\nThank you. The program is now working on copying the files.")

# Change the working directory to the source path.
os.chdir(source_path)

# Specify the name of the PDF folder.
pdf_folder = library_name + r".Data\PDF"

# Create a list to which to add the subfolders that contain the PDFs.
subfolders = []

# Add all subfolders within the PDF folder.
for subfolder in os.listdir(pdf_folder):
    subfolders.append(subfolder)

# Create a list to which to add the filepaths for the PDFs themselves.
pdf_paths = []

# Add the filepaths for the PDFs to the new list.
for subfolder in subfolders:
    pdf_paths.append(pdf_folder + "\\" + subfolder + "\\*.pdf")

# Using the PDF filepaths, copy each PDF to the destination path.
for path in pdf_paths:
    for file in glob.glob(path):
        shutil.copy(file, destination_path)

# Inform the user that the program has finished.
print("\nThe PDF files should now all be in the destination folder. Press")
print("    \"Enter\" to close this program.")

close = input()
