#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' #establishes possible list of usable characters in cipher
MAX_KEY_SIZE = len(SYMBOLS) #establish the maximum key value depending on the number of possible characters

def getMode(): #defining function getMode
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower() #gets input from user
        if mode in ['encrypt', 'e', 'decrypt', 'd']: #if the input is within this list:
            return mode #return the input
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".') #if input not in list, tell user possible inputs

def getMessage(): #define function getMessage
    message = input('Enter your message: ') #recieves input from user and returns it
    return message

def getKey(): #define function getKey
    key = 0 #sets variable key to 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE)) #tell the user to put in a key within the possible values
        key = int(input()) #get input from user to determine key
        if (key >= 1 and key <= MAX_KEY_SIZE): #if the input is within these parameters:
            return key #return the value

def getTranslatedMessage(mode, message, key):#define function getTranslatedMessage
    if mode[0] == 'd': #if the inputted mode is d:
        key = -key #negates the key value
    translated = ''#set translated to the new message

    for symbol in message: #for each character in the message
        symbolIndex = SYMBOLS.find(symbol) #find the index number for each character
        if symbolIndex == -1: #if the symbol is not in the list
            translated += symbol #don't change the character
        else:
            symbolIndex += key #set the index equal to the key + 1
        if symbolIndex >= len(SYMBOLS): #if the index value of the character is longer than the number of possible characters:
            symbolIndex -= len(SYMBOLS)#subtract the length of the list from the given value
        elif symbolIndex < 0: #if the index value of the character is less than 0
            symbolIndex += len(SYMBOLS) #add the length of the list to the index

        translated += SYMBOLS[symbolIndex] #apply the key to the character
    return translated #save the translated message

mode = getMode() #call getMode
message = getMessage() #call getMessage
key = getKey() #call getKey
print('Your translated text is: ') #print header
print(getTranslatedMessage(mode, message, key)) #print translated message according to variables