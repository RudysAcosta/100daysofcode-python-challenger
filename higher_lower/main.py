import json
import random
import os
from ascii_art import art, art_vs

print(f"{art}")

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# Open JSON File and read content
def get_movies():
    with open('json/movies.json', 'r') as file:
        context = file.read()
    
    movies = json.loads(context)['peliculas']

    return movies

def select_item(items, item_selected = None):

    item  = random.choice(items)

    while item_selected != None and item['id'] == item_selected['id']:
        item  = random.choice(items)
    
    return item

def print_item(item):
    return f"{item['titulo']}, {item['director']}, {item['anio']}"

def show_start_message(items, score):
    clear_screen()
    print(f"{art}")

    if score > 0:
       print(f"Your Score: {score}") 

    print(f"Compare A: {print_item(items[0])}")
    print(art_vs)
    print(f"Against B: {print_item(items[1])}")

    chosse = input("Which one was the highest-grossing? Type 'A' or 'B': ")
    return chosse

def run():
    score = 0
    movies = get_movies()
    items = []
    items.append(select_item(movies))
    items.append(select_item(movies, items[0]))

    
    while True:
        chosse = show_start_message(items, score).upper()

        if chosse not in ['A','B']:
            continue

        if chosse == 'A':
            if items[0]['recaudacion'] > items[1]['recaudacion']:
                print(items[0]['recaudacion'], items[1]['recaudacion'])
                score += 1
                items[1] = select_item(movies, items[0])
                continue

        elif chosse == 'B':
            if items[0]['recaudacion'] < items[1]['recaudacion']:
                print(items[0]['recaudacion'], items[1]['recaudacion'])
                score += 1
                items[0] = select_item(movies, items[1])
                continue
        
        
        print(f"Sorry, that's wrong. Final score: {score}")
        exit()

        


if __name__ == '__main__':
    run()