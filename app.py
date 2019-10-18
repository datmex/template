from flask import Flask, render_template,request,redirect,url_for # For flask implementation  
from bson import ObjectId # For ObjectId to work  
from pymongo import MongoClient  
from bson.json_util import dumps
import os  
  
app = Flask(__name__)  
title = "TODO sample application with Flask and MongoDB"  
heading = "TODO Reminder with Flask and MongoDB"  
  
client = MongoClient("mongodb://inegi:rsF7vS5QFZmUCLTHNo7sEYTN3lOxVkHJSH6Vf3xlSGbj8hXzM3hGxZHNxTe9Fny296ya4BgjnSetDZyrj4b8yA==@inegi.documents.azure.com:10255/?ssl=true&replicaSet=globaldb") #host uri  
db = client.inegi    #Select the database  
todos = db.scian #Select the collection name  
  
def redirect_url():  
    return request.args.get('next')# or \  
           #request.referrer or \  
           #url_for('index')  
 
@app.route("/list")  
def lists ():  
    #Display the all Tasks  
    todos_l = todos.find()  
    a1="active"  
    return render_template('index.html',a1=a1,todos=todos_l,t=title,h=heading)  
 
@app.route("/")  
def tasks ():  
    #Display the Uncompleted Tasks  
    todos_l = todos.find_one()  
    print(todos_l)
    a2="active"  
    return render_template('index.html',a2=a2,todos=todos_l,t=title,h=heading)  
 
 
@app.route("/completed")  
def completed ():  
    #Display the Completed Tasks  
    todos_l = todos.find({"done":"yes"})  
    a3="active"  
    return render_template('index.html',a3=a3,todos=todos_l,t=title,h=heading)  
 
@app.route("/done")  
def done ():  
    #Done-or-not ICON  
    id=request.values.get("_id")  
    task=todos.find({"_id":ObjectId(id)})  
    if(task[0]["done"]=="yes"):  
        todos.update({"_id":ObjectId(id)}, {"$set": {"done":"no"}})  
    else:  
        todos.update({"_id":ObjectId(id)}, {"$set": {"done":"yes"}})  
    redir=redirect_url()      
  
    return redirect(redir)  
 
@app.route("/action", methods=['POST'])  
def action ():  
    #Adding a Task  
    name=request.values.get("name")  
    desc=request.values.get("desc")  
    date=request.values.get("date")  
    pr=request.values.get("pr")  
    todos.insert({ "name":name, "desc":desc, "date":date, "pr":pr, "done":"no"})  
    return redirect("/list")  
 
@app.route("/remove")  
def remove ():  
    #Deleting a Task with various references  
    key=request.values.get("_id")  
    todos.remove({"_id":ObjectId(key)})  
    return redirect("/")  
 
@app.route("/update")  
def update ():  
    id=request.values.get("_id")  
    task=todos.find({"_id":ObjectId(id)})  
    return render_template('update.html',tasks=task,h=heading,t=title)  
 
@app.route("/action3", methods=['POST'])  
def action3 ():  
    #Updating a Task with various references  
    name=request.values.get("name")  
    desc=request.values.get("desc")  
    date=request.values.get("date")  
    pr=request.values.get("pr")  
    id=request.values.get("_id")  
    todos.update({"_id":ObjectId(id)}, {'$set':{ "name":name, "desc":desc, "date":date, "pr":pr }})  
    return redirect("/")  

  
if __name__ == "__main__":  
  app.run()