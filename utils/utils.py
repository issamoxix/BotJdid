import json
def get_token():
    with open('secrets.json','r') as file:
        try:
            TOKEN = json.loads(file.read())["TOKEN"]
            return TOKEN
        except:
            raise Exception("TOKEN doesn't exists on the secrets.json file !")