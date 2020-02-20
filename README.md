# Natural Language Processing in the Law Domain
## University of Bristol - Final Year Project

### Overview
The project was a contribution to a law academic’s research into the growing relationship between intellectual property law and human rights law; in particular, the extent to which intellectual property laws involve human rights considerations, and their balance between consideration of creators and users.

Notably, the project's results and its future work were enthusiastically discussed at the British and Irish Law Education and Technology conference 2019.


### Key Requirements
The project was broadly split into three key areas: natural language processing, visualisation and usability. See my [presentation poster](https://github.com/org9711/Natural-Language-Processing-in-IP-HR-Law/blob/master/poster.pdf) for a brief overview.
* Natural language processing: Create two models - one to identify whether a documents is remated more to human rights or to intellectual property; the other to identify whether a document indicates that the current legal climate more strongly benefits the user of intellectual property or the creator of it.
* Visualisation: Display the results of these models in a way that clearly shows any trends that exist.
* Usability: Create a user interface which allows anyone to input their own documents and display the results. Furhter, develop the code base in a fashion that allows it to be expanded upon by others for future work.

### Results
#### Natural Language Processing
* The topic classification of HR-IP, done using machine learning techniques, gave strong results with a balanced accuracy score of 0.984.
* The average p-values of the trends for HR and IP documents were higher than the significance threshold so no trends in the results could be claimed to be significant.
* Given limited time of the academic, there was not enough means to evaluate what was a simple user-creator model and therefore no conclusions could be drawn from it.

#### Visualisation
* The academic said she 'agreed' (Likert scale) that all five key visualisation evaluation aims were met.
* The law academics at BILETA did not need the meanings of the graphs to be explained to them.

#### Usability
* All desired functionality for the tool was accessible through a tool that could be accessed via Windows and Ubuntu desktops.  
* The academic, however, expressed desire for the tool to not need downloading.

### Conclusions and Future Work
* Natural language processing: Similar trends frequently appeared but none were statistically significant. To investigate trends further, n-grams could be used to give context to the text, or more documents could be used to increase reliability.
* Visalisation: More advanced 3D visualisation framworks could be used in order to enable academics to see trends that appear across three dimensions.
* Usability: If demand were to warrant it, the tool could be hosted on the cloud so nothing would need to be installed and so academics could use the tool collaboratively. The codebase could have be more useable if automated testing would have been used to give a future developer confidence that the tool works as expected.

### Technologies
The entire project was written in Python as it is the standard for data science applications. Some frameworks I used to assist me are listed below:
* PDF scraping: pdfminer
* Topic classification: sklearn
* Trend detection: statsmodels
* Visualisation: matplotlib
* User interface: tkinter

### Further Reading
If you somehow have the time, you're welcome to browse all my findings in detail in my [thesis](https://github.com/org9711/Natural-Language-Processing-in-IP-HR-Law/blob/master/thesis.pdf).

Further, all the code for the project can be viewed in the [src](https://github.com/org9711/Natural-Language-Processing-in-IP-HR-Law/tree/master/src) folder above.
