import sqlalchemy
import os


from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']


engine = create_engine(db_connection_string, 
                      connect_args={
                        "ssl":{
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })


# helper function 
def load_jobs_from_db():
    with engine.connect() as conn:  # Connect to the database using the engine
        result = conn.execute(text("select * from jobs"))  # Execute SQL query to select all rows from the 'jobs' table
        jobs = []
        for row in result.all():  # Iterate over the result rows
            jobs.append(dict(row._asdict()))  # Convert each row to a dictionary and append to the 'jobs' list
        return jobs  # Return the list of job dictionaries



# for apply button
def load_job_from_db(id):
    with engine.connect() as conn:
       
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id={id}")) # Execute the SQL query with the provided ID
        
        
        rows = [] # Create an empty list to store the rows
        
        
        column_names = result.keys() # Get the column names from the result set
        
       
        for row in result.all():  # Iterate over each row in the result set
            
            row_dict = dict(zip(column_names, row)) # Convert the row into a dictionary by pairing column names with row values
            
            
            rows.append(row_dict) # Add the row dictionary to the list of rows
        
        
        if len(rows) == 0: # Check if the list of rows is empty
            
            return None # Return None if no rows are found
        else:
            
            return rows[0] # Return the first row (dictionary) if it exists


# for application form data
def add_applicaton_to_db(job_id,data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id,name,email,linkedin_url,resume) VALUES (:job_id, :name, :email, :linkedin_url, :resume)")
    values={'job_id': job_id,
            'name':data['name'],
            'email':data['email'],
            'linkedin_url':data['linkedin_url'],
            'resume':data['resume']
            }
    conn.execute(query,values)
    