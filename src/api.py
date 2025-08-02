from flask import Flask, Response
from action.Add import giveLikeUnlike
from action.Delete import deleteUserIdDataFromJson, deleteUserLoginDataFromJson
from action.Validate import checkValue, checkDataBeforeAdd
from action.Modify import modifyUserIdDataFromJson
from action.Helper import openJsonFile
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app) #, resources={r"/*": {"origins": "http://10.0.1.139:3000"}}
#develop

# USER
usersJson = 'storage/users.json'
userFields = ['login', 'password']
returnUserFields = ['login','password','role','id']

@app.route("/users", methods=['GET'])
def showUsers():
    return Response(json.dumps(openJsonFile(usersJson, 'r'), ensure_ascii=False), status=200, mimetype='application/json')

@app.route('/users/add', methods=['POST'])
def addUsers():
    return checkDataBeforeAdd(usersJson, userFields, "login")

@app.route('/users/login', methods=['POST'])
def checkUser():
    return checkValue(usersJson, userFields, returnUserFields)

@app.route('/users/<int:index>', methods=['DELETE'])
def deleteIdUsers(index):
    return deleteUserIdDataFromJson(index, usersJson)

@app.route('/users/<string:login>', methods=['DELETE'])
def deleteLoginUsers(login):
    return deleteUserLoginDataFromJson(login, usersJson)

@app.route('/users/modify/<int:id>', methods=['POST'])
def modifyIdUsers(id):
    return modifyUserIdDataFromJson(id, usersJson)

# ARTICLE
articlesJson = 'storage/article.json'
articlesFields = ['title','subTitle','content']

@app.route("/articles", methods=['GET'])
def showArticles():
    return Response(json.dumps(openJsonFile(articlesJson, 'r'), ensure_ascii=False), status=200, mimetype='application/json')

@app.route('/articles/add', methods=['POST'])
def addNewArticles():
    return checkDataBeforeAdd(articlesJson, articlesFields, "post")

# FORUM
forumJson = 'storage/forum.json'
postFields = ['userId', 'title', 'content']

@app.route("/forum", methods=['GET'])
def showForum():
    return Response(json.dumps(openJsonFile(forumJson, 'r'), ensure_ascii=False), status=200, mimetype='application/json')

@app.route('/forum/like/<int:post>/<int:userId>', methods=['POST'])
def addPostLike(post, userId):
    return giveLikeUnlike(forumJson, usersJson, "like", userId, post)

@app.route('/forum/unlike/<int:post>/<int:userId>', methods=['POST'])
def addPostUnlike(post, userId):
    return giveLikeUnlike(forumJson, usersJson, "unlike", userId, post )

@app.route('/forum/like/<int:post>/<int:comment>/<int:userId>', methods=['POST'])
def addCommentLike(post, comment, userId):
    return giveLikeUnlike(forumJson, usersJson, "like", userId, post, comment)

@app.route('/forum/unlike/<int:post>/<int:comment>/<int:userId>', methods=['POST'])
def addCommentUnlike(post, comment, userId):
    return giveLikeUnlike(forumJson, usersJson, "unlike", userId, post, comment)

@app.route('/forum/addPost', methods=['POST'])
def addPost():
    return checkDataBeforeAdd(forumJson, postFields, "post")

# @app.route('/forum/addCommentPost/<int:postId>', methods=['POST'])
# def addComment(postId):
#     return checkDataBeforeAdd(forumJson, postFields, "comment", postId)

#TODO dodawanie nowych komentarzy w postach
#TODO modyfikowanie postów / komentarzy (może przy modyfikacji że user który stworzył i user z odpowiednią rolą(admin) może)
#TODO usuwanie (też per role i user który dodał)
#TODO pokazywanie kto dał like

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

