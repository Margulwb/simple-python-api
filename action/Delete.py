from flask import jsonify
from action.Helper import openJsonFile, saveJsonFile

def deleteUserIdDataFromJson(index, jsonFile):
    existingData = openJsonFile(jsonFile, 'r') or []

    if 0 <= index < len(existingData):
        deleted_data = existingData[index]
        del existingData[index]
        saveJsonFile(jsonFile, existingData)
        return jsonify({ 'deleted_data': deleted_data })
    else:
        return jsonify({'error': 'Wrong index'}), 400

def deleteUserLoginDataFromJson(string, jsonFile):
    existingData = openJsonFile(jsonFile, 'r') or []
    index = next((i for i, item in enumerate(existingData) if item.get('login') == string), None)

    if index is not None:
        deleted_data = existingData.pop(index)
        saveJsonFile(jsonFile, existingData)
        return jsonify({'deleted_data': deleted_data}), 200
    else:
        return jsonify({'error': 'Wrong login'}), 400