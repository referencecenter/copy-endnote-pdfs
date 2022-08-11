#! python3
# copy-endnote-pdfs.py

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
The only lines users will need to edit are between the long lines of
    hashes (lines 39-58). Specifically, they will need to edit the
    variables in lines 47, 52, and 57 to reflect their specific EndNote
    library and the appropriate filepaths. Note the caution in lines 41–
    42 regarding hard drives vs. network drives."""

# Import libraries.
import shutil
import os
import glob
from pathlib import Path

########################################################################
# Specify variables.
# I recommend using folders on a hard drive. While this program should
    # work on a network drive, it is MUCH slower.

# Specify the source path. This is the folder where the EndNote library
    # and its associated .Data folder are located. Replace only what is
    # between the quotation marks, not the "r" that precedes them.
source_path = r"C:\Users\rastley\Documents\EndNote Libraries"

# Specify the name of the EndNote library, without the extension. (For
    # example, "Maternal Mortality," not "Maternal Mortality.enl.")
    # Medical Education.enl."
library_name = "Predictors of Relationship Persistence"

# Specify the destination path. This is the folder to which the PDF
    # files will be copied. Replace only what is between the quotation
    # marks, not the "r" that precedes them.
destination_path = r"C:\Users\rastley\Documents\PDFs"
########################################################################

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
