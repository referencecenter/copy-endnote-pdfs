# copy-endnote-pdfs

These programs copy all PDFs from an EndNote library's .Data subfolders to one single folder.

## Background

In the [__EndNote__](https://endnote.com/ 'EndNote | The best reference management tool') desktop application, libraries include multiple files: The main library file has an .enl extension, but it is connected to a .Data folder, which includes other files. The desktop application is able to automatically retrieve the full texts of some references. Users can upload additional full-text files they have access to. Full texts can include PDF files, which are saved in separate folders within the .Data folder. 

Without something like these programs, users need to manually go into each .Data subfolder and copy the PDFs.

## Potential Use Cases

* A researcher wants to share PDFs with collaborators who do not have access to the EndNote library.
* A patron wants full-text access to the articles a librarian included in a literature search.

## Which Program to Use?

### Requirements

These programs require three pieces of information:

* The name of the EndNote library
* The filepath of the folder where the EndNote library and its associated data folder is saved
* The filepath of the folder to which you want to copy the PDFs

There are different ways to provide this information. None of them requires you to know Python, but one requires you to make small changes to the code. Depending on your comfort level and whether you have Python installed, you may prefer one program over another.

### Programs

* [__copy-endnote-pdfs.py__](https://github.com/referencecenter/copy-endnote-pdfs/blob/main/copy-endnote-pdfs.py 'copy-endnote-pdfs/copy-endnote-pdfs.py at main • referencecenter/copy-endnote-pdfs') requires you to have Python installed and to edit three lines of code to provide the needed information.
* [__copy-endnote-pdfs_interactive.py__](https://github.com/referencecenter/copy-endnote-pdfs/blob/main/copy-endnote-pdfs_interactive.py 'copy-endnote-pdfs/copy-endnote-pdfs_interactive.py at main • referencecenter/copy-endnote-pdfs') requires you to have Python installed, but you can just run the program, and it will prompt you for the needed information without you needing to edit the code.
* To run the previous program without Python installed, download [__copy-endnote-pdfs_interactive.zip__](https://github.com/referencecenter/copy-endnote-pdfs/blob/main/copy-endnote-pdfs_interactive.zip 'copy-endnote-pdfs/copy-endnote-pdfs_interactive.zip at main • referencecenter/copy-endnote-pdfs'), extract the compressed contents, and run __dist/copy-endnote-pdfs_interactive.exe__. The downside is that this program is slower.
