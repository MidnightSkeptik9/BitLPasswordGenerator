import random
# not used but I will leave it for your use if you so choose

# define a list of characters that can appear within a bitlocker
# recovery password
characters = '0123456789'
characterList = list(characters)

# define a funtion to make a password as a list with specific formatting
# refer to Model 1 within README.md to see an example list
def makePassword(): # *** returns a list *** #
    password = ""
    for _ in range(0, 48):
        password += str(random.choice(characterList))
    return password

print(len(makePassword()))

# making a password:
# password = makePassword()

# formatting a password:
# formatAsString(password) # Note: password is the listObject

# the rest is up to you
# refer to README.md to find out how to use these functions further