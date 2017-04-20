import pyglet, random, math
from game import *

# Set up a window
game_window = pyglet.window.Window(500, 600)

main_batch = pyglet.graphics.Batch()

# Set up the two top labels
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
# generation_label = pyglet.text.Label(text="Generation: 0", x=10, y=555, batch=main_batch)
# max_fitness_label = pyglet.text.Label(text="Max Fitness: 0", x=20, y=340)
# avg_fitness = pyglet.text.Label(text="Avg Fitness: 0", x=20, y=340)
# alive_label = pyglet.text.Label(text="Alive gamers: 0", x=20, y=360)
game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=250, y=-300, anchor_x='center', 
                                    batch=main_batch, font_size=48)


bg = pyglet.sprite.Sprite(resources.road_image)
bg.scale=0.7
bg.x = 250
bg.y = 300


PLAYER_SIZE = 100
score = 1
game_objects = []
gamers = []
# blocks = []

car_ship = player.Player(x=200, y=60, batch=main_batch)

# replaced name of asteroids by blocks
blocks = load.gen_enemies(3,batch= main_batch)
print("length at start of block is "+str(len(blocks)))

# # Store all objects that update each frame in a list
game_objects = [car_ship] + blocks

# # Tell the main window that the player object responds to events
game_window.push_handlers(car_ship)

@game_window.event
def on_draw():
    game_window.clear()
    bg.draw()
    main_batch.draw()

def update(dt):
    
    global blocks, game_objects, car_ship

    if len(blocks) < 3:
        try:    
            blocks.extend(load.gen_enemies(3-len(blocks), blocks[-1].y, batch=main_batch))
        except IndexError:
            blocks = load.gen_enemies(3, 200, batch=main_batch)

    removal = []
    for obj in blocks:
        obj.update(dt)
        if obj.dead:
            removal.append(obj)

    # Get rid of dead objects
    for block in removal:
        blocks.remove(block)
        block.delete()

    if not car_ship.dead:
        car_ship.update(dt)

    for block in blocks:
        if block.collides_with(car_ship):
            car_ship.dead = True

    if car_ship.dead:
        game_over_label.y = 300

    global score
    score += 10 * dt
    score_label.text = "Score: {}".format(int(score))


if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/120.0)
    
    # Tell pyglet to do its thing
    pyglet.app.run()
