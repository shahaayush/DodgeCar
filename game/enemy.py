import physicalobject, resources , load


class Enemy(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Enemy, self).__init__(resources.enemy_image, *args, **kwargs)
        self.velocity_y = 200
        self.dead= False

    def check_bounds(self):
        if self.y < -20:
            print("SOMEONE DIED")
            self.dead = True
        # else:
        #     self.dead= False  
    
    # def update(self, dt):
    #     super(Enemy, self).update(dt)

    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        # self.engine_sprite.delete()
        super(Enemy, self).delete()
        
