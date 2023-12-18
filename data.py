import requests 

params = {
    "amount": 10,
    # "difficulty":"easy",
    "type":"boolean",
}

def get_quiz():
    response = requests.get(url='https://opentdb.com/api.php', params= params)

    question_data = response.json()["results"]

    return question_data
