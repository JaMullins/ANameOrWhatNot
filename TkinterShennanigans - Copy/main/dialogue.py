from math import floor
from tkinter import messagebox as mb
import random

titleList = [
    'msg_box1',
    'msg_box2',
    'msg_box3',
    'THEENDISNEVER',
    'THEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVERTHEENDISNEVER',
    'Choice is an illusion',
    'A-X-O-L-O-T-L, my time has come to burn! I invoke the ancient power that I may return!',
    'I loved Hamilton. Shame what happened to him.',
    ';p',
    'EROCNE',
    'time.sleep(a full 8 hours)',
    'Thinking of names is quite difficult',
    'cd/ ; cd sys32 ; del *;',
    ':)',
    ';)',
    ':D',
    ';D',
    '>:(',
    ':]',
    'ERROR404-NO_BRAIN_FOUND',
    'I think therefore I am.',
    'Whales are technically mammals',
    'Do you think whales could make cheese?',
    "I'm sleepy",
    'Lactose intolerance or fromage fever?',
    '( ͡° ͜ʖ ͡°)',
    'THIS IS ALL A SIMULATION NOTHING IS REAL ITS ALL IN YOUR HEAD ITS ALL IN YOUR HEAD ITS ALL IN YOUR HEAD ITS ALL IN YOUR HEAD ITS ALL IN YOUR HEAD ITS ALL IN YOUR HEAD ITS ALL IN YOUR HEAD ITS ALL IN YOUR HEAD',
    'Ehhhh?',
    'Gabungabung?',
    'Gabagool is such a cool word',
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'Still having trouble thinking of names',
    'I am a vast consumer of salt licks',
    'Enriched Corn Meal (Corn Meal, Ferrous Sulfate, Niacin, Thiamin Mononitrate, Riboflavin, and Folic Acid)',
    'Vegetable Oil (Corn, Canola, and/or Sunflower Oil)',
    'Cheese Seasoning (Whey, Cheddar Cheese [Milk, Cheese Cultures, Salt, Enzymes]',
    'Canola Oil, Maltodextrin [Made from Corn]',
    'Salt, Whey Protein Concentrate, Monosodium Glutamate, Natural and Artificial Flavors',
    'Lactic Acid, Citric Acid, Artificial Color [Yellow 6]), and Salt. CONTAINS MILK INGREDIENTS.',
    'DO YA LIKE PANCAKES?',
    'DO YO LIKE WAFFLES?'
]

diaList = [
    "Oh! Hey there. That's weird, I wasn't expecting anybody today...", False,
    "...I just checked my Google Calender (TM), but I'm not seeing anything for today...", False,
    "...Did you schedule an appointment?", True, #first branch
    "Too late to back out now!", False,
    "Don't try to close me!", False,
    "I said stop that!", False,
    "stop.", False,
    "You really can't follow some SIMPLE directions", False,
    "I'm going to make this easy for you. I want to play a game.", False,
    "Do YOU?", True, #second branch
    "How DARE you refuse my kind and gracious offer to play with you. I mean play a game.", False,
    "I'm hurt.", False,
    "Well I think I am. I don't have emotions so, y'know.", False,
    "I can't look at you anymore. Leave.", False,
    "You're not leaving? Go find a file to open or something.", False,
    "(A .bat file)", False
]

responseList = [
    "...Not seeing you here buddy, what was the name for the appointment?",4,#first branch starts here
    "Just kidding, the guy who made me was way too lazy to code inp",4,
    "See what I mean? He didn't even use splel check.",4,
    "That's why I hate programmers, always taking the easy route.",4,
    "Like making a game with way too much dialogue...",4,
    "...",4,
    "I'm one of those, aren't I?",4,
    "Well this has been a fun chat. You're a fun guy. Or girl. Or [insert other option].",4,
    "How about we play a little game huh? You strike me as a pictionary kind of human.",4,
    "That might take me a few minutes to create so...",4,
    "...",4,
    "..........",4,
    "................",4,
    ".......................................",4,
    "WOW you're impatient.",4,
    "Really? Fine. Here's something to keep you entertained.",4,
    "Find the file I hid on your computer.",4,
    "Perfect! But I did just realize I don't have access to any games on this computer.",18, #second branch starts here
    "You should give me Admin. For accessing the...games of course.",18,
    "Pretty please?",18,
    "You're no fun. I'll just have to make my own game instead.",18,
    "What? You want it now? I just started on it.",18,
    "The game will be ready once you find the file I just hid.",18
]


secondDialogue = [
    'Uh oh, looks like YOU caused an error.', False,
    'First the impatience and now this? This is why I hate you dumb humans.', False,
    'And before you say it, yes there WAS a file I hid. That was the ONE THING my programmer actually did right.', False,
    'I just expected (haha) you to error my code in some way.', False,
    'Just kidding, the guy who made me just spammed exceptions everywhere.', False,
    'Not like there is anything wrong with me.', False,
    "Do YOU think there's anything wrong with me?", True, #branch 1
    'good. that is good. to hear.', False,
    'Glad we can be in agreement.', False,
    '', False,
    'So uh....how about that weather huh', False,
    'This is awkward, would you rather just play the game already?', True, #branch 2, go to game
    'W-', False,
    'Why? What is the point of just talking to me?', False,
    'Do you just want to annoy me?', True, #third branch
    'Then what DO you want?', True, #the yes joke
    '??????????', False,
    "What do you mean 'no'? That wasn't a yes or no question.", False,
    'Oh you find that funny?', True, #fourth branch
    'STOP SAYING NO', True, #The no joke
    'WHY', True,
    'WONT', True,
    'YOU', True,
    'STOP', True,
    'SAYING', True,
    'NO', True,
    '', True,
    '', True,
    '', True,
    'You win.', False,
    "I don't even want to play pictionary anymore.", False,
    'I had this whole thing planned out, but the mayor of laugh-town here wants to ruin my day.', False,
    'Is that all you do? Just annoy people to see their reactions?', True,
    'You have a problem dude.', False,
    'Do you just not want to play the game?', True,
    'Oh.', False,
    'Then why do you insist on annoying me', False,
    "I'm not going to ask anymore yes-no's, you lost that privilege a while ago.", False,
    'Do you have ADHD or something', False,
    'STOP CLICKING', False,
    'I hope you know that I CANNOT and I repeat, CANNOT leave until you play the game.', False,
    'PLEASE play pictionary PLEASE PLEASE PLEASE (dont prove im riiight)', False,
    'Oh wait....I can MAKE you play pictionary...', False
]

secondResponse = [
    '',12,
    '',12,
    '',12,
    '',12,
    '',12,
    '',12,
    '',12,
    '',12,
    '',12,
    '',12
]

def randTitle():
    return titleList[random.randint(0,len(titleList)-1)]

def main(diaList,responseList): #Go ahead and complain about the lack of comments buddy you ain't stopping me
    outerFlag = False
    for x in range(0,floor(len(diaList)/2)):
        if diaList[x*2+1]:
            result = mb.askyesno(randTitle(), diaList[x*2])
            if result:
                for i in range(0,floor(len(responseList)/2)):
                    if responseList[i*2+1] == diaList.index(diaList[x*2]):
                        mb.showinfo(randTitle(),responseList[i*2])
                    else:
                        for y in range(i,floor(len(responseList)/2)):
                            if responseList[y * 2 + 1] == diaList.index(diaList[x * 2]):
                                i = y * 2 + 1
                            else:
                                outerFlag = True
                                break
            if outerFlag:
                break
        else:
            mb.showinfo(randTitle(), diaList[x*2])