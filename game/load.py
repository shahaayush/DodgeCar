import pyglet, math, random
import physicalobject, resources, enemy

def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)

def cars(batch=None):
    new_sprite = pyglet.sprite.Sprite(img=resources.car_image, 
                                          x=350, y=60, 
                                          batch=batch)
    new_sprite.scale = 0.06
    return new_sprite

def gen_enemies(num_icons, start_y=120, batch=None):
    blocks = []
    for i in range(num_icons):
        # x = start_x + random.randint(40, 150) * (i + 1) + 100 * (i + 1)
        # while y>120 and y<550
        try:
            y = blocks[-1].y + random.randint(90, 150)
        except IndexError:
            y = start_y + random.randint(100, 350)
        xl = random.sample(set([200,300]), 1)
        new_sprite = enemy.Enemy(x=xl[0], y=y, batch=batch)
        # new_sprite.scale = 0.2
        blocks.append(new_sprite)
    return blocks

# def asteroids(num_asteroids, player_position, batch=None):
#     """Generate asteroid objects with random positions and velocities, not close to the player"""
#     asteroids = []
#     for i in range(num_asteroids):
#         # asteroid_x, asteroid_y = player_position
#         # while distance((asteroid_x, asteroid_y), player_position) < 100:
#         asteroid_xl = random.sample(set([200,300]), 1)
#         asteroid_x=asteroid_xl[0]
#         asteroid_y = random.randint(120,550)
#         new_asteroid = physicalobject.PhysicalObject(img=resources.enemy_image, 
#                                                      x=asteroid_x, y=asteroid_y,
#                                                      batch=batch)
#         new_asteroid.velocity_x, new_asteroid.velocity_y = 0,200
#         asteroids.append(new_asteroid)
#     return asteroids
