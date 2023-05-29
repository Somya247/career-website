from flask import Flask, render_template, jsonify,request,json  # Import necessary modules
from database import load_jobs_from_db,load_job_from_db,add_applicaton_to_db  # Import the database and helper function and other function
from sqlalchemy import text  # Import the text module from SQLAlchemy
from jinja2 import Template, Environment

app = Flask(__name__)  # Create a Flask application



@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()  # Call the 'load_jobs_from_db' function to retrieve the job listings
    return render_template("home.html", jobs=jobs)  # Render the 'home.html' template and pass the 'jobs' data



@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()  # Call the 'load_jobs_from_db' function to retrieve the job listings
    return jsonify(jobs)  # Return the job listings as JSON

@app.route("/api/job/<id>")
def show_job_json(id):
  job=load_job_from_db(id)
  return jsonify(job)


# for apply buttons 
@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found",404
  return render_template('jobdescription.html',job=job)



@app.route("/job/<id>/apply", methods=["POST"])
def apply_to_job(id):
    # print("Route /job/<id>/apply has been executed.")
    data = request.form # Save the data to the database or perform any other necessary actions

    job = load_job_from_db(id)
    # return jsonify(data)

    add_applicaton_to_db(id, data)
    return render_template("application_submitted.html", application=data, job=job) # Render the "Application Submitted" template and pass the application data


# add name = "(something)"  
# Verify that the form fields have a name attribute assigned. Without the name attribute, the form data won't be sent to the server.


# for jumping / anchor
# @app.route('/home')
# def home():
#     return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # Start the Flask application