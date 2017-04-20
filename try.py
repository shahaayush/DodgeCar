import pyglet, random, math, sys, neat
from game import *
from pyglet.window import key

# Set up a window
window = pyglet.window.Window(500, 600)

main_batch = pyglet.graphics.Batch()

# Set up the two top labels
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
generation_label = pyglet.text.Label(text="Generation: 0", x=10, y=555,batch=main_batch)
max_fitness_label = pyglet.text.Label(text="Max Fitness: 0", x=10, y=535, batch=main_batch)
avg_fitness = pyglet.text.Label(text="Avg Fitness: 0", x=10, y=515, batch=main_batch)
alive_label = pyglet.text.Label(text="Alive gamers: 0", x=10, y=495, batch=main_batch)
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
blocks = []

def fitness(pop):
    print 'LOOLOLOLOLO'
    global score
    for genome, gamer in zip(pop, gamers):
        genome['fitness'] = gamer.genome['fitness']

save = None
if len(sys.argv) > 1:
    save=True
nn = neat.main(fitness, gen_size=99999, pop_size=200, save=save)
pop = []
generation = 0
max_fitness = 1
avg_fitness = 1
alive_gamers = 0

def restart():
    global fittest, fittest_act, max_fitness, pop, avg_fitness, score
    global generation, max_fitness
    generation += 1
    pop = next(nn)
    max_fitness = max(max_fitness, score)
    avg_fitness = sum(x['fitness'] for x in pop)/len(pop)

    # Set score to 0
    score = 0
    score_label.text = "Score: {}".format(score)
    generation_label.text = "Generation:: {}".format(generation)
    max_fitness_label.text = "Max Fitness:: {}".format(max_fitness)

    global game_objects, gamers, blocks

    # Delete game objects
    for block in blocks:
        block.delete()

    for gamer in gamers:
        gamer.delete()

    # Initialize gamers of the new generation
    gamers = []
    for genome in pop:
        gamer = player.Player(x=200, y=60, batch=main_batch)
        # gamer.y += float(gamer.scale * PLAYER_SIZE / 2)
        gamer.genome = genome
        gamer.activate = neat.generate_network(genome)
        gamers.append(gamer)

    # Initialize 3 starting blocks
    blocks = load.gen_enemies(3, batch=main_batch)

    # Store all objects
    game_objects = gamers + blocks

    # game_window.push_handlers(gamers)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        for gamer in gamers:
            if gamer.x== 300 and not gamer.dead:
                gamer.x= 200
            else :
                gamer.x= 200

    if symbol == key.RIGHT :
        for gamer in gamers:
            if gamer.x== 200 and not gamer.dead:
                gamer.x= 300
            else :
                gamer.x= 300
    


@window.event
def on_key_release(symbol, modifiers):
    pass

@window.event
def on_draw():
    window.clear()
    bg.draw()
    main_batch.draw()

def update(dt):
    dt = 20*dt
    global blocks, game_objects, car_ship, score

    alive_label.text = "Alive gamers: {}".format(len([x for x in gamers if not x.dead]))

    if len(blocks) < 3:
        try:    
            blocks.extend(load.gen_enemies(3-len(blocks), blocks[-1].y, batch=main_batch))
        except IndexError:
            blocks = load.gen_enemies(3, 200, batch=main_batch)

    blocks_ahead = filter(lambda b: b.y > 150, blocks)
    sorted_blocks = sorted(blocks_ahead, key=lambda b: b.y)
    try:
        closest_block_x = (sorted_blocks[0].x - 200)/100
        closest_block_y = sorted_blocks[0].y
    except:
        closest_block_x = 0
        closest_block_y = 0
    # try:
    #     second_closest_block = sorted_blocks[1].position
    # except:
    #     second_closest_block = 0
    # try:
    #     third_closest_block = sorted_blocks[2].position
    # except:
    #     third_closest_block = 0
    nn_in = [0, 0, 0, 0]
    nn_in = [0, 0]
    nn_in = closest_block_x, closest_block_y

    r_count = 0
    for gamer in gamers:
        if not gamer.dead:
            if gamer.activate(nn_in)[0] > 0.5:
                r_count += 1
                gamer.x = 300
            else:
                gamer.x = 200
            gamer.update(dt)
    # print r_count, " gamers went right"

    removal = []
    for block in blocks:
        block.update(dt)
        for gamer in gamers:
            if not gamer.dead:
                if gamer.collides_with(block):
                    gamer.genome['fitness'] = score
                    gamer.dead = True
                    gamer.y = -99999

        if block.dead:
            removal.append(block)

    for block in removal:
        blocks.remove(block)
        block.delete()

    if len([g for g in gamers if not g.dead]) == 0:
    # if no gamers are alive, start next generation
        pyglet.clock.unschedule(update)
        print("Dead. Restarting..")
        init()
        return

    score += 10 * dt
    score_label.text = "Score: {}".format(int(score))

def init():
    restart()
    pyglet.clock.schedule_interval(update, 1 / 120.0)


if __name__ == '__main__':
    init()
    pyglet.app.run()





