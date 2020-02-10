''' Initialize global variables'''
secret = ""
letter = ""
updatedWord = []

def intialize():
    '''Sets secret and displays 
    updatedWord'''
    print("")
    

def getLetter():
    '''Gets letter from user'''
    global letter
    
def test():
    '''tests if letter in secret, 
    if True updates undatedWord displays 
        updatedWord, calls ifWon
    if False displays updatedWord, calls 
        getLetter
    '''
    global updatedWord
    
def ifWon():
    '''outputs a message if won or 
        calls getLetter if not'''
    print()

def main():
    '''Starts the program'''
    intialize()
    getLetter()
    test()

main()
    
    