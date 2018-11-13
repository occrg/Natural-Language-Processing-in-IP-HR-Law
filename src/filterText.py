import sys

from tokeniseTXT import openTXTfile

def removePars(text, keyphrase):
    text = text

def removeSentences(text, keyphrase):
    text = text

def main():
    if(len(sys.argv) != 3):
        raise ValueError("Wrong number of arguments. There should be 2 (excluding Python file name).")
    origin = sys.argv[1]
    destination = sys.argv[2]
    keyphrase = "intellectual"
    text = openTXTfile(origin)
    text = removePars(text, keyphrase)

if __name__ == '__main__':
    main()
