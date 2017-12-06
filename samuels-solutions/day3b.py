import sys


def getValue(x, y):
    if x in (0, 1) and y == 0:  # Starting Points (0,0) & (1,0)
        return 1
    if abs(x) == abs(y):    # Handle corners
        if x > 0 and y > 0:   # CORNER RIGHT-UP = LEFT-DOWN + DOWN
            val = getValue(x - 1, y - 1) + getValue(x, y - 1)
        elif x < 0 and y > 0:   # CORNER LEFT-UP = RIGHT-DOWN + RIGHT
            val = getValue(x + 1, y - 1) + getValue(x + 1, y)
        elif x < 0 and y < 0:   # CORNER LEFT-DOWN = RIGHT-UP + UP
            val = getValue(x + 1, y + 1) + getValue(x, y + 1)
        elif x > 0 and y < 0:   # CORNER RIGHT-DOWN = LEFT UP + LEFT + UP
            val = getValue(x - 1, y + 1) + \
                getValue(x - 1, y) + getValue(x, y + 1)
    else:
        if x > 1 and abs(x + y) == 1 and abs(x) > abs(y):   # Start of next spiral
            val = getValue(x - 1, y + 1) + getValue(x - 1, y)
        elif x > 1 and x > y and abs(x) > abs(y):
            if x - y == 1:  # Prepare for CORNER RIGHT-UP
                val = getValue(x, y - 1) + getValue(x - 1, y - 1) + \
                    getValue(x - 1, y)
            else:   # Move UP
                val = getValue(x, y - 1) + getValue(x - 1, y - 1) + \
                    getValue(x - 1, y) + getValue(x - 1, y + 1)
        elif y > 0 and x + y > 1:       # Move LEFT
            val = getValue(x + 1, y) + getValue(x + 1, y - 1) + \
                getValue(x, y - 1) + getValue(x - 1, y - 1)
        elif y > 0 and x + y == 1:      # Prepare for CORNER LEFT-UP
            val = getValue(x + 1, y) + getValue(x + 1, y - 1) + \
                getValue(x, y - 1)
        elif x < 0 and x - y < -1:      # Move DOWN
            val = getValue(x, y + 1) + getValue(x + 1, y + 1) + \
                getValue(x + 1, y) + getValue(x + 1, y - 1)
        elif x < 0 and x - y == -1:     # Prepare for CORNER LEFT-DOWN
            val = getValue(x, y + 1) + getValue(x + 1, y + 1) + \
                getValue(x + 1, y)
        elif y < 0 and x + y < 0:                     # Move RIGHT
            val = getValue(x - 1, y) + getValue(x - 1, y + 1) + \
                getValue(x, y + 1) + getValue(x + 1, y + 1)
    return val


print(getValue(int(sys.argv[1]), int(sys.argv[2])))
