<pre>This tool is used to upload the default image files to a customer vManage. By default these images are uploaded:
c1100-ucmk9.16.12.1e.SPA.bin
isr4200-ucmk9.16.12.1e.SPA.bin
isr4300-ucmk9.16.12.1e.SPA.bin
isr4400-ucmk9.16.12.1e.SPA.bin
isr4400v2-ucmk9.16.12.1e.SPA.bin
secapp-ucmk9.16.12.01e.1.0.8_SV2.9.13.0_XE16.12.aarch64.tar
secapp-ucmk9.16.12.01e.1.0.8_SV2.9.13.0_XE16.12.x86_64.tar
viptela-19.2.1-x86_64.tar.gz
vmanage-19.2.1-x86_64.tar.gz


Usage: vupload.py [OPTIONS]

Options:
  --host TEXT       vManage Host Name or IP  [required]
  --user TEXT       vManage Username  [required]
  --password TEXT   vManage Password  [required]
  --file_list TEXT  Files to Upload, separated by commas
  --help            Show this message and exit.

example for uploading default file list:

python3 vupload.py --host vmanage-name.viptela.net --user admin --password admin

example for uploading user defined file list:

python3 vupload.py --host vmanage-name.viptela.net --user admin --password admin --file_list a,b,c

Create a folder named "StandardFiles" in the same directory of this script and place the above mentioned items in there. If using a user defined list, still place the files in this folder.
</pre>
