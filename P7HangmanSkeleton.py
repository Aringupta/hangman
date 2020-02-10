from __future__ import print_function
''' Initialize global variables'''
word = ""
letter = ""
updatedSpaces = []
lives = 6

def intialize():
    '''Sets word and displays 
    updatedSpaces'''
    print("")
    

def getLetter():
    '''Gets letter from user'''
    global letter
    
def check():
    '''checks if letter in word, 
    if True updates undatedSpaces displays 
        updatedSpaces, calls won
    if False displays updatedSpaces, calls 
        getLetter
    '''
    global updatedSpaces
    global lives
    
def won():
    '''outputs a message if won or 
        calls getLetter if not'''
    print()

def main():
    '''Starts the program'''
    intialize()
    getLetter()
    check()

main()
    