# Natural Language Processing in Intellectual Property and Human Rights Law
## Project Summary
More information can be found in admin/preliminary_outline.txt.

## Progress
* Python script made to convert PDFs to TXT files.
* Python script made to give word count of all words in TXTs folders separately present these together in a graph. It also produces a csv file for the occurrence of key phrases and the occurence of other words in the same sentence as these phrases.

## Preparation
* Install Python.
* Install pdfminer library using pip or otherwise.
* Navigate to files in 'src' folder.

## Use
Enter the following commands into the terminal:
* "python convertPDFtoTXT.py $file_origin $start_page $end_page $file_destination", where:
  * $file_origin is the location of the file you want to convert from PDF to TXT (e.g. PDFs/example.pdf),
  * $file_destination is the location of where you want to output the TXT file (e.g. TXTs/example.txt),
  * $start_page is the number of the first page you want to change to text (with the first page of the PDF being 1). This is an optional argument. All pages will be converted if this is left blank,
  * $end_page is the number of the last page you want to change to text. This is an optional argument;
* "python allTXTsToCSVs.py"

## File Structure
* 'src' folder: contains code used to process data.
* 'admin' folder: contains files used to manage and administrate the project.
* 'submission' folder: contains all files submitted as required by course.

## Problems
* I haven't checked how to programs work on non-unix OSs. They might behave differently because of different ways that OSs process new lines and directory paths.
  * Pull Git repository to Windows OS and accomadate for differences in code so same code will work regardless of OS.
