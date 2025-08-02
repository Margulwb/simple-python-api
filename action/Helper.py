from flask import jsonify, request
import json
import os

def openJsonFile(jsonFile, mode):
    if os.path.exists(jsonFile):
        with open(jsonFile, mode, encoding='utf-8') as file:
            return json.load(file)
    else:
        return None
    
def loadJsonFile(filePath, mode='r'):
    try:
        with open(filePath, mode) as jsonFile:
            return json.load(jsonFile)
    except FileNotFoundError:
        return None

def saveJsonFile(jsonFile, data):
    if os.path.exists(jsonFile):
        with open(jsonFile, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    else:
        return None

def checkUserExist(usersJson, userId):
    users_data = openJsonFile(usersJson, 'r')
    for user in users_data:
        if user['id'] == userId:
            return user
    return None
