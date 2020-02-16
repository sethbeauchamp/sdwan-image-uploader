#! /usr/bin/python3

import os
import sys
import requests
import click
import urllib3
from utils.get_file_list import get_file_list

class vmanageSession():

    def __init__(self, host, user, password, port, disable_warnings):

        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.base_url = 'https://{0}:{1}/dataservice'.format(self.host, self.port)
        self.session = requests.Session()
        self.disable_warnings = disable_warnings
        if self.disable_warnings:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def login(self):

        self.login_url = '{0}/j_security_check'.format(self.base_url)
        self.login_credentials = {'j_username':self.user, 'j_password':self.password}

        try:
            response = self.session.post(url=self.login_url, data=self.login_credentials, verify=False)
        except requests.exceptions.RequestException as e:
            print("Something went wrong:")
            print(e)
            sys.exit(1)

        if response.status_code != 200:
            print("Unable to connect to vManage. Check the host name/ip and credentials.")

        response = self.session.get(url='{0}/client/token'.format(self.base_url))

        if response.status_code == 200:
            self.token = response.text
            self.headers = {'X-XSRF-TOKEN': self.token}
        elif response.status_code == 404:
            self.headers = {}
        else:
            print("Unable to retreive token: {0}".format(response.status_code))

    def upload(self, file_list):
        self.upload_url = '{0}/device/action/software/package'.format(self.base_url)
        number_of_items = len(file_list)
        current_item = 0
        for file in file_list:
            try:
                f = open('./Images/{0}'.format(file), 'rb')
            except FileNotFoundError:
                print("File Not Found. Check the filename and path.")
            current_item += 1
            files = {'name':(os.path.basename(f.name), f)}
            size = int(os.stat('./Images/{0}'.format(file)).st_size / 1024)
            print("Now Uploading {0}. {1} KB ({2} of {3})".format(file, size, current_item, number_of_items))
            try:
                response = self.session.post(url=self.upload_url, headers=self.headers, files=files)

                if response.status_code == 200:
                    print("{0} upload finished".format(file))
            except requests.exceptions.RequestException as e:
                print("An error has occurred while uploading {0}".format(file))
                print(e)
            f.close()

@click.command()
@click.option('--host', help='vManage Host Name or IP', required=True)
@click.option('--port', help='vManage Host Port', default=8443, required=False)
@click.option('--disable_warnings', help='Disable Insecure Warnings', is_flag=True)
@click.option('--user', help='vManage Username', required=True)
@click.option('--password', help='vManage Password', hide_input=True, required=True)
@click.option('--file_list', help='Files to Upload, separated by commas', default=get_file_list(), required=False)
def main(host, user, password, file_list, port, disable_warnings):
    if type(file_list) is str:
        file_list = file_list.split(',')
    request = vmanageSession(host, user, password, port, disable_warnings)
    request.login()
    request.upload(file_list)


if __name__ == "__main__":
    main()
