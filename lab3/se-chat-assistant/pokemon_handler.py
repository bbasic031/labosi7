from query_handler_base import QueryHandlerBase
import json
import requests

class PokemonHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "pokemon" in query:
            return True
        return False

    def process(self, query):
        try:
            result=self.call_api()
            id=result["id"]
            name=result["name"]
            for i in range (1,906):
                self.ui.say(f"Id: {id}\n Name: {name}")
        except:
            self.ui.say("Oh no! There was an error trying to contact Pokemon api.")
            self.ui.say("Try something else!")
        
    def call_api(self):        

        url = "https://pokemon-go1.p.rapidapi.com/pokemon_names.json"

        headers = {
	       "X-RapidAPI-Key": "019075f4b6msh29832d903d679cap1835a5jsnc8ddbf969c12",
	       "X-RapidAPI-Host": "pokemon-go1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        return json.loads(response.text)