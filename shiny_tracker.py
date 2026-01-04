import keyboard
import os
import json

POKEMON_NAMES = 'pokemon_species.json'
database = None
progress_data = {}

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
    is_valid = False
    while not is_valid:
        tracked_mon = input('Enter the name of the Pokemon to shiny hunt: ')
        is_valid = check_mon_validity(tracked_mon)
    return tracked_mon

def load_progress():
    with open('shiny_progress.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def update_progress(tracked_mon, encounters_so_far):
    global progress_data
    progress_data = {"pokemon": tracked_mon,
                    "encounters": encounters_so_far}

def save_progress():
    with open('shiny_progress.json', 'w', encoding="utf-8") as f:
        json.dump(progress_data, f, indent=2)

if __name__ == '__main__':
    open_species_json()
    clear_console()
    
    print('Welcome to the Pokemon Shiny Tracker!')
    
    tracked_mon = None
    encounters = None
    can_continue = False
    
    while not can_continue:
        print('\n0 -> Hunt a new Pokemon\n1 -> Load previous hunt')
        user_choice = input('\nType a number:')
        
        try:
            parsed_choice = int(user_choice)
            
            if parsed_choice == 0:
                tracked_mon = get_tracked_mon()
                encounters = 0
                can_continue = True
            elif parsed_choice == 1:
                pokemon_to_hunt = load_progress()
                tracked_mon = pokemon_to_hunt["pokemon"]
                encounters = pokemon_to_hunt["encounters"]
                can_continue = True
            else:
                clear_console()
                print('Please input a valid option:')
        except ValueError:
            clear_console()
            print('Please input a number:')


    while True:
        clear_console()
        print('Hunting a shiny', tracked_mon, '...')
        print('Controls: ↑ = increment, ↓ = decrement, ESC = save & quit program')
        print('Encounters:', encounters)
        key_event = keyboard.read_event()
        
        if key_event.event_type == keyboard.KEY_DOWN:
            if key_event.name == 'up':
                encounters += 1
            elif key_event.name == 'down':
                if encounters - 1 >= 0:
                    encounters -= 1
            elif key_event.name == 'esc':
                update_progress(tracked_mon, encounters)
                save_progress()
                print('Progress saved! Goodbye.')
                break