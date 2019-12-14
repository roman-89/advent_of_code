

def transform_wire_to_coordinates_set(w):
    coords = set()
    pointer = (0, 0)
    for e in w.split(','):
        d = e[0]
        l = int(e[1:])
        x_delta = 0
        y_delta = 0
        if d == 'R':
            x_delta = 1
        elif d == 'L':
            x_delta = -1
        elif d == 'U':
            y_delta = 1
        elif d == 'D':
            y_delta = -1
        for _ in range(l):
            pointer = (pointer[0]+x_delta, pointer[1]+y_delta)
            coords.add(pointer)
    return coords
            

def closest_dist(w1, w2):
    c1 = transform_wire_to_coordinates_set(w1)
    c2 = transform_wire_to_coordinates_set(w2)
    cross = c1 & c2
    return min([abs(c[0])+abs(c[1]) for c in cross])


assert  closest_dist('R75,D30,R83,U83,L12,D49,R71,U7,L72',
                     'U62,R66,U55,R34,D71,R55,D58,R83') == 159
assert  closest_dist('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                     'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7') == 135
                     

# second part

def transform_wire_to_coordinates_list(w):
    coords = []
    pointer = (0, 0)
    for e in w.split(','):
        d = e[0]
        l = int(e[1:])
        x_delta = 0
        y_delta = 0
        if d == 'R':
            x_delta = 1
        elif d == 'L':
            x_delta = -1
        elif d == 'U':
            y_delta = 1
        elif d == 'D':
            y_delta = -1
        for _ in range(l):
            pointer = (pointer[0]+x_delta, pointer[1]+y_delta)
            coords.append(pointer)
    return coords


def min_steps(w1 , w2):
    c1 = transform_wire_to_coordinates_list(w1)
    c2 = transform_wire_to_coordinates_list(w2)
    cross = set(c1) & set(c2)
    return min([c1.index(c) + c2.index(c) for c in cross]) + 2
    
    
    
                     
assert  min_steps('R75,D30,R83,U83,L12,D49,R71,U7,L72',
                     'U62,R66,U55,R34,D71,R55,D58,R83') == 610
assert  min_steps('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                     'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7') == 410

