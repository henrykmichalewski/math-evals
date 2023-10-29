"""
This file contains a Python prompt and a template to compose solutions 
to math problems.

The PYTHON_PROMPT string includes an introduction comment that explains 
the tasks, followed by a function stub for user's solution.
"""


PYTHON_PROMPT = '''# Language: Python 3
# Task: Synthesize function to solve the problem

"""
Contains maths exercises formulated in doc-strings of functions.
Solutions are written in simple python code and with a lot of comments
that explain what is done and why and how it is related to the specification.
"""

def exercise1():
    """
    There are 15 trees in the grove. Grove workers will plant trees in the grove today.
    After they are done, there will be 21 trees. How many trees did the grove workers plant today?
    """
    original_trees = 15
    final_trees = 21
    # Number of trees planted = final trees - original trees
    trees_planted = final_trees - original_trees
    return trees_planted

def exercise2():
    """
    If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
    """
    original_cars = 3
    new_cars = 2
    # Total cars = original cars + new cars
    total_cars = original_cars + new_cars
    return total_cars

def exercise3():
    """
    Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
    """
    leah_chocolates = 32
    sister_chocolates = 42
    chocolates_eaten = 35
    # Total chocolates before eating = leah's + sister's chocolates
    total_chocolates = leah_chocolates + sister_chocolates
    # Chocolates left after eating = total chocolates - chocolates eaten
    chocolates_left = total_chocolates - chocolates_eaten
    return chocolates_left

def exercise4():
    """
    Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops.
    How many lollipops did Jason give to Denny?
    """
    original_lollipops = 20
    lollipops_left = 12
    # Lollipops given to Denny = original lollipops - lollipops left
    lollipops_given = original_lollipops - lollipops_left
    return lollipops_given

def exercise5():
    """
    Shawn has five toys. For Christmas, he got two toys each from his mom and dad.
    How many toys does he have now?
    """
    original_toys = 5
    toys_from_mom = 2
    toys_from_dad = 2
    # Total toys after Christmas = original toys + toys from mom + toys from dad
    total_toys = original_toys + toys_from_mom + toys_from_dad
    return total_toys

def exercise6():
    """
    There were nine computers in the server room. Five more computers were installed each day,
    from monday to thursday. How many computers are now in the server room?
    """
    original_computers = 9
    daily_new_computers = 5
    days = 4
    # Total new computers added = daily new computers * number of days
    total_new_computers = daily_new_computers * days
    # Total computers after addition = original computers + total new computers
    total_computers = original_computers + total_new_computers
    return total_computers

def exercise7():
    """
    Michael had 58 golf balls. On tuesday, he lost 23 golf balls.
    On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
    """
    original_balls = 58
    balls_lost_tuesday = 23
    balls_lost_wednesday = 2
    # Golf balls left after losing on Tuesday = original balls - balls lost on Tuesday
    balls_after_tuesday = original_balls - balls_lost_tuesday
    # Golf balls left after losing on Wednesday = balls after Tuesday - balls lost on Wednesday
    balls_after_wednesday = balls_after_tuesday - balls_lost_wednesday
    return balls_after_wednesday

def exercise8():
    """
    Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
    """
    original_money = 23
    bagels_count = 5
    bagel_price = 3
    # Total amount spent on bagels = number of bagels * price per bagel
    bagels_cost = bagels_count * bagel_price
    # Money left after buying bagels = original money - bagels cost
    money_left = original_money - bagels_cost
    return money_left
'''

PYTHON_TEMPLATE = '''
def exercise9():
    """
    {question}
    """
'''
