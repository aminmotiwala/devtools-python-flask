import string
import random
import json

characterList = ""
password = []

def setCharacterList():
    global characterList
    characterList += string.ascii_letters
    characterList += string.digits
    characterList += string.punctuation

def generatePassword():
    setCharacterList()
    password.clear()
    for i in range(12):
        # Picking a random character from our
        # character list
        randomchar = random.choice(characterList)

        # appending a random character to password
        password.append(randomchar)

    return ''.join(password)

def beautify(input_text):
    try:
        # Attempt to load the JSON data
        json_data = json.loads(input_text)

        # Beautify the JSON using indentation for better readability
        beautified_json = json.dumps(json_data, indent=2)

        return beautified_json, None

    except json.JSONDecodeError as e:
        errorMsg = 'Invalid JSON format: '
        errorMsg += e.msg
        if e.pos > 0 and e.pos < len(errorMsg):
            errorMsg += ' at '+e.pos
        return None, errorMsg