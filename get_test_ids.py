import json, socket, requests, os
from variables import my_ip, validator_url
#Sacar la ipo local de nuestro validador

def refresh_ids():
    fileName = "test-name-id.json"
    ets_url = validator_url + '/ExecutableTestSuites.json?fields=*' #Nombres de los ETS
    result_json = {}

    if os.path.exists(fileName):
        os.remove(fileName)
    #Comprobamos que la URL del ETS esté accesible
    ets_response = requests.get(ets_url)
    if ets_response :
        api_response = json.loads(ets_response.text)

        for ets_test_object in api_response["EtfItemCollection"]["executableTestSuites"]["ExecutableTestSuite"]:
            result_json[ets_test_object["label"]] = ets_test_object["id"]
        with open(fileName, 'w') as result_file:   
            json.dump(result_json, result_file)
        