from flask import Flask, url_for, request, render_template
from markupsafe import escape
import json
import datetime
import random

app = Flask(__name__)


# function to add to JSON 
def write_json(data, filename='posts2.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      

@app.route('/')
@app.route('/home')
def home():
    # Opening JSON file 
    with open('posts2.json', 'r') as openfile: 
        # Reading from json file 
        posts = json.load(openfile) 
    print(posts)
    return render_template('home.html', posts=posts)

@app.route('/add_post', methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        req = request.form
        date_now = datetime.datetime.now()
        with open('posts2.json') as json_file: 
            data = json.load(json_file) 
            temp = data 
  
            # python object to be appended 
            y = {
                "id": random.randint(1, 9),
                "title": request.form.get("title"),
                "contents": request.form.get("contents"),
                "owner": request.form.get("owner"),
                "created_at": date_now.strftime("%Y, %B, %A"),
                "modified_at":  date_now.strftime("%Y, %B, %A")
            }
  
            # appending data to emp_details  
            temp.append(y) 
      
        write_json(data)  
    return render_template('post.html')

#with open('posts2.json', 'w') as outfile:
 #   json.dump(data, outfile)

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run(debug=True)
