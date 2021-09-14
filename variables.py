import socket
import os
def _get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

my_ip = _get_ip_address()
validator_url = 'https://inspire.ec.europa.eu/validator/v2'.format(my_ip)#IP del validador
# test_object = 'https://ogc-api.nrw.de/'.format(my_ip) 
test_object = 'https://api-ver.lantmateriet.se/byggnad/atom/v1.1/inspire/bu'.format(my_ip) 
# test_object = 'https://www.ordnancesurvey.co.uk/xml/products/AddressBase.xml'.format(my_ip) 
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' #PATH de chrome para abrir el report
validator_name = "validator-v2021.0"
ets_ids = ["EID11571c92-3940-4f42-a6cd-5e2b1c6f4d93"]





    
    
