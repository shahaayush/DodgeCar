import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

# Tell pyglet where to find the resources
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

# Load the three main resources and get them to draw centered

car_image = pyglet.resource.image("car.png")
center_image(car_image)

road_image = pyglet.resource.image("road.jpeg")
center_image(road_image)


enemy_image = pyglet.resource.image("enemy.png")
center_image(enemy_image)
