from flask import Flask, request, jsonify
from API.scripts.controllers.StatesOfTheWorldController import StatesOfTheWorldController as StatesController

app = Flask(__name__)


@app.route('/top-10-tari-populatie', methods=['GET'])
def get_to_10_states_by_population():
    return StatesController.get_to_10_states_by_population()


@app.route('/top-10-tari-densitate', methods=['GET'])
def get_to_10_states_by_density():
    return StatesController.get_to_10_states_by_density()


@app.route('/top-10-tari-suprafata', methods=['GET'])
def get_to_10_states_by_surface():
    return StatesController.get_to_10_states_by_surface()


@app.route('/toate-tarile', methods=['GET'])
def get_states_by_language():
    language = request.args.get('limba')
    if language:
        return StatesController.get_states_by_language(language)
    neighbour = request.args.get('vecin')
    if neighbour:
        return StatesController.get_states_by_neighbour(neighbour)
    time_zone = request.args.get('fus-orar')
    if time_zone:
        if " " in time_zone:
            time_zone_split = time_zone.split(" ")
            time_zone = time_zone_split[0] + "+" + time_zone_split[1]
        return StatesController.get_states_by_time_zone(time_zone)
    political_regime = request.args.get('regim-politic')
    if political_regime:
        return StatesController.get_states_by_political_regime(political_regime)


@app.route('/insert-all-data', methods=['POST'])
def insert_all_data():
    if StatesController.insert_all_data():
        return jsonify("All the data were inserted with success!")
    else:
        return jsonify("A problem has occurred!")


if __name__ == '__main__':
    app.run(port=8080)
