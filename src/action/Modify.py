from flask import jsonify, request
from action.Helper import openJsonFile, saveJsonFile

def modifyUserIdDataFromJson(id, usersJson):
    newData = request.json
    existing_data = openJsonFile(usersJson, 'r') or []
    user_found = False

    for item in existing_data:
        if item.get('id') == id:
            user_found = True

            if 'login' in newData and newData['login'] != item['login']:
                existing_logins = {u.get('login') for u in existing_data if u.get('id') != id}
                if newData['login'] in existing_logins:
                    return jsonify({'error': "Login already exists for another user"}), 400

            for key, value in newData.items():
                if key in item:
                    item[key] = value
                else:
                    return jsonify({'error': f'Field "{key}" does not exist in user data'}), 400


            saveJsonFile(usersJson, existing_data)
            return jsonify({'message': 'Data modified successfully'}), 200

    if not user_found:
        return jsonify({'error': 'User not found'}), 404