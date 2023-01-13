from query_handler_base import QueryHandlerBase
import random
import json
import requests

class TriviaHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "trivia" in query:
            return True
        return False

    def process(self, query):
        full = query.split()
        category = full[1]
        limit = full[2]
        try:
            result=self.call_api(category,limit)
            for i in range (len(result)):
                self.ui.say(f"Question: {result[i]['question']}\n Answer: {result[i]['answer']}")
        except:
            self.ui.say("Oh no! There was an error trying to contact Trivia api.")
            self.ui.say("Try something else!")
        
    def call_api(self,category,limit):        

        url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"

        querystring = {"category":category,"limit":limit}

        headers = {
	        "X-RapidAPI-Key": "019075f4b6msh29832d903d679cap1835a5jsnc8ddbf969c12",
	        "X-RapidAPI-Host": "trivia-by-api-ninjas.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return json.loads(response.text)

