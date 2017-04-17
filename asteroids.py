import pyglet, random, math
from game import load, resources , player

# Set up a window
game_window = pyglet.window.Window(500, 600)

main_batch = pyglet.graphics.Batch()

# Set up the two top labels
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)

bg = pyglet.sprite.Sprite(resources.road_image)
bg.scale=0.7
bg.x = 250
bg.y = 300

car_ship = player.Player(x=200, y=60, batch=main_batch)

asteroids = load.asteroids(3, car_ship.position, main_batch)

# # Store all objects that update each frame in a list
game_objects = [car_ship] + asteroids

# # Tell the main window that the player object responds to events
game_window.push_handlers(car_ship)

@game_window.event
def on_draw():
    game_window.clear()
    bg.draw()
    main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)
    # To avoid handling collisions twice, we employ nested loops of ranges.
    # This method also avoids the problem of colliding an object with itself.
    for i in xrange(len(game_objects)):
        for j in xrange(i+1, len(game_objects)):
            
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            
            # Make sure the objects haven't already been killed
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)
    
    # Get rid of dead objects
    for to_remove in [obj for obj in game_objects if obj.dead]:
        # Remove the object from any batches it is a member of
        to_remove.delete()
        
        # Remove the object from our list
        game_objects.remove(to_remove)


if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/120.0)
    
    # Tell pyglet to do its thing
    pyglet.app.run()
