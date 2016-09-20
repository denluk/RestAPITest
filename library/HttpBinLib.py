# -*- coding: utf-8 -*-
import requests
from RequestsLogging import write_log, write_stream_logs
from robot.api import logger

"""
Library for sending different type of requests.
"""

class HttpBinLib:
    service = 'http://httpbin.org'

    def __init__(self):
        self.service = 'http://httpbin.org'

    def set_service_name(self,service_name):
        """
            Установка имени сервиса с которым работают методы.\n\n

            *Args:*\n
            _service_name_ - имя сервиса на который будут отправляться запросы. \n

            *Examples*:\n
            | *Test cases*  | *Action*           | *Argument*
            |  Test Setup   |  Set service name  | http://httpbin.org
        """
        self.service = service_name

    def send_get_request(self, headers):
        """
            Получение http-ответа на get запрос с переданными хидерами.\n\n

            *Args:*\n
            _headers_ - словарь(dictionary) со всеми хидерами которые хотим передать в запросе\n\n

            *Examples*:\n
            | *Test cases*  | *Action*                           | *Argument*                    | *Argument*                   |
            | Simple Test   | set test variable                  | ${header_key}                 | key_name                     |
            |               | set test variable                  | ${header_value}               | key_value                    |
            |               | ${headers}=                        | Create dictionary             | ${header_key}=${header_value}|
            |               | ${response}=                       | Send get request              | ${headers}                   |
            """
        full_url = "{}/get".format(self.service)
        logger.info("url = {}, headers={}".format(full_url,headers))
        response=requests.get(url=full_url,headers=headers)
        write_log(response)
        return response

    def send_auth_request(self, url_login, entered_login, entered_password):
        """
                Получение http-ответа на auth запрос.\n\n

                *Args:*\n
                _url_login_ - имя пользователя и пароль которые передаются в url (строка в формате :usr/:password)\n\n
                _entered_login_ - вводимый пользователь\n\n
                _entered_password_ - вводимый пароль\n\n

        """
        full_url = "{url}/basic-auth/{url_login}".format(url=self.service,url_login=url_login)
        logger.info("url = {url} auth = {login}:{password}".format(url=full_url, login=entered_login, password=entered_password))
        response = requests.get(url=full_url, auth=(entered_login, entered_password))
        write_log(response)
        return response


    def send_stream_request(self, lines_number):
        """
                Получение http-ответа на stream запрос.\n\n

                *Args:*\n
                _lines_number_ - кол-во ожидаемых строк\n\n
        """
        full_url = "{url}/stream/{lines_number}".format(url=self.service,lines_number=lines_number)
        logger.info("url = {}".format(full_url))
        response = requests.get(url=full_url)
        write_stream_logs(response)
        return response
