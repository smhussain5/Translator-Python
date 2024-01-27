"""
Terminal application that translates english text to 1 of 10 different languages
"""

from googletrans import Translator
from pyfiglet import Figlet

fig = Figlet(font="isometric1")  # WELCOME SCREEN
print(fig.renderText("LANG"))

print("WELCOME TO PYTHON TRANSLATE!")
print("It's simple. Just follow the prompts!")

translator = Translator()

language_options = {
    1: "ig",
    2: "es",
    3: "haw",
    4: "tl",
    5: "pt",
    6: "sq",
    7: "bg",
    8: "fr",
    9: "de",
    10: "la",
}

PLAY_AGAIN = True

while PLAY_AGAIN:
    print("\n>>> MENU <<<\n")
    print("Enter '1' for IGBO")
    print("Enter '2' for SPANISH")
    print("Enter '3' for HAWAIIAN")
    print("Enter '4' for FILIPINO")
    print("Enter '5' for PORTUGUESE")
    print("Enter '6' for ALBANIAN")
    print("Enter '7' for BULGARIAN")
    print("Enter '8' for FRENCH")
    print("Enter '9' for GERMAN")
    print("Enter '10' for LATIN\n")

    user_text = input("Enter text to be translated: ")
    lang_code = int(input("Enter language option: "))

    translation = translator.translate(
        user_text, src="en", dest=f"{language_options[lang_code]}"
    )

    print(f"\nYOUR TEXT ({translation.src.upper()}): {user_text}")
    print(f"TRANSLATION ({translation.dest.upper()}): {translation.text}\n")

    replay_choice = input("Try another translation? Enter Y/N...: ")  # APP REPLAY

    PLAY_AGAIN = bool(replay_choice.upper() == "Y")

print("Thanks! See you again next time!")  # APP END
