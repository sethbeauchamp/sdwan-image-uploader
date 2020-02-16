#! /usr/bin/python3

import click
from utils.get_file_list import get_file_list
from utils.api import vmanage_session


@click.command()
@click.option('--host', help='vManage Host Name or IP', required=True)
@click.option('--port', help='vManage Host Port', default=8443, required=False)
@click.option('--disable_warnings', help='Disable Insecure Warnings', is_flag=True)
@click.option('--user', help='vManage Username', required=True)
@click.option('--password', help='vManage Password', hide_input=True, required=True)
@click.option('--file_list', help='Files to Upload, separated by commas',
              default=get_file_list(), required=False)
def main(host, user, password, file_list, port, disable_warnings):
    '''
    Check if file_list came from user input and convert it to a list.
    Set up connection to vManage then begin uploading files
    '''
    if isinstance(file_list, str):
        file_list = file_list.split(',')
    request = vmanage_session(host, user, password, port, disable_warnings)
    request.login()
    request.upload(file_list)


if __name__ == "__main__":
    main()
