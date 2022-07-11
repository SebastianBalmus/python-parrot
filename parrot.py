from color_dict import colors
import time
import keyboard
import os


while True:
    for frame in range(10):

        with open(f'frames/{frame}.txt', 'r') as f:
            lines = f.read()

            print('\n\n**********PRESS ESC TO STOP DANCING**********')
            print('\n\n\n')
            print(colors[frame] + lines + colors['reset'])
            print('\033[?25l', end="")

            if keyboard.is_pressed('esc'):
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()

            time.sleep(0.015)
            os.system('cls' if os.name == 'nt' else 'clear')
