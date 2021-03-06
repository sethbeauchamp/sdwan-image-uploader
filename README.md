[![Build Status](https://travis-ci.org/sethbeauchamp/sdwan-image-uploader.svg?branch=master)](https://travis-ci.org/sethbeauchamp/sdwan-image-uploader)
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/sethbeauchamp/sdwan-image-uploader)

# Cisco SDWAN Image Uploader

This tool allows you to upload one or more image files to a vManage server.
Upload IOS XE, vManage, and vEdge image files to vManage.

## Setup

Clone to repository to your local machine. Use a virtual environment if desired.
```
git clone https://github.com/sethbeauchamp/sdwan-image-uploader.git
cd sdwan-image-uploader
pip3 install -r requirements.txt
mkdir Images
```

Move any image files you wish to upload into the the Images folder within the sdwan-image-uploader folder.

## Usage
```
Options:
  --host TEXT         vManage Host Name or IP  [required]
  --port INTEGER      vManage Host Port
  --disable_warnings  Disable Insecure Warnings
  --user TEXT         vManage Username  [required]
  --password TEXT     vManage Password  [required]
  --file_list TEXT    Files to Upload, separated by commas
  --help              Show this message and exit.
```
**Upload all files in the Images folder:**

```
python3 vupload.py --host vmanage-name.viptela.net --user admin --password admin
```

**Upload a specific file or list of files in the Images Foler:**

```
python3 vupload.py --host vmanage-name.viptela.net --user admin --password admin --file_list file1.bin,file2.gz,file3.tar
```

**Example of a full run:**

![full-run-example](img/ex.png)