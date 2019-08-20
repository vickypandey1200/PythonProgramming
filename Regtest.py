import re

def Main():
    line = "I think I understand regular expressions"

    matchResult = re.match("think", line, re.M|re.I)
    if matchResult:
        print("Match found : "+matchResult.group())
    else:
        print("No match was found..")


    searchResult = re.search("think", line, re.M|re.I)
    if searchResult:
        print("Search Found: "+searchResult.group())
    else:
        print("Nothing found while searching")


if __name__=="__main__":
    Main()
