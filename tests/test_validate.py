import pytest
import sys
import os
sys.path.append("..")
from utils.get_file_list import get_file_list


def test_get_file_list_check_files_valid():
    os.chdir('tests')
    file_list = get_file_list()
    assert len(file_list) == 3
    assert 'file4.pdf' not in file_list
    assert 'file1.bin' in file_list
    assert 'file2.tar' in file_list
    assert 'file3.gz' in file_list