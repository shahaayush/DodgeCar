import math
from pyglet.window import key
import physicalobject, resources , load

class Player(physicalobject.PhysicalObject):
    """Physical object that responds to user input"""
    
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.car_image, *args, **kwargs)
        
        self.keys = dict(left=False, right=False)
    
    def on_key_press(self, symbol, modifiers):    
        if symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
    
    def update(self, dt):
        # Do all the normal physics stuff
        super(Player, self).update(dt)
        
        if self.keys['left']:
            if self.x == 300:
                self.x -= 100
            else :
                self.x = 200

        if self.keys['right']:
            if self.x == 200:
                self.x += 100
            else : 
                self.x = 300
    
    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        # self.engine_sprite.delete()
        super(Player, self).delete()