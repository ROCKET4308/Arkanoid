from classes.Block import Block

blocks = []

for i in range(50, 200, 30):
    for j in range(50, 700, 70):
        blocks += [Block([j, i], 50, 20)]

