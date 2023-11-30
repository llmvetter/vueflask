from flask import Flask, jsonify
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

Patients = [
    {
        'full_name': 'Jonas P',
        'status': 'inactive',
        'more_info': 'tbd'
    },
    {
        'full_name': 'Jonas P',
        'status': 'inactive',
        'more_info': 'tbd'
    },
    {
       'full_name': 'Jonas P',
        'status': 'inactive',
        'more_info': 'tbd'
    }
]


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/strokecockpit', methods=['GET'])
def ping_pong():
    return jsonify('This is the Strokecockpit Landing page')

@app.route('/patients', methods=['GET'])
def all_patients():
    return jsonify({
        'status': 'success',
        'patients': Patients
    })

if __name__ == '__main__':
    app.run()