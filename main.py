
import random 

word_list = {'electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop',
 'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 
 'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 
 'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider',
 'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language',
 'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus', 
 'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful',
 'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard', 
 'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser',
 'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen',
 'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
 'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
 'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph', 
 'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 
 'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete', 
 'brain', 'control', 'prophet', 'freedom', 'harbour', 'confidence', 'positive', 
 'harvest', 'hunger', 'woman', 'children', 'stranger', 'garden', 'pleasure', 
 'between', 'recognition', 'tomorrow', 'autumn', 'monkey', 'spring', 'winter', 
 'classification', 'typewriter', 'success', 'difference', 'acoustics', 
 'agreement', 'sorrow', 'christmas', 'silver', 'birthday', 'championship', 
 'comfortable', 'diffusion', 'murder', 'policeman', 'science', 'desert', 
 'blood', 'funeral', 'silence', 'garment', 'merchant', 'spirit', 'punishment', 
 'measurement', 'ocean', 'digital', 'illusion', 'tyrant', 'castle', 'passion', 
 'magician', 'remedy', 'knowledge', 'threshold', 'number', 'vision', 
 'absence', 'mystery', 'morning', 'device', 'thoughts', 'spirit', 'future', 

 'mountain', 'treasure', 'machine', 'whispering', 'eternity', 'reflection', 
 'achievement', 'lightning', 'secret', 'environment', 'shepherd', 'confusion', 
 'grave', 'promise', 'honour', 'reward', 'temple', 'distance', 'eagle', 'saturn',
 'finger', 'belief', 'crystal', 'fashion', 'direction', 'captain', 'moment', 
 'permission', 'logic', 'analysis', 'password', 'english', 'equalizer', 
 'emotion', 'battle', 'expression', 'scissors', 'trousers', 'glasses', 
 'dictionary', 'chemistry', 'induction', 'detail', 'widow', 'wealth', 'health',
 'disaster', 'volcano', 'poverty', 'limitation', 'perfect', 'intelligence',
 'failure', 'ignorance', 'destination', 'source', 'resort', 'satisfaction',
 'frequency', 'selection', 'substitution', 'kingdom', 'pattern', 'management', 
 'situation', 'multiply', 'treatment', 'dollar', 'intuition', 'chapter', 'magnet'
 'desire', 'command', 'action', 'consciousness', 'enemy', 'security', 'object', 
 'happen', 'happiness', 'worry', 'method', 'tolerance', 'error', 'hesitation', 
 'record', 'tongue', 'supply', 'vibration', 'stress', 'despair', 'restaurant', 
 'television', 'video', 'audio', 'layer', 'mixture', 'doorbell', 'cousin', 
 'finance', 'production', 'invisible', 'excitement', 'afternoon', 'office', 
 'illustration', 'valley', 'apartment', 'necessary', 'shortage', 'almost', 
 'blanket', 'suggestion', 'overflow', 'demonstration', 'challenge', 'compact', 
 'tower', 'question', 'problem', 'pressure', 'beast', 'encouragement', 'afraid', 
 'cavity', 'appearance', 'wonderful', 'matter', 'dimension', 'business', 'doubt',
 'conversation', 'reaction', 'psychology', 'superstition', 'smash', 'horseshoe', 
 'surprise', 'nothing', 'ladder', 'opposite', 'reality', 'genius', 'string', 
 'destruction', 'expensive', 'painting', 'chicken', 'wishing', 'profession', 
 'hatred', 'possession', 'criticism', 'zebra', 'harmony', 'personality', 
 'addition', 'subtraction', 'cipher', 'encryption', 'compression', 'extension', 
 'blessing', 'meeting', 'difficulty', 'weapon', 'against', 'external', 'internal'
 'legend', 'servant', 'secondary', 'license', 'directory', 'statistics', 

 'attraction', 'sensitivity', 'magnification', 'someone', 'symptom', 'recipe', 
 'service', 'family', 'island', 'planet', 'butterfly', 'diving', 'strength', 
 'extreme', 'opportunity', 'illumination', 'cable', 'conflict', 'interference', 
 'receiver', 'transmitter', 'channel', 'company', 'grocery', 'devil', 'angel', 
 'exactly', 'document', 'tutorial', 'sound', 'voice', 'abbreviation', 'abdomen', 
 'abrupt', 'absolute', 'absorption', 'abstract', 'academy', 'acceleration', 
 'accident', 'account', 'acidification', 'actress', 'adaptation', 'addiction', 
 'adjustment', 'admiration', 'adoption', 'advanced', 'adventure', 'advertisement'
 'agenda', 'airport', 'algorithm', 'allocation', 'aluminium', 'ambiguity', 
 'amphibian', 'anaesthesia', 'analogy', 'anchor', 'animation', 'anode', 'cathode'
 'apparent', 'appendix', 'approval', 'approximation', 'arbitrary', 'architecture'
 'arithmetic', 'arrangement', 'article', 'ascending', 'ashamed', 'asleep', 
 'assembly', 'astonishment', 'atmosphere', 'awful', 'bachelor', 'backbone', 
 'bacteria', 'balance', 'balloon', 'banana', 'barbecue', 'baseball', 'beaker', 
 'beggar', 'behaviour', 'benefit', 'bidirectional', 'biology', 'blackboard', 
 'bladder', 'bleeding', 'blender', 'bonus', 'bottle', 'bracket', 'branch', 
 'bubble', 'bucket', 'budget', 'bullet', 'burglar', 'butcher', 'bypass', 
 'calculator', 'calibration', 'campaign', 'cancellation', 'candidate', 'candle', 
 'carpenter', 'carriage', 'cartoon', 'cascade', 'casual', 'catalyst', 'category',
 'cement', 'ceremony', 'chairman', 'checkout', 'chimney', 'chocolate', 
 'circumference', 'civilization', 'classroom', 'clearance', 'client', 'coconut', 
 'coincidence', 'colleague', 'comfortable', 'competition', 'kangaroo', 'kidnap', 
 'journal', 'jockey', 'iteration', 'isometric', 'isolation', 'invitation',
 'institution', 'injection', 'humanity', 'housekeeper', 'history', 'heaven', 
 'greenhouse', 'glory', 'foundation', 'formula', 'fluctuation', 'fiction',
 'emission', 'elasticity', 'earthquake', 'dynamic', 'doctorate', 'divorce', 'deri '};



stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


lives = 6

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over= False
correct_letters = []

while not game_over:
    guess = input("guess a letter : ").lower()
    print(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("game over , you loose")

    if "_" not in display:
        game_over=True
        print("you won")
    
    print(stages[lives])


# Work in progress
        


