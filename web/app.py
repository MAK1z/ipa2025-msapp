from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient
from bson import ObjectId

sample = Flask(__name__)

client = MongoClient("mongodb://mongoo:27017/")
mydb = client["ipa2025"]
mycol = mydb["routers"]

data = mycol.find()

@sample.route("/")
def main():
    return render_template("index.html", data=mycol.find())

@sample.route("/add", methods=["POST"])
def add_comment():
    ip = request.form.get("ip")
    username = request.form.get("username")
    password = request.form.get("password")

    if ip and username and password:
        mydict = { "ip": ip, "username": username, "password": password}
        x = mycol.insert_one(mydict)
    return redirect(url_for("main"))

@sample.route("/delete", methods=["POST"])
def delete_comment():
    try:
        idx = int(request.form.get("idx"))
        col = {'_id':data[idx]['_id']}
        res = mycol.delete_one(col)
    except Exception:
        pass
    return redirect(url_for("main"))

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)