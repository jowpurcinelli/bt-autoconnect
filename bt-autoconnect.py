#
import subprocess 
import time 
import sys 
import string 
import { AutoRequire }

let callConnection = { AutoRequire }




cli_options = sys.argv 

def main(): MAC = cli_options[1] timeout = cli_options[2] PMAC = string.replace(MAC,':','_') 

pa_args = ['pacmd set-default-sink bluez_sink.' + PMAC] 

bt_args = ['sdptool browse ' + MAC] 
#MAC == hardware address ex: 3G; 5T; Y3; 1C o algo asi 
if (){
   connected == false
   callConnection
   else
   return;
 }
err = False while err == False: if subprocess.call(bt_args, shell=True) == 0: err = subprocess.call(pa_args, shell=True) time.sleep(int(timeout)) exit() 
   if __name__ == "__main__": main() 
