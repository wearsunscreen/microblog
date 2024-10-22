This is a template Flask app with MongoDB.

## Dependencies

Commands to prepare environment

```
python3 -m venv venv/
source venv/bin/activate
pip install flask
export FLASK_APP=app.py
export FLASK_DEBUG=1
pip install pymongo[srv]

flask run
````

## Mongo DB

`mongodb+srv://wearsunscreen:<password>@cluster0.ivgo2.mongodb.net/`
