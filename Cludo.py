#set up some constants
MISS_SCARLETT = "Miss Scarlett"
REVEREND_GREEN = "Reverend Green"
COLONEL_MUSTARD = "Colonel Mustard"
PROFESSOR_PLUM = "Professor Plum"
MRS_WHITE = "Mrs. White"
MRS_PEACOCK = "Mrs. Peacock"

CANDLESTICK = "Candlestick"
DAGGER = "Dagger"
LEAD_PIPE = "Lead Pipe"
REVOLVER = "Revolver"
ROPE = "Rope"
SPANNER = "Spanner"

HALL = "Hall"
LOUNGE = "Lounge"
DINING_ROOM = "Dining Room"
KITCHEN = "Kitchen"
BALLROOM = "Ballroom"
CONSERVATORY = "Conservatory"
BILLIARD_ROOM = "Billiard Room"
LIBRARY = "Library"
STUDY = "Study"

#create sets that have all the different things in cluedo
people = {MISS_SCARLETT, REVEREND_GREEN, COLONEL_MUSTARD, PROFESSOR_PLUM, MRS_WHITE, MRS_PEACOCK}
weapons = {CANDLESTICK, DAGGER, LEAD_PIPE, REVOLVER, ROPE, SPANNER}
rooms = {KITCHEN, BALLROOM, CONSERVATORY, BILLIARD_ROOM, LIBRARY, STUDY, HALL, LOUNGE, DINING_ROOM}

#define sets for things that definately haven't commited the crime
knownPeople = set()
knownWeapons = set()
knownRooms = set()

#say how many players there will be in your cluedo game
total_number_of_players = 4

#make new sets for anyone that could possibly have commited the crime by looking at the people that definately haven't done it
def suspected_people(people, knownPeople):
    return people - knownPeople
def suspected_weapons(weapons, knownWeapons):
    return weapons - knownWeapons
def suspected_rooms(rooms, knownRooms):
    return rooms - knownRooms

#define how a round class should be created, it will be used to efficiently store all the data needed in the cluedo game
class Round:
    def __init__(self,asker,helper,person,weapon,room,card) :
        self.asker = asker
        self.helper = helper
        self.person = person
        self.weapon = weapon
        self.room = room
        self.card = card
    
#define how a player class should be created, it will be used to efficiently store all of the data that is needed for a player
class Player:
    def __init__(self, ownedCards, notOwnedCards) :
        self.ownedCards = ownedCards
        self.notOwnedCards = notOwnedCards

#test data for the program to use, you can change this to any cluedo game and it should work
def round_generator():
    rounds = []
    rounds.append(Round(0,1,MISS_SCARLETT,SPANNER,DINING_ROOM,SPANNER))
    rounds.append(Round(1,3,MISS_SCARLETT,CANDLESTICK,STUDY,None))
    rounds.append(Round(2,3,PROFESSOR_PLUM,LEAD_PIPE,LIBRARY,None))
    rounds.append(Round(3,0,MISS_SCARLETT,CANDLESTICK,LIBRARY,None))
    rounds.append(Round(0,1,MISS_SCARLETT,CANDLESTICK,DINING_ROOM,DINING_ROOM))
    rounds.append(Round(1,0,MISS_SCARLETT,LEAD_PIPE,STUDY,None))
    rounds.append(Round(2,3,COLONEL_MUSTARD,REVOLVER,LIBRARY,None))
    rounds.append(Round(3,0,REVEREND_GREEN,LEAD_PIPE,LOUNGE,None))
    rounds.append(Round(0,1,MISS_SCARLETT,REVOLVER,BALLROOM,MISS_SCARLETT))
    return rounds

#create efficient profiles for the up to 6 possible players that could be participating in a cluedo game
def player_generator(total_number_of_players):
    players = []
    for i in range(total_number_of_players):
        players.append(Player(set(), set()))
    return players

#takes the cards we know a helper doesn't have, and the cards that were asked about, and if it can it will work out which one of the cards was shown
def sherlock(cards_helper_doesnt_have, cards_helper_asked_about):
    deduction = cards_helper_asked_about - cards_helper_doesnt_have
    if 1 == len(deduction):
        answer = deduction.pop()
        return answer

#returns the players that are unable to help with any certain round
def players_that_couldnt_help(total_number_of_players, asker, helper):
    playersThatCantHelp = []
    x = asker
    while x + 1 != helper and x < total_number_of_players - 1:  
        x += 1
        playersThatCantHelp.append(x)
        if x >= total_number_of_players - 1:
            x = -1
    return playersThatCantHelp

#return an updated set of players including the cards they definately don't have, by looking at which players couldn't help in all the rounds
def cards_players_dont_have(players, rounds):
    for round in rounds:
        playersThatCantHelp = players_that_couldnt_help(total_number_of_players, round.asker, round.helper)
        for number in playersThatCantHelp:
            players[number].notOwnedCards.add(round.person)
            players[number].notOwnedCards.add(round.weapon)
            players[number].notOwnedCards.add(round.room)
    return players

#returns an updated set of knowledge, given a card that we now know
def update_knowledge(card, knownPeople, knownWeapons, knownRooms):
    if (card) in people:
        knownPeople.add(card)
    if (card) in weapons:
        knownWeapons.add(card)
    if (card) in rooms:
        knownRooms.add(card)
    return knownPeople, knownWeapons, knownRooms

#update knowledge by cycling thorugh all the rounds based on the cards we have been shown in each round
def analyse_rounds_cards_shown(rounds, knownPeople, knownWeapons, knownRooms):
    for round in rounds:
        knownPeople, knownWeapons, knownRooms = update_knowledge(round.card, knownPeople, knownWeapons, knownRooms)
    return knownPeople, knownWeapons, knownRooms

#update knowledge by cycling through all the rounds based on the cards other players have been showing
def analyse_rounds_sherlock(rounds, knownPeople, knownWeapons, knownRooms):
    for round in rounds:
        helper = players[round.helper]
        cards_asked_about = {round.weapon, round.person, round.room}
        card = sherlock(helper.notOwnedCards, cards_asked_about)
        knownPeople, knownWeapons, knownRooms = update_knowledge(card, knownPeople, knownWeapons, knownRooms)
    return knownPeople, knownWeapons, knownRooms

#generate a game of cluedo
rounds = round_generator()
players = player_generator(total_number_of_players)

#tell the subprogrames to analyse the data from the game
knownPeople, knownWeapons, knownRooms = analyse_rounds_cards_shown(rounds, knownPeople, knownWeapons, knownRooms)
players = cards_players_dont_have(players, rounds)
knownPeople, knownWeapons, knownRooms = analyse_rounds_sherlock(rounds, knownPeople, knownWeapons, knownRooms)

#work out the suspects from the game 
suspectedPeople = suspected_people(people, knownPeople)
suspectedWeapons = suspected_weapons(weapons, knownWeapons)
suspectedRooms = suspected_rooms(rooms, knownRooms)
print(suspectedPeople)
print(suspectedWeapons)
print(suspectedRooms)