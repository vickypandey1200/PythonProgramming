import re
import argparse

def Main():

    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="specify word to search")
    parser.add_argument("fname", help="specify file to search from")
    args = parser.parse_args()

    searchFile = open(args.fname)
    lineNume=0

    for line in searchFile.readLines():
        line = line.strip("\n\r")
        lineNum+=1
        searchResult =  re.search(args.word, line, re.M|re.I)
        if searchResult:
            print(str(lineNum)+" : "+line)

if __name__ == "__main__":
    Main()
