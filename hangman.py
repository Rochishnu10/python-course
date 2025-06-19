import random

words = ["ant", "bat", "cat", "duck", "elephant", "frog","apple", "brick", "cloud", "dream",
        "eagle", "flame", "grape", "house", "island", "jelly", "kite", "lemon", "magic", 
        "north", "ocean", "pearl", "queen", "river", "stone", "tiger", "umbrella", "valley",
        "whale", "xenon", "yarn", "zebra", "anchor", "breeze", "candle", "drum", "echo", 
        "feather", "giant", "honey", "iron", "jungle", "knife", "ladder", "mirror", "nest", 
        "orbit", "planet", "quiet", "rocket", "shadow", "train", "unity", "vapor", "window", 
        "xylem", "year", "zone", "arc", "beam", "chess", "dove", "ember", "frost", "glow", 
        "hill", "ink", "jade", "knot", "leaf", "maze", "net", "owl", "pipe", "quilt", "rope",
        "sand", "tail", "urn", "vine", "wave", "axe", "yoke", "zip", "ant", "ball", "coin",
        "duck", "egg", "fan", "gap", "hat", "ice", "jam", "key", "log", "man", "nap", "oak",
        "pan", "rat", "sun", "top", "use", "van", "web"]  #100 random words

chosen_word = random.choice(words)
replaced = ""
chance = 5
guessed = 0
correct_letter=[]

# print(chosen_word)

for i in range(0,len(chosen_word)):
    replaced +="_ "

print(replaced)

game_over = False


while not game_over:
    display= ""
    print(f"guess left : {chance}")
    guess = str(input("enter your guess: "))
    
    if guess not in chosen_word:
        chance-=1
        
    for letter in chosen_word :
        
        if letter == guess:
            correct_letter.append(guess)
            display+=guess
            
        elif letter in correct_letter:
            display+=letter
            
        else:
            display+="_"
            
    
    print("\n")   
    print(display)
    # print("\n\n")
    if "_" not in display :
        game_over = True
        print("you win")
    if chance == 0:
        game_over= True
        print("\n\nyou lose")
        print(f"the correct word was :   {chosen_word}")

        
    
