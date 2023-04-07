import os
import platform
os_name=(platform.system())
if os_name=="Windows":
    os.system("pip install pandas")
    os.system("pip install colorama")
    os.system("pip install pyfiglet")

elif os_name=="Mac":
    os.system("pip install pandas")
    os.system("pip install colorama")
    os.system("pip install pyfiglet")
else:
    os.system("pip3 install pandas")
    os.system("pip3 install colorama")
    os.system("pip3 install pyfiglet")