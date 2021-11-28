#modules to install: flask, Flask-PyMongo, dnspython

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

#Connecting to MongoDB 
app.config['MONGO_DBNAME'] = 'test_api'
app.config["MONGO_URI"] = "mongodb+srv://<>" #Insert mongo URI here

mongo = PyMongo(app)

@app.route('/people', methods=['GET'])
def get_all_people():
    people = mongo.db.people

    output = []

    for query in people.find(): 
        output.append({'firstname' : query['firstname'], 'lastname' : query['lastname'], 'country' : query['country'], 'email' : query['email']})

    return jsonify({'result' : output})

@app.route('/people/<name>', methods=['GET'])
def get_one_person(name):
    people = mongo.db.people

    query = people.find_one({'firstname' : name})
    
    if query:
        output = {'firstname' : query['firstname'], 'lastname' : query['lastname'], 'country' : query['country'], 'email' : query['email']}
    else:
        output = 'No results found'

    return jsonify({'result' : output})

@app.route('/people', methods=['POST'])
def post_one_person():
    people = mongo.db.people
    
    #Get the information from the JSON objects
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    country = request.json['country']
    email = request.json['email']
    
    #MongoDB returns the id of the query inserted
    people_id = people.insert_one({'firstname' : firstname, 'lastname' : lastname, 'country' : country, 'email' : email})
    #query the database again to get the object inserted
    new_people = people.find_one({'_id' : people_id})

    output = {'firstname' : new_people['firstname'], 'lastname' : new_people['lastname'], 'country' : new_people['country'], 'email' : new_people['email']}

    return jsonify({'result' : output})

if __name__ == "__main__":
    app.run(debug=True)