import random
import pyautogui # not used but I will leave it for your use if you so choose

# define a list of characters that can appear within a bitlocker
# recovery password
characters = '0123456789'
characterList = list(characters)

# define a funtion to make a password as a list with specific formatting
# refer to Model 1 within README.md to see an example list
def makePassword(): # *** returns a list *** #
    password = []
    for _ in range(0, 12):
        nestedList = []
        for _ in range(0, 4):
            char = random.choice(characterList)
            nestedList.append(char)
        password.append(nestedList)
    return password

# define a function to loop through the list created in the function
# above that formats it as Model 2 in README.md is formatted
def formatAsString(listObject): # *** returns a string *** #
    passwordString = ''
    for x in range(0, 8):
        for y in range(0, 4):
            char = listObject[x][y]
            passwordString += str(char)
    # this creates an invalid password with a hyphen at the end
    # so we use removesuffix() to get rid of 
    return passwordString

# making a password:
# password = makePassword()

# formatting a password:
# formatAsString(password) # Note: password is the listObject

# the rest is up to you
# refer to README.md to find out how to use these functions further