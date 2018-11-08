# Natural Language Processing in Intellectual Property and Human Rights Law
## Project Summary
More information can be found in admin/preliminary_outline.txt.

## Progress
* Python script made to convert PDFs to TXT files.
* Python script made to clean data and count words.

## Preparation
* Install Python.
* Install pdfminer library using pip or otherwise.
* Navigate to files in 'src' folder.

## Use
Enter the following commands into the terminal:
* "python convertPDFtoTXT.py example.pdf $start_page $end_page",
  * Where $start_page is the number of the first page you want to change to text (with the first page of the PDF being 1) and $end_page is the last. These can be left blank if all pages from the PDF are wanted.
* "python tokeniseTXT.py example.txt",
* "cat exampleCount.csv".

## File Structure
* 'src' folder: contains code used to process data.
* 'admin' folder: contains files used to manage and administrate the project.
* 'submission' folder: contains all files submitted as required by course.
