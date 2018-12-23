import numpy as np
# the data for part1 and part2 differ, part1 is commented out and marked

#pre_recipe_count = 702831 part 1
sought_recipes = [7, 0, 2, 8, 3, 1]
checked_scores = len(sought_recipes)
recipes = [3, 7]
elves = [
    [0, 3],
    [1, 7]
]
elves = np.array(elves)# current recipe

found = False
start_index = 0
while not found:  # len(recipes) <= pre_recipe_count + checked_scores: part 1
    nr_score = elves[:, 1].sum()
    if len(str(nr_score)) == 2:
        nr_score = [nr_score//10, nr_score%10]
    else:
        nr_score = [nr_score]
    recipes.extend(nr_score)
    # part 2
    if len(recipes) > checked_scores-1:  # need at least 6 recipes
        while start_index <= len(recipes)-checked_scores:
            if recipes[start_index:start_index+checked_scores] == sought_recipes:
                found = True
                break
            else:
                start_index += 1
    if found:
        break
    for i in range(2):
        new_index = (elves[i, :].sum() + 1) % len(recipes)
        elves[i, 0] = new_index
        elves[i, 1] = recipes[new_index]


#print(recipes[pre_recipe_count:pre_recipe_count+checked_scores]) part 1
print(start_index)
