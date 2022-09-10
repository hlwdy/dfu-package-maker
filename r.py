#make the zip package from hex.
#By hlwdy.
import os
from shutil import copyfile

INPUT_FILE = "input.hex"
ZIP = ".zip"
HEX_SRC='./Debug'
 
def copy_build_file(srcDir):
    dst = os.path.dirname(os.path.abspath(__file__))
    copyfile(srcDir+"/"+INPUT_FILE, dst+"/"+INPUT_FILE)
 
def create_dfu_zip_file():
    os.system("nrfutil.exe pkg generate --hw-version 52 --sd-req 0xB6 --key-file private.pem --application-version 1 --application  " +
              INPUT_FILE+" DFU_pac"+ZIP)
 
copy_build_file(HEX_SRC)
create_dfu_zip_file()