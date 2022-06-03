import random
words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks'] 

word=random.choice(words)
display = '*'*len(word)

missed = 0
game_over = False
while not game_over:
    print(display)
    guess = input("Guess a letter in the word >> {}" .format(display))
    
    i = 0
    if guess in word:
        while word.find(guess, i) != -1:
            i = word.find(guess, i)
            display = display[:i] + guess + display[i+1:]
            i+=1
        print('Correct')
    else:
        print("{} is not in the word" .format(guess))
        missed +=1
        
    if word == display:
        print("The word is {} and you missed {} times" .format(word, missed))
        game_over = True
    
