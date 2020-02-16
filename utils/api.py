import os
import sys
import requests
import urllib3

'''
Contains necessary functions to connect to a vManage server and upload files.
'''

class vmanage_session():

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
            response = self.session.post(url=self.login_url,
                                         data=self.login_credentials, verify=False)
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
        item_counter = 0

        for file in file_list:
            try:
                f = open('./Images/{0}'.format(file), 'rb')
            except FileNotFoundError:
                print("File Not Found. Check the filename and path.")

            #Get file size, convert to MB, increment item counter
            item_counter += 1
            size = int(os.stat('./Images/{0}'.format(file)).st_size / 1024)

            files = {'name':(f)}
            print("Now Uploading {0}. {1} KB ({2} of {3})".format(file, size,
                                                                  item_counter,
                                                                  number_of_items))
            try:
                response = self.session.post(url=self.upload_url, headers=self.headers, files=files)

                if response.status_code == 200:
                    print("{0} upload finished".format(file))
            except requests.exceptions.RequestException as e:
                print("An error has occurred while uploading {0}".format(file))
                print(e)
            f.close()
