
"""
Created on Sun Mar 28 16:43:39 2021

@author: User
"""

from flask import Flask,render_template,request,redirect
from werkzeug.utils import secure_filename
import csv
app = Flask(__name__)
app.config['MAX_CONTENT_PATH']=16 * 1024  #bytes
app.config['UPLOAD_FOLDER']='./upload'


@app.route('/')
def home_page():
    return render_template("index.html")



def write_to_csvfile(data):
    email=data["email"]
    subject=data["subject"]
    message=data["message"]
    with open('database.csv', mode='a',newline='') as db_file:
    
        employee_writer = csv.writer(db_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)  
        employee_writer.writerow([email, subject, message])

def read_from_csvfile(fname='database.csv'):
    content=""
    with open('database.csv', mode='r',newline='') as db_file:
        csv_reader = csv.reader(db_file, delimiter=',')
        for i, line in enumerate(csv_reader):   
            line="{}\t\t\t{}\t\t\t{}\n".format(*line)  

            content+=line
    return content
    

    
@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_csvfile(data)
            #return "thanks"   
            return redirect("thankyou.html")
        except:
            return redirect("somethingwrong.html")
    else:
        return redirect("somethingwrong.html")


  
@app.route('/messages.html')
def show_messages():
    content = read_from_csvfile()
    return render_template("messages.html", text=content)    



	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      passwd=request.form["password"]
      file = request.files['file']
      filename = secure_filename(file.filename)
      if passwd=="esii00esii00" and filename:
          file.save(app.config['UPLOAD_FOLDER']+ "/"+filename)
          return redirect("uploadsuccessfull.html")
      else:
          return redirect("uploadsuccessfull.html")



@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)  