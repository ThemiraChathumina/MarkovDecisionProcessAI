# Index: 200088D
# Name: K.H.T.Chathumina

def value_iteration(rewards, epsilon):
    """
    This function returns the final utility values after converging as a dictionary with state number and utility value.
    """
    world = [[[0, 0, 0, 4], [0, 0, 0, 5], [0, 0, 0, 6]],
             [[0, 0, 0, 1], [0, 0, 0, 2], [0, 0, 2, 3]]]
    actions = ['N', 'E', 'S', 'W', 'DN']
    p = {'u': 0.9, 'l': 0.05, 'r': 0.05, 'dn': 1}
    gamma = 0.999
    rows = len(world)
    cols = len(world[0])
    for i in range(rows):
        for j in range(cols):
            world[i][j][1] = rewards[world[i][j][3] - 1]
    while True:
        delta = 0
        for i in range(rows):
            for j in range(cols):
                if world[i][j][2] == 3:
                    continue
                temp = world[i][j][0]
                s = [0 for a in actions]
                for action in range(len(actions)):
                    x = {'up': 0, 'left': 0, 'right': 0, 'nothing': 0}
                    if actions[action] == 'N':
                        if i - 1 < 0:
                            x['up'] = p['u'] * world[i][j][0]
                        else:
                            x['up'] = p['u'] * world[i - 1][j][0]
                        if j - 1 < 0:
                            x['left'] = p['l'] * world[i][j][0]
                        else:
                            x['left'] = p['l'] * world[i][j - 1][0]
                        if j + 1 >= cols:
                            x['right'] = p['r'] * world[i][j][0]
                        else:
                            x['right'] = p['r'] * world[i][j + 1][0]
                    elif actions[action] == 'E':
                        if j + 1 >= cols:
                            x['up'] = p['u'] * world[i][j][0]
                        else:
                            x['up'] = p['u'] * world[i][j + 1][0]
                        if i - 1 < 0:
                            x['left'] = p['l'] * world[i][j][0]
                        else:
                            x['left'] = p['l'] * world[i - 1][j][0]
                        if i + 1 >= rows:
                            x['right'] = p['r'] * world[i][j][0]
                        else:
                            x['right'] = p['r'] * world[i + 1][j][0]
                    elif actions[action] == 'S':
                        if i + 1 >= rows:
                            x['up'] = p['u'] * world[i][j][0]
                        else:
                            x['up'] = p['u'] * world[i + 1][j][0]
                        if j + 1 >= cols:
                            x['left'] = p['l'] * world[i][j][0]
                        else:
                            x['left'] = p['l'] * world[i][j + 1][0]
                        if j - 1 < 0:
                            x['right'] = p['r'] * world[i][j][0]
                        else:
                            x['right'] = p['r'] * world[i][j - 1][0]
                    elif actions[action] == 'W':
                        if j - 1 < 0:
                            x['up'] = p['u'] * world[i][j][0]
                        else:
                            x['up'] = p['u'] * world[i][j - 1][0]
                        if i + 1 >= rows:
                            x['left'] = p['l'] * world[i][j][0]
                        else:
                            x['left'] = p['l'] * world[i + 1][j][0]
                        if i - 1 < 0:
                            x['right'] = p['r'] * world[i][j][0]
                        else:
                            x['right'] = p['r'] * world[i - 1][j][0]
                    else:
                        x['nothing'] = p['dn'] * world[i][j][0]

                    s[action] = x['up'] + x['right'] + x['left'] + x['nothing']
                world[i][j][0] = world[i][j][1] + gamma * max(s)
                if world[i][j][2] == 2:
                    world[i][j][0] = world[i][j][1]
                    world[i][j][2] = 3
                delta = max(delta, abs(temp - world[i][j][0]))
        if delta < epsilon * ((1 - gamma) / gamma):
            utilities = dict()
            for i in range(rows):
                for j in range(cols):
                    utilities[str(world[i][j][3])] = round(world[i][j][0], 4)
            return utilities




