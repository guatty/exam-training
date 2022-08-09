from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

# configuration
if "DEBUG" in os.environ:
    DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



root = "./data/trainings/"


REGISTERED_TRAININGS = json.load(open(root+"listing.json", 'r', encoding='utf-8'))
AVAILABLE_TRAININGS = [ {'name': e['name'], 'code': e['code']} for e in REGISTERED_TRAININGS.values()]


@app.route('/undefined/availableTrainings', methods=['GET', 'POST'])
@app.route('/availableTrainings', methods=['GET', 'POST'])
def availableTrainings():
    return jsonify(AVAILABLE_TRAININGS)

@app.route('/undefined/questionsForTraining', methods=['GET', 'POST'])
@app.route('/questionsForTraining', methods=['GET', 'POST'])
def questionsForTraining():
    data = request.get_json()
    code = data['training_code'] if 'training_code' in data else request.args.get('training_code')
    training_elts = json.load(open(root+REGISTERED_TRAININGS[code]['file_stem']+".json", 'r', encoding='utf-8'))
    

    if 'training_code' in data and data['training_code'] in REGISTERED_TRAININGS:
        return training_elts
    else:
        return jsonify({ 'message': 'Cet entraînement n\'existe pas' }), 401


if __name__ == '__main__':
    pass
