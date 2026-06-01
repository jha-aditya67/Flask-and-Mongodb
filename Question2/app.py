from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://adityajha6758_db_user:7RluicnbfrQ577yo@cluster0.odi93hy.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["collegeDB"]
collection = db["students"]

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = {
            "name": request.form['name'],
            "email": request.form['email']
        }

        collection.insert_one(data)

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
