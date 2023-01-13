from query_handler_base import QueryHandlerBase
import random
import requests
import json

class LoveHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "love" in query:
            return True
        return False

    def process(self, query):
        names = query.split()
        fname = names[1]
        sname = names[2]

        try:
            result = self.call_api(fname, sname)
            score = result["percentage"]
            text = result["result"]
            self.ui.say(f"Love score between {fname} and {sname} is {score}%")
            self.ui.say(f"The doctor said: {text}")
        except: 
            self.ui.say("Oh no! There was an error trying to contact Love api.")
            self.ui.say("Try something else!")



    def call_api(self, fname, sname):
        import requests

        url = "https://love-calculator.p.rapidapi.com/getPercentage"

        querystring = {"sname":"Bakula","fname":"Bruno"}

        headers = {
	        "X-RapidAPI-Key": "019075f4b6msh29832d903d679cap1835a5jsnc8ddbf969c12",
	        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return json.loads(response.text)
