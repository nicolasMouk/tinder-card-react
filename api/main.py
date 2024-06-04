from flask import Flask, jsonify
import requests
import random
from flask_cors import CORS
apiRoute = "https://randomuser.me/api/?results={}"
app = Flask(__name__)
CORS(app)

@app.route('/get_profile', methods=['GET'])
def get_profile():
    url = apiRoute.format(10)
    requete = requests.get(url)
    personne= requete.json()
    results = personne.get('results', [])
    peoples= get_attribut(results)
    return jsonify(peoples)


def get_attribut(results :jsonify)-> list :
    list_person=[]
    for personne in results :
        first_name=personne.get('name').get('first')
        last_name=personne.get('name').get('last')
        gender=personne.get('gender')
        age=personne.get('dob').get('age')
        country=personne.get('location').get('country')
        picture=personne.get('picture').get('large')
        descritpion = get_descriptions(gender)
        list_person.append({"name":first_name,"last_name":last_name,"gender":gender,"age":age,"country":country,"url":picture, "description": descritpion})
    return list_person

def get_descriptions(gender :str)-> str :
    descriptions_women = [
    "Incredibly modest Twitter enthusiast. Freelance craft beer aficionada. Social media maven. Lifelong connoisseur of fine spirits. TV expert.",
    "Dedicated professional gamer. Passionate about coffee culture. Adventurer. Approachable beer lover. Internet ninja.",
    "Tech geek. Foodie. Travel addict. Coffee connoisseur. Music enthusiast.",
    "Bookworm. Yoga practitioner. Nature lover. Coffee addict. Adventure seeker.",
    "Fitness fanatic. Animal lover. Coffee addict. Social media guru. Foodie.",
    "Music lover. Movie buff. Foodie. Social media addict. Coffee enthusiast."
    ]

    descriptions_men = [
        "Bacon ninja. Extreme TV lover. Twitter fanatic. Unapologetic explorer. Wannabe food specialist.",
        "Explorer. Evil thinker. Hardcore communicator. Music trailblazer. Food fan. Unapologetic student. Beer practitioner.",
        "Tech enthusiast. Adventure seeker. Music lover. Coffee addict. Foodie.",
        "Gamer. Movie buff. Beer aficionado. Tech geek. Adventure seeker.",
        "Fitness enthusiast. Sports fan. Beer lover. Tech geek. Movie buff.",
        "Entrepreneur. Tech geek. Sports enthusiast. Beer aficionado. Adventure seeker."
    ]
    if gender=='female' :
        return random.choice(descriptions_women)
    return random.choice(descriptions_men)


if __name__ == '__main__':
    app.run(debug=True)
