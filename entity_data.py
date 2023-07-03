
from random import randint, choice

#-----Data Set Function for Assessing Your Solution------------------#
#
# The function in this module generates the data sets that will be
# used to assess your solution.
#
# Do NOT change any of the code in this module.  Do NOT submit a copy
# of this module with your solution - we will use our own copy to
# assess your code.
#
# The following function creates a random data set defining the
# overall image to draw.  Your program must work for ANY data set that
# can be produced by this function.  The results returned by calling
# this function will be used as the argument to your data visualisation
# function during marking.  For convenience during code development
# and marking this function also prints the data set generated to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
def entity_actions(width = 1, height = 1):

    # Define the entities
    entities = ['Left entity', 'Right entity']
    # Define the possible entity states, biased towards
    # being healthy
    statuses = ['Healthy', 'Healthy', 'Unwell']
    # Define the ways the two entities can move,
    # biasing them to move towards the opposite side
    # of the grid
    directions_0 = ['East', 'East', 'North', 'South']
    directions_1 = ['West', 'West', 'North', 'South']
    # Choose the total number of entity actions
    # (in addition to the 'initial states' action)
    num_actions = randint(0, 25)

    # Initialise the data set with the health status of both entities
    actions = [[choice(statuses), choice(statuses)]]

    # Create the individual steps
    for step in range(0, num_actions):
        # Choose which entity wants to move
        entity = choice(entities)
        # Choose which way the entity wants to move
        if entity == entities[0]:
            direction = choice(directions_0)
        else:
            direction = choice(directions_1)
        # Choose the number of cells the entity wants to move
        # (ignoring the limitations on their ability to do so)
        if direction in ['North', 'South']:
            num_cells = randint(1, height // 3)
        else:
            num_cells = randint(1, width // 2)
        # Add the chosen action to the data set
        actions.append([entity, direction, num_cells])

    # Print the whole data set to the shell window, laid out
    # so that it's easy to distinguish the actions attempted by
    # the two entities
    print('The entity actions to visualise are as follows:\n')
    print(str(actions).replace('],', '],\n').replace("['Right", "  ['Right"))
    # Return the data set to the caller
    return actions

#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
# Some "fixed" data sets
#
# Developing code when the underlying data set changes randomly can
# be difficult.  To help you develop your code you can temporarily
# provide the call to the "actions" function defined in the
# assignment template file with a "seed" value which will force it to
# produce a known data set.
#
# To do so, just put the seed value in the call to "actions" as
# its argument.  Of course, having completed your solution, your
# program must work for any list that can be returned by calling
# "actions" with no argument.
#
# Some examples of useful seeds follow.  Note that the following
# descriptions all assume that the grid has its default width and
# height (different behaviours will be created if the grid's size
# is changed). Let RHS mean "right-hand side" and LHS mean "left-
# hand side". Seeds marked "+" were used in the client's briefing.
#
# Each of the following seeds produces actions in which the
# entities do not attempt to leave the grid and do not cross
# into the other entity's half of the grid.
#
# Seed 31: Neither entity moves and both are healthy
# Seed 139: Neither entity moves and both are unwell
# Seed 165: Neither entity moves and the right one is unwell +
# Seed 2: Only the right entity moves
# Seed 137: Only the right entity moves
# Seed 49: Only the left entity moves
# Seed 57: Only the left entity moves +
# Seed 21: Both entities move but stay in their own half
# Seed 70: Both entities move but stay near home
# Seed 79: Both entities move close to the halfway point
#
# Each of the following seeds produces actions in which the
# entities attempt to escape from the grid, but still stay on
# their own side.
#
# Seed 18: Left entity attempts to escape from bottom of grid +
# Seed 67: Right entity attempts to escape from bottom of grid
# Seed 87: Left entity attempts to escape from top of grid
# Seed 184: Left entity attempts to escape from top of grid +
#
# Each of the following seeds produces actions in which the
# entities attempt to escape from the opposite side of the grid.
#
# Seed 44: Left entity attempts to escape from grid's right side
#          and right entity attempts to escape from grid's
#          left side
# Seed 58: Both attempt to escape from opposite sides of grid +
#
# Each of the following seeds produce actions in which the
# entities wander all over the grid but do not change their
# health status.
#
# Seed 16: Both entities are well and go into the other entity's half +
# Seed 3: Both entities are sick and wander far from home +
# Seed 17: Both entities are well and go into the other entity's half
# Seed 10: Both entities are well and visit the other entity's home
# Seed 53: Entities swap sides but both remain well
#
# Each of the following seeds produces actions in which a healthy
# entity becomes infected by crossing into the half of
# the grid where a sick entity lives.
#
# Seed 15: Left entity goes one cell into RHS and gets sick
# Seed 9: Right entity crosses into LHS and gets sick
# Seed 12: Left entity crosses into RHS and gets sick +
# Seed 26: Left entity crosses into RHS and gets sick
# Seed 20: Right entity crosses into LHS and gets sick +
#
# Of course, you are free to choose other seed values to help you debug
# your code.
#
#--------------------------------------------------------------------#
