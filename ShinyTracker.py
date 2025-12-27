import keyboard
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()
print('Welcome to the Pokemon Shiny Tracker!')

tracked_mon = input('Enter the name of the Pokemon to shiny hunt: ')
encounters = 0

while True:
    clear_console()
    print('Hunting a shiny', tracked_mon, '...')
    print('Controls: ↑ = increment, ↓ = decrement, ESC = quit program')
    print('Encounters:', encounters)
    key_event = keyboard.read_event()
    
    if key_event.event_type == keyboard.KEY_DOWN:
        if key_event.name == 'up':
            encounters+=1
        elif key_event.name == 'down':
            if encounters - 1 >= 0:
                encounters-=1
        elif key_event.name == 'esc':
            print('Goodbye!')
            break