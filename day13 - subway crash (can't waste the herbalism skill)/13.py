# straight | -
# curve \ /  connect perpendicular, exactly two paths
# intersection +
# moving one by one, line by line, left to right (basic loop - a tick)
# each cart movement I have to check if it collided with another
# collision - X

class Cart:
    def __init__(self, location, direction):
        #self.symbol = symbol  # ??
        self.location = location  # list x, y
        self.direction = direction  # 0 up 1 right 2 down 3 left
        self.turn = -1  # 0 forward +1 right -1 left
        self.active = True  # False if crashed

    def move(self):
        d = self.direction
        # x
        if d == 3:
            self.location[0] -= 1
        elif d == 1:
            self.location[0] += 1
        # y
        elif d == 0:
            self.location[1] -= 1
        elif d == 2:
            self.location[1] += 1

    def intersection(self):
        """Called when an intersection is reached"""
        new_turn = (self.turn + 2) % 3 - 1
        self.direction = (self.direction + self.turn) % 4
        self.turn = new_turn
        # self.change_symbol()

    def rotate_curve(self, track_symbol):
        d = self.direction
        if track_symbol == "/":
            if d == 0 or d == 2:
                self.direction += 1
            elif d == 1 or d == 3:
                self.direction -= 1
        else:  # \
            if d == 0 or d == 2:
                self.direction -= 1
            elif d == 1 or d == 3:
                self.direction += 1
            self.direction = self.direction % 4
        # self.change_symbol()

    """def change_symbol(self):
        d = self.direction
        if d == 0:
            self.symbol = "^"
        elif d == 1:
            self.symbol = ">"
        elif d == 2:
            self.symbol = "v"
        else:
            self.symbol = "<" """

    def crashed(self):
        self.active = False

    def __lt__(self, other):
        comes_before = False
        if self.location[1] < other.location[1]:  # row above
            comes_before = True
        elif self.location[0] < other.location[0] and self.location[1] == other.location[1]:
            # same row, but earlier on
            comes_before = True
        return comes_before

    def __repr__(self):
        return str(self.location)


subway = []
carts = []
cart_loc = set()
i = 0
while True:
    line = input()
    if line == "":
        break
    subset = []
    j = 0
    for l in line:
        subset.append(l)
        cart = None
        location = [j, i]
        if l == "^":
            cart = Cart(location, 0)
        elif l == ">":
            cart = Cart(location, 1)
        elif l == "v":
            cart = Cart(location, 2)
        elif l == "<":
            cart = Cart(location, 3)
        if cart != None:
            carts.append(cart)
            cart_loc |= {tuple(location)}
        j += 1
    subway.append(subset)
    i += 1

for cart in carts:
    x = cart.location[0]
    y = cart.location[1]
    if cart.direction in [0, 2]:
        symbol = "|"
    else:
        symbol = "-"
    subway[y][x] = symbol
    

print("Read the map. Now to simulate...")
print("Oh, and, you have", len(carts), "carts!")

#crash = False
#crash_site = None
crashed = set()
while len(crashed) < len(carts) - 1:  # not crash
    carts.sort()
    #print(" ")
    crash_loc = set()
    for cart in carts:
        if not cart.active:
            continue
        loc = tuple(cart.location)
        cart_loc -= {loc}

        cart.move()
        loc = tuple(cart.location)
        #print(cart.location, cart.direction, end=" ")
        if loc in cart_loc or loc in crash_loc:
            cart.crashed()
            crashed |= {cart}
            # look for the other one(s)
            for cart2 in carts:
                if cart2.location == list(loc) and cart2.active:
                    cart2.crashed()
                    crashed |= {cart2}
            crash_loc |= {loc}
            #crash_site = cart.location
            #crash = True
            #break
        else:
            cart_loc |= {loc}
        
        symbol = subway[cart.location[1]][cart.location[0]]
        #print("Symbol", symbol)
        if symbol != "-" and symbol != "|":
            if symbol == "+":
                # intersection
                cart.intersection()
            else:
                cart.rotate_curve(symbol)
            #print("   New dir", cart.direction)
    cart_loc -= crash_loc


#print("First crash: " + str(crash_site))
print("Survivor:", set(carts) - crashed, cart_loc)
