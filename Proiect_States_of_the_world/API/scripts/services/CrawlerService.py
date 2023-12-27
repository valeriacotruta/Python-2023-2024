from bs4 import BeautifulSoup
import requests


class CrawlerService:
    """
      A class used to manage the crawler operations like parsing of the states' details from the websites into tables,
      based on some HTML tags.

      Attributes
      ----------
      beautiful_soup : BeautifulSoup
          an instance of the BeautifulSoup library

      Methods
      -------
      parse_information(self, web_url, class_name):
        Parses the information from a web url, inside an HTML class.
      parse_states_by_capitals(self, web_url, class_name):
        Parses the states with their capitals from a specific web url, inside an HTML class.
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the CrawlerService object.
        """
        self.beautiful_soup = None

    def parse_information(self, web_url, class_name):
        """
        Parses the information from a web url, inside an HTML class and creates a list based on the information processed.

        :param web_url: a web url we make a request to and get its text
        :param class_name: the name of the class that has all the information that will processed

        :return:list
        """
        content = requests.get(web_url).text
        self.beautiful_soup = BeautifulSoup(content, "html.parser")
        table_information = self.beautiful_soup.find('table', {'class': class_name})
        table_body = table_information.find('tbody')
        table_rows = table_body.find_all('tr')
        table_data = list(map(
            lambda row: list(map(lambda element: element.text.strip(), row.find_all('td'))),
            table_rows
        ))
        table_data = [row for row in table_data if row != []]
        return table_data

    def parse_states_by_capitals(self, web_url, class_name):
        """
        Parses the information from a web url, inside an HTML class and creates a list based on the information processed
        about the states and their capitals.

        :param web_url: a web url we make a request to and get its text
        :param class_name: the name of the class that has all the information that will processed
        :return: list
        """
        content = requests.get(web_url).text
        self.beautiful_soup = BeautifulSoup(content, "html.parser")
        table_information = self.beautiful_soup.find('table', {'class': class_name})
        table_body = table_information.find('tbody')
        table_rows = table_body.find_all('tr')
        table_data = list(map(
            lambda row: list(map(lambda element: element.text.strip(), row.find_all('th') + row.find_all('td'))),
            table_rows
        ))
        table_data = [row for row in table_data if row != table_data[0]]
        return table_data
