# inches!
# #ID @ left,top: widthxheight

original_w = 1000
original_h = 1000
fabric = [["." for i in range(original_w)] for j in range(original_h)]
squares = []

while True:
    square = input()

    if square == "":
        break
    else:
        square = square.split(" ")
    
    square_id = square[0][1:]   # without the hash
    
    margins = square[2].split(",")  # @ is skipped, result is list of str
    margins[1] = margins[1][0:len(margins[1])-1]
    
    size = square[3].split("x")

    # actual values
    square_l = int(margins[0])
    square_t = int(margins[1])
    square_w = int(size[0])
    square_h = int(size[1])

    square = (square_id, square_t, square_l, square_h, square_w)

    squares.append(square)

    # marking the fabric
    first_index = (square_t, square_l)    # row, line
    for i in range(first_index[0], first_index[0] + square_h):
        for j in range(first_index[1], first_index[1] + square_w):
            if fabric[i][j] == ".":
                fabric[i][j] = square_id
            else:
                fabric[i][j] = "X"

for square in squares:
    full = True
    for i in range(square[1], square[1]+square[3]):
        for j in range(square[2], square[2]+square[4]):
            if fabric[i][j] == "X":
                full = False
                break
        if not full:
            break
    if full:
        full = square[0]
        break

print("Full ID: " + full)
