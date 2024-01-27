#The game takes words from a self created corpus called hangman.txt
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK stop words 
import nltk
nltk.download('stopwords')

def choose_word():
    with open('self_made_corpus.txt', 'r', encoding='utf-8') as file:
        text = file.read()
       
        words = word_tokenize(text.lower())
        
    
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if len(word) >= 5 and word not in stop_words]
    
    return random.choice(filtered_words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def draw_hangman(attempts):
    hangman_pics = [
        """
         -----
         |   |
             |
             |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
             |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
        ------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
        ------
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
        ------
        """
    ]
    print(hangman_pics[6 - attempts])

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    while attempts > 0:
        draw_hangman(attempts)
        display = display_word(word, guessed_letters)
        print("Word: " + display)
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
        else:
            print("Incorrect guess. Try again.")
            attempts -= 1
        
        if "_" not in display:
            draw_hangman(attempts)
            print("Congratulations! You guessed the word:", word)
            break
        
        print("Attempts left:", attempts)
    
    if attempts == 0:
        draw_hangman(attempts)
        print("Sorry, you're out of attempts. The word was:", word)
    
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()

# Run the game
hangman()

