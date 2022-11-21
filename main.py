# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()


#def spellCheckDictionary_Linear():

#def spellCheckDictionary_Binary():

#def spellCheckAlice_Linear():

#def spellCheckAlice_Binary():


'''
menu = "Main Menu\n" + "1: Spell Check a Word (Linear Search)\n" + "2: Spell Check a Word (Binary Search)\n" + "3: Spell Check Alice In Wonderland (Linear Search)\n" + "4: Spell Check Alice In Wonderland (Binary Search)\n" + "5: Exit\n Please type your number: "

running = True
while running:
    selection = input(menu)
    if selection == "1":
        #spellCheckDictionary_Linear():
    elif selection == "2":
        #spellCheckDictionary_Binary():
    elif selection == "3":
        #spellCheckAlice_Linear()
    elif selection == "4":
        #spellCheckAlice_Binary()
    else:
        loop = False

'''