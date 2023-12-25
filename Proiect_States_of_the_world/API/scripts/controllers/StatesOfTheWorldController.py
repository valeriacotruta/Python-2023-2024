from API.scripts.services import StatesOfTheWorldService as StatesService
from flask import jsonify


class StatesOfTheWorldController:
    states_of_the_world_service = StatesService.StatesOfTheWorldService()

    @staticmethod
    def get_to_10_states_by_population():
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_to_10_states_by("population"))

    @staticmethod
    def get_to_10_states_by_density():
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_to_10_states_by("density"))

    @staticmethod
    def get_to_10_states_by_surface():
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_to_10_states_by("surface"))

    @staticmethod
    def get_states_by_language(language):
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_states_by("language", language))

    @staticmethod
    def get_states_by_neighbour(neighbour):
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_states_by("neighbour", neighbour))

    @staticmethod
    def get_states_by_time_zone(time_zone):
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_states_by("time_zone", time_zone))

    @staticmethod
    def get_states_by_political_regime(political_regime):
        return jsonify(
            StatesOfTheWorldController.states_of_the_world_service.get_states_by("political_regime", political_regime))

    @staticmethod
    def insert_all_data():
        StatesOfTheWorldController.states_of_the_world_service.create_records()
        return StatesOfTheWorldController.states_of_the_world_service.insert_all_data()
