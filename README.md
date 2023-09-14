# BitLPasswordGenerator

## Model 1
An example of the result of the first function called <u>makePassword()</u> when printed to the console.

[['n', 'Z', 'O', '8'], ['N', '7', 'R', '0'], ['n', 'j', 'r', 'U'], ['J', 'k', 'n', 'P'], ['p', 's', 'q', 'J'], ['B', 'c', 'V', '8'], ['7', 'J', 'h', 'X'], ['U', 'N', 't', 'i']]

It is <u>1</u> list with <u>8</u> nested lists that contain <u>4</u> characters each as the above list is.

We do this because in <u>Model 2</u>, where the password is 48 characters long with hyphens separating each section of 4 characters, we need it to be in nested lists, otherwise it would be hard to sift through using <u>for loops</u>, whereas how I have it, its quite easy.

## Model 2
The function <u>formatAsString(listObject)</u> is used to format the nested lists into a password formatted like this:
<u>XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX</u>
where every 'X' in this example, would be a different character.

# Requirements

Refer to **<u>requirements.txt</u>**, which tells you what modules are required for the proper functionality. In this case, all you need it **<u>random</u>**, but I have also included **<u>pyautogui</u>** for your use. Note: within main.py, pyautogui is not accessed.

Note: use **<u>pip install pyautogui</u>** if you dont already have it installed.

# Conclusion

Do what you want/need with this, any help you need with anything related to pyautogui, I would suggest using youtube, stackoverflow, google, or chatgpt.