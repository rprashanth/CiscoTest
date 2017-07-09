from flask import Flask, request, jsonify, render_template
from flask_restful import reqparse, Resource, Api
import numpy as np
from config import SHUFFLING_ALGORITHM

app = Flask(__name__)
api = Api(app)
ListOfDeck = {} # dict to store all decks

parser = reqparse.RequestParser()
parser.add_argument('task')

class Deck():
    def __init__(self):
        # default deck gets created in this order
        self.newDeck = {'deck':['Ace', '1-Diamonds', '1-Hearts', '1-Spades',
                        '2-clubs', '2-Diamonds', '2-Hearts', '2-Spades',
                        '3-clubs', '3-Diamonds', '3-Hearts', '3-Spades',
                        '4-clubs', '4-Diamonds', '4-Hearts', '4-Spades',
                        '5-clubs', '5-Diamonds', '5-Hearts', '5-Spades',
                        '6-clubs', '6-Diamonds', '6-Hearts', '6-Spades',
                        '7-clubs', '7-Diamonds', '7-Hearts', '7-Spades',
                        '8-clubs', '8-Diamonds', '8-Hearts', '8-Spades',
                        '9-clubs', '9-Diamonds', '9-Hearts', '9-Spades',
                        '10-clubs', '10-Diamonds', '10-Hearts', '10-Spades',
                        'J-clubs', 'J-Diamonds', 'J-Hearts', 'J-Spades',
                        'Q-clubs', 'Q-Diamonds', 'Q-Hearts', 'Q-Spades',
                        'K-clubs', 'K-Diamonds', 'K-Hearts', 'K-Spades',
                            ]}
    def getNewDeck(self):
        return self.newDeck

class TodoList(Resource):
    # returns a list of available decks.
    def get(self):
        allDecks = ListOfDeck.keys()
        if len(allDecks)>0:
            return str(list(allDecks))
        return "No Decks to show"

    # to create a new Deck
    def post(self):
        newDeck = Deck()
        args = parser.parse_args()
        if args['task'] in ListOfDeck.keys():
            return str(args['task']) + ' already exists'

        ListOfDeck[args['task']] = newDeck.getNewDeck()['deck']
        return "New Deck "+str(args['task']) +  ' created', 201

class Service(Resource):
    def get(self, deckname,):
        try:
            return str(ListOfDeck[deckname])
        except:
            return str(deckname)+ " doesnot exist"

    def put(self, deckname):
        # print(ListOfDeck[deckname])
        try:
            SHUFFLING_ALGORITHM(ListOfDeck[deckname])
            return deckname + ' is shuffled '
        except:
            return deckname + ' does not exist to shuffle '

    def delete(self, deckname):
        if deckname in ListOfDeck.keys():
            del ListOfDeck[deckname]
            return str(deckname) + ' removed'

        return str(deckname) + ' doesnot exist'

api.add_resource(TodoList, '/deck')
api.add_resource(Service, '/deck/<deckname>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)