from flask import Flask, render_template, jsonify
from jinja2 import Template, Environment

app = Flask(__name__)

# for jobs on page
JOBS = [
  {
  'id':1,
  'title':'Barista',
  'location':'Mumbai',
  'salary':'25,000'
  },
  {
  'id':2,
  'title':'Chef',
  'location':'Mumbai',
  'salary':'35,000'
  },
  {
  'id':3,
  'title':'Counter Server',
  'location':'Mumbai',
  'salary':'15,000'
  },
  {
  'id':4,
  'title':'Cleaner',
  'location':'Mumbai',
  'salary':'10,000'
  },
  {
  'id':5,
  'title':'Manager',
  'location':'Mumbai'
  }
]

# send this data to html by giving argument with render template 

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)

# jobs listings info in json endpoint
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
   app.run(host='0.0.0.0',debug=True)

