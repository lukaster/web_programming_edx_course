from flask import Flask, render_template, request, session
from flask_session.__init__ import Session

app=Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

#pip3 install flask-session
#pip install werkzeug==0.16.0

@app.route("/")
def index():
    # return "hey there flask fella!"
    headline_text = "What is shakin' bacon?"
    i_am_sad = True
    name_list = ["Hans","Spooky","Ghost Boy"]
    return render_template("index.html",headline_text=headline_text, i_am_sad=i_am_sad, name_list=name_list)

@app.route("/bye")
def bye():
    # return "hey there flask fella!"
    headline_text = "So long and thanks for all the fish!"
    i_am_sad = False
    return render_template("more.html",headline_text=headline_text,i_am_sad=i_am_sad)

@app.route("/hello",methods=["GET","POST"])
def hello():
    name=request.form.get("name")
    if request.method=="POST":
        return render_template("hello.html",name=name)
    else:
       return "please go to submit the form"

#notes_list = []
@app.route("/notes",methods=["GET","POST"])
def notes():
    if session.get("notes_list") is None:
        session["notes_list"]=[] #my particular sess has empty list of notes
    if request.method=="POST":
        note = request.form.get("note")
        #notes_list.append(note)
        session["notes_list"].append(note)
    return render_template("notes.html", notes_list=session["notes_list"])

"""
@app.route("/<string:name>")
def greet(name):
    name = name.capitalize()
    return f"greetings, {name}!"
    
"""