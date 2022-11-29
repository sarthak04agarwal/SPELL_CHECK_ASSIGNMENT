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

    # Menu to present to the user
    menu = "Main Menu\n" + "1: Spell Check a Word (Linear Search)\n" + "2: Spell Check a Word (Binary Search)\n" + "3: Spell Check Alice In Wonderland (Linear Search)\n" + "4: Spell Check Alice In Wonderland (Binary Search)\n" + "5: Exit\n Please type your number: "
    # Asks the user what function to run
    running = True
    while running:
        selection = input(menu)
        if selection == "1":
            spellCheckDictionary_Linear(dictionary)
        elif selection == "2":
            spellCheckDictionary_Binary(dictionary)
        elif selection == "3":
            spellCheckAlice_Linear(dictionary, aliceWords)
        elif selection == "4":
            spellCheckAlice_Binary(dictionary, aliceWords)
        else:
            running = False
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()





# Takes in dictionary and asks the user for a input value, and then uses Linear Search to see if the value is in the Dictionary
def spellCheckDictionary_Linear(dictionary):
    dictionary_Word = input("Please input the word that you would like to search in the dictionary: ")
    dictionary_Word = dictionary_Word.lower()
    for i in range(len(dictionary-1)):
        if dictionary[i] == dictionary_Word:
            print("Linear Seach: " + dictionary_Word + "is IN the dictionary at position " + i) 
        
    print("Linear Search: " + dictionary_Word + "is NOT IN the dictionary.")


# Takes in dictionary and asks the user for a input value, and then uses Binary Search to see if the value is in the Dictionary
def spellCheckDictionary_Binary(dictionary):
    dictionary_Word = input("Please input the word that you would like to search in the dictionary: ")
    dictionary_Word = dictionary_Word.lower()
    low = 0
    high = len(dictionary) - 1
 
    while low <= high:
        mid = (high + low) // 2
        if dictionary[mid] < dictionary_Word:
            low = mid + 1
 
        elif dictionary[mid] > dictionary_Word:
            high = mid - 1
 
        else:
            print("Binary Search: " + dictionary_Word + "is IN the dictionary at position " + str(mid) + ".")
 
    print("Binary Search: " + dictionary_Word + " is NOT IN the dictionary.")
   
# Takes in aliceWords and dictionary and uses a Linear Search to search how many of the words from aliceWords are not found in the Dictionary
def spellCheckAlice_Linear(dictionary, aliceWords):
    wordNotIncluded = 0
    for x in range(len(aliceWords)):
        if aliceWords.lower[x] not in dictionary:
            wordNotIncluded+= 1
    print("Linear Search" + wordNotIncluded + "words NOT found in the dictionary.")

# Takes in aliceWords and dictionary and uses a Binary Search to search how many of the words from aliceWords are not found in the Dictionary
def spellCheckAlice_Binary(aliceWords, dictionary):
    wordNotIncluded = 0 
    for x in range(len(aliceWords)):
        low = 0
        high = len(dictionary) - 1
    
        wordNotIncluded = 0 
        while low <= high:
 
            mid = (high + low) // 2
            if dictionary[mid] < aliceWords.lower[x]:
                low = mid + 1
 
            elif dictionary[mid] > aliceWords.lower[x]:
                high = mid - 1
 
            else:
                wordNotIncluded+= 1
    print(wordNotIncluded + "words NOT found in the dictionary.")


# Call main() to begin program
main()