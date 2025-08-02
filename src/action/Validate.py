from flask import jsonify, request
from action.Helper import openJsonFile
from action.Add import saveDataToJson

def checkValue(jsonFile, requiredFields, returnFields):
    value = request.json

    if all(field in value for field in requiredFields):
        credentials = {field: value[field] for field in requiredFields}
        value_info = checkValueExist(credentials, jsonFile, returnFields)
#jak nie ma takiego loginu to zwróć że nie ma usera
        if value_info:
            return jsonify({'value_info': value_info}), 200
        else:
            return jsonify({'error': 'Wrong data'}), 401
    else:
        return jsonify({'error': 'Wrong fields: login | password | role'}), 400

def checkValueExist(credentials, jsonFile, returnFields):
    data = openJsonFile(jsonFile, 'r')
    for user in data:
        if all(user.get(field) == credentials[field] for field in credentials):
            return {field: user.get(field) for field in returnFields}
    return False

def checkDataBeforeAdd(jsonFile, requiredFields, customFeatures, postId=None):
    newData = request.json
    if not all(field in newData for field in requiredFields):
        return jsonify({'error': "Wrong data, missing required fields"}), 400

    existingData = openJsonFile(jsonFile, 'r') or []

    if customFeatures == "login":
        error_response = loginCheckData(newData, existingData)
        if error_response:
            return error_response

    return saveDataToJson(jsonFile, newData, existingData, customFeatures, postId=None)

def loginCheckData(newData, existingData):
    if not isinstance(newData['login'], str) or not isinstance(newData['password'], str):
        return jsonify({'error': "Login and password must be strings"}), 400
    if len(newData['login']) < 3 or len(newData['password']) < 3:
        return jsonify({'error': "Login or password must be at least 3 characters long"}), 402
    if not isValidPassword(newData['password']):
        return jsonify({'error': "Password must contain at least one letter and one digit"}), 403

    existingLogins = set(item.get('login') for item in existingData)
    if newData['login'] in existingLogins:
        return jsonify({'error': "Login already exists"}), 401

    newData.setdefault('role', 'user')

    return None

def isValidPassword(password):
    return any(char.isdigit() for char in password) and any(char.isalpha() for char in password)