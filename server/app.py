from flask import Flask, jsonify, request
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

@app.route('/patients', methods=['GET', 'POST'])
def all_patients():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        Patients.append({
            'full_name': post_data.get('full_name'),
            'status': post_data.get('status'),
            'more_info': post_data.get('more_info')
        })
        response_object['message'] = 'Patient added!'
    else: 
        response_object['patients'] = Patients
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()


