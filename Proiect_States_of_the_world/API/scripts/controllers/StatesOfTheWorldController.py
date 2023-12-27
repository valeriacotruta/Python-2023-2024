from API.scripts.services import StatesOfTheWorldService as StatesService
from flask import jsonify


class StatesOfTheWorldController:
    """
        A class to represent a controller that handles client's requests, creates a bridge between the client and
        different components of the API (such as services or models), and returns a response back to the client.

        Attributes
        ----------
        states_of_the_world_service : StatesOfTheWorldService
           an instance of StatesOfTheWorldService class

        Methods
        -------
        get_to_10_states_by_population():
           A static method that returns the response of the states_of_the_world_service.get_to_10_states_by("population") function.
        get_to_10_states_by_density():
           A static method that returns the response of the states_of_the_world_service.get_to_10_states_by("density") function.
        get_to_10_states_by_surface():
           A static method that returns the response of the states_of_the_world_service.get_to_10_states_by("surface") function.
        get_states_by_language(language):
           A static method that returns the response of the states_of_the_world_service.get_states_by("language", language) function.
        get_states_by_neighbour(neighbour):
           A static method that returns the response of the states_of_the_world_service.get_states_by("neighbour", neighbour) function.
        get_states_by_time_zone(time_zone):
           A static method that returns the response of the states_of_the_world_service.get_states_by("time_zone", time_zone) function.
        get_states_by_political_regime(political_regime):
           A static method that returns the response of the states_of_the_world_service.get_states_by("political_regime", political_regime) function.
        insert_all_data():
            Returns True if all the data have been successfully inserted or an exception if they were not.
    """
    states_of_the_world_service = StatesService.StatesOfTheWorldService()

    @staticmethod
    def get_to_10_states_by_population():
        """
        A static method that returns the response of the states_of_the_world_service.get_to_10_states_by("population") function.

        :return: Response
        """
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_to_10_states_by("population"))

    @staticmethod
    def get_to_10_states_by_density():
        """
        A static method that returns the response of the states_of_the_world_service.get_to_10_states_by("density") function.

        :return: Response
        """
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_to_10_states_by("density"))

    @staticmethod
    def get_to_10_states_by_surface():
        """
        A static method that returns the response of the states_of_the_world_service.get_to_10_states_by("surface") function.

        :return: Response
        """
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_to_10_states_by("surface"))

    @staticmethod
    def get_states_by_language(language):
        """
        A static method that returns the response of the states_of_the_world_service.get_states_by("language", language) function.
        :param language: the language by which we filter the states
        :return: Response
        """
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_states_by("language", language))

    @staticmethod
    def get_states_by_neighbour(neighbour):
        """
        A static method that returns the response of the states_of_the_world_service.get_states_by("neighbour", neighbour) function.

        :param neighbour: the neighbour by which we filter the states

        :return: Response
        """
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_states_by("neighbour", neighbour))

    @staticmethod
    def get_states_by_time_zone(time_zone):
        """
        A static method that returns the response of the states_of_the_world_service.get_states_by("time_zone", time_zone) function.

        :param time_zone:the time zone by which we filter the states
        :return: Response
        """
        return jsonify(StatesOfTheWorldController.states_of_the_world_service.get_states_by("time_zone", time_zone))

    @staticmethod
    def get_states_by_political_regime(political_regime):
        """
        A static method that returns the response of the states_of_the_world_service.get_states_by("political_regime", political_regime) function.

        :param political_regime: the political regime by which we filter the states
        :return: Response
        """
        return jsonify(
            StatesOfTheWorldController.states_of_the_world_service.get_states_by("political_regime", political_regime))

    @staticmethod
    def insert_all_data():
        """
        Returns True if all the data have been successfully inserted or an exception if they were not.

        :return: Union[bool, Exception]
        """
        StatesOfTheWorldController.states_of_the_world_service.create_records()
        return StatesOfTheWorldController.states_of_the_world_service.insert_all_data()
