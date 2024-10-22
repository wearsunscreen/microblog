import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://wearsunscreen:Brillig55@cluster0.ivgo2.mongodb.net/")
app.db = client.microblog

entries = []

@app.route('/', methods=['GET', 'POST'])
def home():
    print([e for e in app.db.entries.find({})])

    if request.method == 'POST':
        entry_content = request.form.get('content')
        formatted_date = datetime.datetime.today().strftime('%Y-%m-%d')
        entries.append((entry_content, formatted_date))

    return render_template('home.html', entries=entries)
