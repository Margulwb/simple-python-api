from flask import jsonify, request
from datetime import datetime
from action.Helper import openJsonFile, saveJsonFile, checkUserExist

def saveDataToJson(jsonFile, newData, existingData, customFeatures, postId=None):
    if existingData is None:
        existingData = []

    if customFeatures == "post":
        missingPostData = {
            "like": newData.get("like", 0),
            "unlike": newData.get("unlike", 0),
            "likeUsers": newData.get("likeUsers", []),
            "unlikeUsers": newData.get("unlikeUsers", []),
            "date": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            "comment": newData.get("comment", [])
        }
        newData.update(missingPostData)

    if 'id' not in newData:
        maxId = max((item.get('id', 0) for item in existingData), default=0)
        newData['id'] = maxId + 1

    newData = {key: (int(value) if key == 'id' else value) for key, value in newData.items()}
    existingData.append(newData)
    saveJsonFile(jsonFile, existingData)

    return jsonify({'message': 'Save data'}), 200

def giveLikeUnlike(jsonFile, usersJson, sign, userId, post, comment=None):
    existingData = openJsonFile(jsonFile, 'r') or []

    userExist = checkUserExist(usersJson, userId)
    if userExist is None:
        return jsonify({"error": f"User not found {userId}"}), 404

    target = None
    for item in existingData:
        if item['id'] == post:
            target = item
            break
    if not target:
        return jsonify({"error": "Post not found"}), 404

    if comment is not None:
        targetComments = target.get('comment', [])
        target = next((c for c in targetComments if c['id'] == comment), None)
        if not target:
            return jsonify({"error": "Comment not found"}), 404

    userLiked = f"{sign}Users"
    if userId in target.get(userLiked, []):
        target[userLiked].remove(userId)
        target[sign] -= 1 if sign in target else 0
    else:
        target[sign] = target.get(sign, 0) + 1
        target.setdefault(userLiked, []).append(userId)

    saveJsonFile(jsonFile, existingData)
    return jsonify({'message': f'{sign} added successfully'}), 200