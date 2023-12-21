from bs4 import BeautifulSoup
import requests


class CrawlerService:
    def __init__(self):
        self.beautiful_soup = None

    def parse_information(self, web_url, class_name):
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
