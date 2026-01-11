!pip install groq
import random
import gradio as gr

# word list
words = ["apple", "banana", "orange", "grapes", "mango"]
word = random.choice(words)

# hint letters (shown before first guess)
guessed_letters = []
guessed_letters.append(word[0])
guessed_letters.append(random.choice(word))

wrong_guesses = 0
max_wrong = 6

# function to show word
def get_display_word():
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# initial hint shown BEFORE guessing
initial_status = (
    "Word: " + get_display_word() +
    "\nRemaining attempts: " + str(max_wrong)
)

def play_hangman(guess):
    global wrong_guesses, guessed_letters

    guess = guess.lower()

    if guess:
        if guess in guessed_letters:
            message = "You already guessed this letter."
        else:
            guessed_letters.append(guess)
            if guess not in word:
                wrong_guesses += 1
                message = "Wrong guess!"
            else:
                message = "Good guess!"
    else:
        message = ""

    display_word = get_display_word()

    status = (
        "Word: " + display_word +
        "\nRemaining attempts: " + str(max_wrong - wrong_guesses)
    )

    if "_" not in display_word:
        status += "\nYou won!"
    elif wrong_guesses == max_wrong:
        status += "\n You lost! Word was: " + word

    return status, ""

with gr.Blocks() as demo:
    gr.Markdown("## Hangman Game")
    gr.Markdown("Hint: First letter and one random letter are already shown")

    output = gr.Textbox(
        label="Game Status",
        value=initial_status,
        lines=4
    )

    letter_input = gr.Textbox(label="Enter a letter")
    btn = gr.Button("Guess")

    btn.click(
        play_hangman,
        inputs=letter_input,
        outputs=[output, letter_input]
    )

demo.launch()
