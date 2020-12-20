import pyglet
from pathlib import Path
import random
import os

# 1.1 Velikost grafických objektů
size = 42

# 1.2 Cesta k obrázkům
snake_images_path = Path("snake")
food_images_path = Path("foods")
poo_images_path = Path("poo/poop.png")

# 1.3 Načtení obrázků jídla
files = os.listdir(food_images_path)
food_list = []
for i in files:
    food_list.append(pyglet.image.load("foods/" + i))

# 1.4 Načtení obrázku hovínka
poo_image = pyglet.image.load(poo_images_path)


class State:
    def __init__(self):
        self.i = 0
        self.snake = [(0, 0), (1, 0)]
        self.snake_direction = 0, 1
        self.width = 10
        self.height = 10
        self.poo = []
        self.food = []
        self.new()
        self.food_type
        

    def move(self):
        # 2.1 Přiřadí aktuální pozici do pomocných proměnných
        old_x, old_y = self.snake[-1]
        
        # 2.2. Přiřadí aktuální směr do pomocných proměnných
        dir_x, dir_y = self.snake_direction
        
        # 2.3 Vytvoří pomocné proměnné s údajem o pozici asměru pro jednotlivé osy
        new_x = old_x + dir_x
        new_y = old_y + dir_y
        
        # LADÍCÍ ČÁST
        print(f"Snake position X:{new_x}, Y:{new_y}")
        
        # 2.4 Vytvoří pomocnou entici z promměnných viz. 2.3
        new_head = new_x, new_y

        end = "GAME OVER. Score: "+ str(len(self.snake))
        # 2.5 Podmínky hlídající hada na hrací ploše, náraz do hovínka a náraz do sebe sama 
        if new_x < 0 or new_head in self.poo or new_head in self.snake:
            exit(end)
        if new_y < 0 or new_head in self.poo or new_head in self.snake:
            exit(end)
        if new_x >= self.width or new_head in self.poo or new_head in self.snake:
            exit(end)
        if new_y >= self.height or new_head in self.poo or new_head in self.snake:
            exit(end)
        
        # 2.6 Připojí entici z 2.4 do seznamu
        self.snake.append(new_head)
        
        # 2.7 Pokud se pozice hlavy rovná pozici jídla, smaže jídlo a vytvoří nové. Pokud se pozice hlavy nerovná pozici jídla, smaže poslední článek hada.
        if new_head in self.food:
            self.food.remove(new_head)
            self.new()
        else:
            del self.snake[0]


    def new(self):

        # 3.1 Cyklus - maximální počet nových objektů = 100
        for temp in range(100):

            # 3.2 Do pomocných proměnných se uloží náhodné číslo jehož maximální hodnota je výška hracího pole, nebo šířka hracího pole
            x_snake = random.randrange(self.width)
            y_snake = random.randrange(self.height)

            # 3.3 Vybere druh jídla - náhodně + LADÍCÍ ČÁST
            self.food_type = random.randrange(len(food_list))
            print(f"Food type: {self.food_type}")

            # 3.4 Vztvoří se sořadnice z hodnot viz. 3.2 
            position_snake = x_snake, y_snake

            # 3.5 Do souřadnic pro hovínko se zapíše souřadníce poslední části hada (ocasu)
            position_poo = self.snake[0]

            # 3.6 Podmínka zjišťující zda nové souřadnice jídla nejsou na pozici kde se nachází had nebo jídlo. 
            if (position_snake not in self.snake) and (position_snake not in self.food) :

                # 3.7 Při splnění podmínky 3.6 se do seznamu souřadnic jídla přidá nová souřadnice
                self.food.append(position_snake)

                # 3.8 Každé tři snězené jídla přidají jedno hovínko
                if self.i == 3:
                    self.poo.append(position_poo)
                    self.i = 0
                else:
                    self.i += 1
                
                # LADÍCÍ ČÁST
                print (f"Food position {x_snake}, {y_snake}")
                print (f"Self.snake {self.snake}, Self.food {self.food}, Self.poo {self.poo}")
                return


# 1.5 Vytvoří prázdný slovník pro jednotlivé části hada
snake_tiles = {}

# 1.6 Načtou se obrázky do slovníku
for path in snake_images_path.glob("*.png"):
    snake_tiles[path.stem] = pyglet.image.load(path)

window = pyglet.window.Window()

state = State()

# 1.7 zapíše do atributu objektu typu třídy počet polí které vzniknou dělením výšky/šířky hrací plochy a velikostí objektu
state.width = window.width // size
state.height = window.height // size


@window.event
def on_draw():
    window.clear()
    # 4.1 Vykreslí obrázek hada s parametry umístění a velikosti
    for x, y in state.snake:
        snake_tiles["tail-head"].blit(x * size, y * size, width=size, height=size)
    
    # 4.2 Vykreslí obrázek jídla s parametry umístění a velikosti
    for x, y in state.food:
        food_list[state.food_type].blit(x * size, y * size, width=size, height=size)
    
    # 4.3 Vykreslí obrázek hovínka s parametry umístění a velikosti
    for x, y in state.poo:
        poo_image.blit(x * size, y * size, width=size, height=size)


@window.event
# 1.8 Funkce zapisující směr do atributu objeku typu třída po stisknutí šipky na klávesnici
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        state.snake_direction = -1, 0
    if symbol == pyglet.window.key.RIGHT:
        state.snake_direction = 1, 0
    if symbol == pyglet.window.key.UP:
        state.snake_direction = 0, 1
    if symbol == pyglet.window.key.DOWN:
        state.snake_direction = 0, -1


def move(dt):
    state.move()


# 1.9 Zavolání funkce move každých 300 milisekund
pyglet.clock.schedule_interval(move, 0.3)

pyglet.app.run()
