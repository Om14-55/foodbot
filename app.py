# from flask import Flask,render_template,jsonify,request
# from dotenv import load_dotenv
# import os
# from foodbot.retrival_generation import generation
# from foodbot.ingest import ingestdata

# app=Flask(__name__)
# load_dotenv()

# vstore=ingestdata("done")
# chain=generation(vstore)

# @app.route("/")
# def index():
#   return render_template('chain.html')
# @app.route("/get",methods=["GET","POST"])
# def chat():
#   msg=request.form["msg"]
#   input=msg
#   result=chain.invoke(input)
#   print("Response:",result)
#   return str(result)

# if __name__=='__main__':
#   app.run(debug=True)
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
import re
from foodbot.retrival_generation import generation
from foodbot.ingest import ingestdata

app = Flask(__name__)
load_dotenv()

vstore = ingestdata("done")  # ✅ only this
chain = generation(vstore)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    results = chain.invoke(input)
    result = re.sub(r"[*#`_>]+", "", results)  # removes **, ##, ###, etc.
    result = result.strip()
    print("Response:", result)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
