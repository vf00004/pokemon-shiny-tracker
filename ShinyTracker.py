import keyboard
import os
import json

POKEMON_NAMES = 'pokemon_species.json'
database = None
tracked_mon = None

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_species_json():
    global database 
    with open(POKEMON_NAMES, 'r', encoding='utf-8') as f:
        database = json.load(f)
        
def check_mon_validity(tracked_mon):
    global database
    if tracked_mon.lower() in database:
        return True

def get_tracked_mon():
    global tracked_mon
    is_valid = False
    while not is_valid:
        tracked_mon = input('Enter the name of the Pokemon to shiny hunt: ')
        is_valid = check_mon_validity(tracked_mon)

if __name__ == '__main__':
    open_species_json()
    clear_console()
    
    print('Welcome to the Pokemon Shiny Tracker!')
    get_tracked_mon()
    encounters = 0

    while True:
        clear_console()
        print('Hunting a shiny', tracked_mon, '...')
        print('Controls: ↑ = increment, ↓ = decrement, ESC = quit program')
        print('Encounters:', encounters)
        key_event = keyboard.read_event()
        
        if key_event.event_type == keyboard.KEY_DOWN:
            if key_event.name == 'up':
                encounters += 1
            elif key_event.name == 'down':
                if encounters - 1 >= 0:
                    encounters -= 1
            elif key_event.name == 'esc':
                print('Goodbye!')
                break