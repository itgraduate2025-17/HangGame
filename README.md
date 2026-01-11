# Hangman Game 

This is a simple Hangman game built using Python and Gradio.  
The game selects a random word from a predefined list and allows the user to guess letters.  

## What it does
The game shows a **hint before the first guess**, revealing the first letter and one random letter from the word.  
The player guesses letters one by one.  
The game keeps track of wrong guesses and ends when the player either guesses the word or runs out of attempts.  
The interface is built using Gradio for a user-friendly web interaction.

## How it is built
- Python: Handles the game logic and tracking of guessed letters  
- Gradio: Provides a simple interactive interface for input and output  
- Functions and loops: Used to update the displayed word and check win/loss conditions  

## Usage
1. Run the `hangman.py` file in Google Colab or your local environment  
2. The initial hint will be displayed  
3. Enter letters in the textbox to guess  
4. The game will show the current word status and remaining attempts
