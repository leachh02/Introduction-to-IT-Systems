
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 2, 2021.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 11039639 # put your student number here as an integer
student_name   = 'Harrison Leach' # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  LOCKDOWN
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "track_entities".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various symbols, using data stored in a list to
#  determine which symbols to draw and where.  See the various
#  "client briefings" in Blackboard for full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by the client.
#  This single template file will be used for all parts and you will
#  submit your final solution as a single Python 3 file only, whether
#  or not you complete all requirements for the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You must NOT change
# any of the code in this section.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless
# instructed.
cell_size = 100 # pixels (default is 100)
grid_width = 8 # squares (default is 8)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.5 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 5, 'normal') # font for the coords
big_font = ('Arial', cell_size // 4, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 7, 'Grid must be at least 7 squares wide'
assert (grid_height >= 5) and (grid_height % 2 != 0), \
       'Grid must be at least 5 squares high and height must be odd'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          label_spaces = True): # NO! DON'T CHANGE THIS!
    
    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(str(x_label + 1), align = 'right', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 5, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(chr(y_label + ord('A')), align = 'center', font = small_font)

        # Mark the two "special" cells
        goto(-cell_size * grid_width // 2 + 0.5 * cell_size, 0)
        dot(cell_size // 6)
        goto(cell_size * grid_width // 2 - 0.5 * cell_size, 0)
        dot(cell_size // 6)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1.15) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ntwo states of\nyour first\nentity here', align = 'right', font = big_font)    
        # Right side
        goto(((grid_width + 1.15) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ntwo states of\nyour second\nentity here', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "track_entities" function.  ALL of your solution code
#  must appear in, or be called from, function "track_entities".  Do
#  NOT put any of your code in other parts of the program and do NOT
#  change any of the provided code except as allowed in the main
#  program below.
#

# All of your code goes in, or is called from, this function
def track_entities(actions):
        #first image
    def superman_well(super_well_x, super_well_y):
        #turtle is on default seetings
        width(1)
        setheading(0)
        color('black')
        #given postion
        superman_x_pos_well = super_well_x
        superman_y_pos_well = super_well_y

        penup()
        #goto set position
        goto(superman_x_pos_well-50,superman_y_pos_well)
        #drawing 100x100 square
        pendown()
        fillcolor('light sky blue')
        begin_fill()
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        end_fill()

        #establish body size variable, this was done thinking scale would be a
        #factor but as they're in 100x100 it probably isn't relevant so it wasn't repeated for the other images
        body_size = 48

        #Draws a red cape before superman's body
        penup()
        goto(superman_x_pos_well,body_size*1.1+superman_y_pos_well)
        setheading(180)
        pendown()
        color('red')
        begin_fill()
        circle(body_size,extent=90)
        end_fill()
        penup()
        goto(superman_x_pos_well,body_size*1.1+superman_y_pos_well)
        setheading(0)
        pendown()
        begin_fill()
        circle(-body_size,extent=90)
        end_fill()
        penup()

        goto(body_size+superman_x_pos_well,body_size+superman_y_pos_well)

        #drawing body
        color('blue')
        forward(body_size)
        setheading(90)
        pendown()
        begin_fill()
        circle(body_size, extent = 180)
        end_fill()

        #drawing hair
        penup()
        color('black')
        hair_size = body_size * 0.53
        goto(hair_size+superman_x_pos_well,body_size *1.3+superman_y_pos_well)
        pendown()
        setheading(90)
        begin_fill()
        circle(hair_size, extent = 180)
        setheading(0)
        forward(hair_size * 2)
        end_fill()

        #drawing head
        color('blanched almond')
        penup()
        head_size = body_size * 0.5
        goto(superman_x_pos_well,(body_size*0.7)+superman_y_pos_well)
        setheading(0)
        pendown()
        begin_fill()
        circle(head_size)
        end_fill()
        penup()

        #drawing curl, got inspiration off ying yang exercise to make the curl
        goto(superman_x_pos_well,(body_size*1.3)+ hair_size-6+superman_y_pos_well)
        color('black')
        curl_size = hair_size*0.25
        pendown()
        setheading(-70)
        begin_fill()
        circle(-curl_size,extent = 180)
        setheading(-45)
        circle(curl_size,extent = 145)
        end_fill()
        penup()

        #drawing eyes
        goto(-0.25*head_size+superman_x_pos_well,1.8*head_size+superman_y_pos_well)
        setheading(325)
        pendown()
        circle(head_size*0.3,extent = 100)
        penup()
        setheading(75)
        forward(head_size* 0.75)
        eye_size = 0.2*head_size
        dot(eye_size*1.4)
        color('white')
        dot(eye_size)
        color('light blue')
        dot(eye_size*0.8)
        setheading(180)
        forward(head_size*0.75)
        color('black')
        dot(eye_size*1.4)
        color('white')
        dot(eye_size)
        color('light blue')
        dot(eye_size*0.8)
        #now moves to draw eyebrow
        setheading(35)
        forward(eye_size*1.1)
        pendown()
        setheading(90)
        color('black')
        circle(eye_size, extent = 180)
        penup()
        setheading(0)
        forward(head_size)
        setheading(10)
        forward(eye_size)
        pendown()
        setheading(90)
        color('black')
        circle(eye_size, extent = 180)
        penup()
        setheading(235)
        forward(head_size*0.4)
        setheading(245)
        pendown()
        forward(head_size/3)
        setheading(0)
        forward(head_size*0.2)
        penup()

        #superman crest
        #essentially a yellow triangle with thick red outline
        goto(superman_x_pos_well,superman_y_pos_well+5)
        fillcolor('yellow')
        pencolor('red')
        begin_fill()
        pendown()
        setheading(45)
        forward(35)
        setheading(180)
        forward(70 * cos(pi/4))
        setheading(315)
        forward(35)
        end_fill()
        penup()
        goto(superman_x_pos_well-5,superman_y_pos_well+10)
        pendown()
        width(3)
        setheading(-40)
        circle(5, extent = 200)
        circle(-5, extent = 200)
        penup()

        #hooking cape onto superman
        color('red')
        goto(superman_x_pos_well+body_size*0.5,superman_y_pos_well + body_size*0.85)
        dot(body_size*0.2)
        goto(superman_x_pos_well-body_size*0.5,superman_y_pos_well + body_size*0.85)
        dot(body_size*0.2)

    
    #second image
    def superman_unwell(super_unwell_x, super_unwell_y):
        #default
        width(1)
        setheading(0)
        color('black')
        #given postion
        superman_x_pos_unwell = super_unwell_x
        superman_y_pos_unwell = super_unwell_y

        penup()
        goto(superman_x_pos_unwell-50,superman_y_pos_unwell)
        #create square
        pendown()
        fillcolor('dark gray')
        begin_fill()
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        end_fill()
        penup()

        #function for cracks on the floor, they don't look amazing but they sort of look like cracks 

        def floor_cracks(x_pos,y_pos,heading):
            goto(x_pos+superman_x_pos_unwell,y_pos+superman_y_pos_unwell)
            setheading(heading)
            color('black')
            pendown()
            forward(6)
            left(30)
            forward(7)
            right(40)
            forward(4)
            left(20)
            forward(8)
            right(20)
            forward(6)
            penup()

        floor_cracks(-30,70,115)
        floor_cracks(-30,20,20)
        floor_cracks(0,86,180)
        floor_cracks(-15,5,130)
        floor_cracks(40,60,95)

        #cape
        penup()
        goto(superman_x_pos_unwell+50,superman_y_pos_unwell+53)
        setheading(180)
        pendown()
        fillcolor('red')
        begin_fill()
        circle(53, extent = 90)
        setheading(0)
        forward(50)
        end_fill()
        penup()

        #drawing body
        penup()
        goto(superman_x_pos_unwell+50,superman_y_pos_unwell+50)
        setheading(180)
        pendown()
        fillcolor('blue')
        begin_fill()
        circle(50, extent = 90)
        setheading(0)
        forward(50)
        end_fill()
        penup()

        #Hair before head
        goto(superman_x_pos_unwell + 18, superman_y_pos_unwell+69)
        setheading(130)
        color('black')
        pendown()
        begin_fill()
        circle(26,extent = 180)
        end_fill()
        penup()

        #head
        goto(superman_x_pos_unwell,superman_y_pos_unwell+50)
        color('blanched almond')
        dot(50)

        #Symbol
        goto(superman_x_pos_unwell+45,superman_y_pos_unwell+5)
        fillcolor('yellow')
        pencolor('red')
        begin_fill()
        pendown()
        setheading(45+45)
        forward(35)
        setheading(180+45)
        forward(70 * cos(pi/4))
        setheading(315+45)
        forward(35)
        end_fill()
        penup()
        goto(superman_x_pos_unwell+38,superman_y_pos_unwell+5)
        pendown()
        width(3)
        setheading(-40+45)
        circle(5, extent = 200)
        circle(-5, extent = 200)
        penup()


        #frowning smile and nose
        goto(superman_x_pos_unwell+21,superman_y_pos_unwell+42)
        color('black')
        setheading(130)
        pendown()
        begin_fill()
        circle(8,extent = 180)
        end_fill()
        penup()
        width(1)
        setheading(120)
        forward(25)
        pendown()
        setheading(290)
        forward(10)
        setheading(45)
        forward(5)
        penup()

        #black eye
        setheading(100)
        forward(15)
        color('purple')
        dot(11)
        color('black')
        dot(7)
        color('white')
        dot(5)
        color('deep sky blue')
        dot(3)
        setheading(220)
        forward(17)
        color('black')
        dot(7)
        color('white')
        dot(5)
        color('deep sky blue')
        dot(3)

        #eye brows
        setheading(210)
        forward(5)
        setheading(135)
        color('black')
        pendown()
        circle(-4,extent = 180)
        penup()
        setheading(50)
        forward(10)
        pendown()
        setheading(135)
        circle(-4,extent = 180)
        penup()

        #curl
        goto(superman_x_pos_unwell-15,69+superman_y_pos_unwell)
        color('black')
        pendown()
        setheading(0)
        begin_fill()
        circle(-5,extent = 180)
        setheading(35)
        circle(5,extent = 145)
        end_fill()
        penup()

        #hook cape on body
        goto(superman_x_pos_unwell+35,superman_y_pos_unwell+47)
        color('red')
        dot(7)
        goto(superman_x_pos_unwell+3,superman_y_pos_unwell+14)
        dot(7)


    #third image
    def flash_well(flash_well_x, flash_well_y):
        #default
        width(1)
        setheading(0)
        color('black')
        #functions for lightning further on

        def lighting_out(light_color):
            color(light_color)
            forward(6)
            pendown()
            setheading(135)
            forward(5)
            setheading(225)
            forward(5)
            setheading(135)
            forward(5)
            setheading(225)
            forward(5)
            setheading(135)
            forward(5)
            setheading(225)
            forward(5)
            setheading(135)
            forward(5)
            setheading(225)
            forward(5)
        #zig-zagging in and zig-zagging out basically

        def lightning_in(light_color):
            setheading(50)
            penup()
            forward(6)
            color(light_color)
            pendown()
            setheading(45)
            forward(5)
            setheading(315)
            forward(5)
            setheading(45)
            forward(5)
            setheading(315)
            forward(5)
            setheading(45)
            forward(5)
            setheading(315)
            forward(5)
            setheading(45)
            forward(5)
            setheading(315)
            forward(5)
            penup()
            setheading(110)

        #given postion
        flash_x_pos_well = flash_well_x
        flash_y_pos_well = flash_well_y

        penup()
        goto(flash_x_pos_well-50,flash_y_pos_well)
        #square
        pendown()
        fillcolor('lawn green')
        begin_fill()
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        end_fill()
        penup()

        #only other time a itried using scale but this variable was eused very minimalistically 
        flash_body_size = 50

        #flash's body
        goto(flash_x_pos_well-5,flash_y_pos_well)
        setheading(60)
        pendown()
        color('red')
        begin_fill()
        forward(flash_body_size)
        circle(flash_body_size*0.25,extent=180)
        forward(flash_body_size+13)
        end_fill()
        penup()

        #flash's arms
        goto(flash_x_pos_well+5,flash_y_pos_well+flash_body_size*0.8)
        setheading(290)
        width(10)
        pendown()
        forward(25)
        setheading(35)
        forward(30)
        penup()
        setheading(160)
        forward(flash_body_size)
        setheading(145)
        pendown()
        circle(flash_body_size*0.5, extent = 60)
        penup()

        #flash's head
        head_size = 40
        goto(flash_x_pos_well+17,flash_y_pos_well+flash_body_size*1.3)
        dot(head_size)
        setheading(340)
        color('blanched almond')
        width(1)
        pendown()
        begin_fill()
        forward(head_size/2)
        setheading(250)
        circle(-head_size/2, extent = 40)
        goto(flash_x_pos_well+17,flash_y_pos_well+flash_body_size*1.3)
        end_fill()
        penup()
        setheading(0)
        forward(head_size*0.25)
        setheading(45)
        pendown()
        begin_fill()
        forward(head_size*0.3)
        setheading(180)
        forward(head_size*0.3)
        setheading(285)
        forward(head_size*0.25)
        end_fill()
        penup()
        #flash masks lightning 'ears'
        setheading(145)
        forward(head_size*0.3)
        width(3)
        color('yellow')
        pendown()
        setheading(165)
        forward(20)
        setheading(300)
        forward(10)
        setheading(165)
        forward(33)
        penup()



        #Face
        setheading(355)
        forward(head_size*1.5)
        color('black')
        dot(head_size*0.17)
        color('white')
        dot(head_size*0.12)
        color('light sky blue')
        forward(0.7)
        setheading(90)
        forward(0.5)
        dot(head_size*0.07)
        setheading(25)
        forward(3)
        setheading(135)
        color('black')
        width(1.5)
        pendown()
        forward(head_size*0.23)
        penup()
        setheading(270)
        forward(head_size*0.5)
        setheading(285)
        pendown()
        circle(head_size*0.25,extent = 40)
        penup()

        #logo
        goto(0+flash_x_pos_well,flash_body_size*0.6+flash_y_pos_well)
        dot(25)
        color('light gray')
        dot(23)
        setheading(60)
        forward(15)
        pendown()
        color('yellow')
        setheading(240)
        forward(18)
        setheading(35)
        forward(8)
        setheading(240)
        forward(18)
        penup()

        #using the lighting functions from before
        goto(-flash_body_size*0.35+flash_x_pos_well,15+flash_y_pos_well)
        lighting_out('orange')
        lightning_in('yellow')
        lighting_out('red')
        lightning_in('yellow')
        lighting_out('red')
        lightning_in('orange')


    #fourth image
    def flash_unwell(flash_unwell_x, flash_unwell_y):
        #default, to not mess with colouring and angles
        width(1)
        setheading(0)
        color('black')
        #given postion
        flash_x_pos_unwell = flash_unwell_x
        flash_y_pos_unwell = flash_unwell_y

        penup()
        goto(flash_x_pos_unwell-50,flash_y_pos_unwell)
        #square
        pendown()
        fillcolor('medium violet red')
        begin_fill()
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        end_fill()
        penup()

        #body
        fillcolor('red')
        begin_fill()
        goto(flash_x_pos_unwell+45,flash_y_pos_unwell)
        pendown()
        setheading(90)
        circle(45,extent = 180)
        end_fill()
        penup()

        #Head
        goto(flash_x_pos_unwell-12,flash_y_pos_unwell+7)
        begin_fill()
        pendown()
        setheading(0)
        forward(28)
        setheading(50)
        forward(30)
        setheading(90)
        forward(35)
        setheading(90)
        circle(14+(30*cos(50*pi/180)), extent = 180)
        setheading(270)
        forward(35)
        setheading(310)
        forward(30)
        end_fill()
        penup()

        #ears
        goto(14+(30*cos(50*pi/180))+flash_x_pos_unwell,flash_y_pos_unwell+50)
        pendown()
        color('yellow')
        width(5)
        setheading(65)
        forward(12)
        setheading(220)
        forward(8)
        setheading(65)
        forward(20)
        penup()
        goto(-(12+(30*cos(50*pi/180)))+flash_x_pos_unwell,flash_y_pos_unwell+50)
        pendown()
        color('yellow')
        width(5)
        setheading(115)
        forward(12)
        setheading(320)
        forward(8)
        setheading(115)
        forward(20)
        penup()

        #detailing the mask
        goto(flash_x_pos_unwell-12,flash_y_pos_unwell+13)
        color('black')
        width(1)
        fillcolor('navajo white')
        begin_fill()
        pendown()
        setheading(0)
        forward(28)
        setheading(50)
        forward(20)
        setheading(90)
        circle(14+(20*cos(50*pi/180)), extent = 180)
        setheading(310)
        forward(20)
        end_fill()
        penup()
        #shocked mouth
        setheading(40)
        forward(25)
        dot(20,'black')
        setheading(100)
        forward(30)
        pendown()
        setheading(255)
        forward(15)
        setheading(0)
        forward(5)

        #eyeslots
        penup()
        eyeslot_size = 25
        fillcolor('navajo white')
        begin_fill()
        setheading(65)
        forward(20)
        pendown()
        setheading(45)
        forward(eyeslot_size)
        setheading(180)
        forward(eyeslot_size*cos(pi/4))
        setheading(270)
        forward(eyeslot_size*sin(pi/4))
        end_fill()
        penup()
        setheading(180)
        forward(16)
        pendown()
        begin_fill()
        setheading(135)
        forward(eyeslot_size)
        setheading(0)
        forward(eyeslot_size*cos(pi/4))
        setheading(270)
        forward(eyeslot_size*sin(pi/4))
        end_fill()
        penup()

        #eyes
        setheading(110)
        forward(12)
        dot(14)
        color('white')
        dot(12)
        color('light blue')
        dot(8)
        setheading(0)
        forward(27)
        color('black')
        dot(14)
        color('white')
        dot(12)
        color('light blue')
        dot(8)
        # eye brows
        forward(10)
        color('black')
        pendown()
        setheading(90)
        circle(10, extent = 180)
        penup()
        setheading(180)
        forward(8)
        pendown()
        setheading(90)
        circle(10, extent = 180)
        penup()
 

    #using the functions to draw for legend
    superman_well(-550,150)
    superman_unwell(-550,-200)
    flash_well(550,150)
    flash_unwell(550,-200)

    #adding in captions for heroes
    goto(-465, 30)
    write("He's A \nSymbol\nOf Hope!", align = 'right', font = big_font)
    goto(-440, -320)
    write("It's Worse \nThan \nKryptonite!", align = 'right', font = big_font) 
    goto(630, 50)
    write("The Fastest \nMan Alive!", align = 'right', font = big_font)
    goto(630, -300)
    write("Not So \nFast Flash!", align = 'right', font = big_font)
    goto(-470, 255)
    write("Superman", align = 'right', font = big_font)
    goto(590, 250)
    write("Flash", align = 'right', font = big_font)


    #establishing common variables
    left_home_x = -350
    left_home_y = -50
    right_home_x = 350
    right_home_y = -50


    superman_current_pos_x = left_home_x
    superman_current_pos_y = left_home_y
    flash_current_pos_x = right_home_x
    flash_current_pos_y = right_home_y

    #draw healthy or unhealthy at home
    if actions[0][0] == 'Healthy':
        superman_well(left_home_x,left_home_y)
        superman_health_status = 'Healthy'
    else:
        superman_unwell(left_home_x,left_home_y)
        superman_health_status = 'Unwell'
        
    if actions[0][1] == 'Healthy':
        flash_well(right_home_x,right_home_y)
        flash_health_status = 'Healthy'
    else:
        flash_unwell(right_home_x,right_home_y)
        flash_health_status = 'Unwell'
        
    #Listen to directions moving through grids


    #Which entity does it relate to
    
    #loops through given instructions
    for instruction in actions[1:]:
        #Supermans direction
        if instruction[0] == 'Left entity':
            
            if instruction[1] == 'North':
                #now move according to direction and magnitude given in instructions
                for steps in range(instruction[2]):


                    #has superman gone past the northern limit
                    if superman_current_pos_y >= 250:
                        pass
                    else:
                    #changing current position every time
                        superman_current_pos_y += 100

                    #depending on if superman is healthy or not
                    if superman_health_status == 'Healthy':
                        superman_well(superman_current_pos_x,superman_current_pos_y)
                    else:
                        superman_unwell(superman_current_pos_x,superman_current_pos_y)

                            
            elif instruction[1] == 'South':
                #now move according to direction and magnitude given in instructions
                for steps in range(instruction[2]):
                    #dont allow entities to leave their grid


                    #Checks to see if superman is at his limit to go down
                    if superman_current_pos_y <= -350:
                        pass
                    else:
                    #changing current position every time
                        superman_current_pos_y -= 100

                    #depending on if superman is healthy or not
                    if superman_health_status == 'Healthy':
                        superman_well(superman_current_pos_x,superman_current_pos_y)
                    else:
                        superman_unwell(superman_current_pos_x,superman_current_pos_y)
            else:
                #now moving 100 pixels for each square in grid
                for steps in range(instruction[2]):

                    #Check superman hasn't ventured out too far
                    if flash_health_status == 'Unwell' and superman_current_pos_x >= -50:
                        superman_health_status = 'Unwell'
                    else:
                        pass
                    
                    if superman_current_pos_x >= 350:
                        pass
                    else:
                    #changing current position every time
                        superman_current_pos_x += 100

                    #depending on if superman is healthy or not
                    if superman_health_status == 'Healthy':
                        superman_well(superman_current_pos_x,superman_current_pos_y)
                    else:
                        superman_unwell(superman_current_pos_x,superman_current_pos_y)


        #For the flash
        else:
            if instruction[1] == 'North':
                #now move according to direction and magnitude given in instructions
                for steps in range(instruction[2]):

                    #Check flash doesn't exceed boundaries
                    if flash_current_pos_y >= 250:
                        pass
                    else:
                    #changing current position every time
                        flash_current_pos_y += 100

                    #depending on if flash is healthy or not
                    if flash_health_status == 'Healthy':
                        flash_well(flash_current_pos_x,flash_current_pos_y)
                    else:
                        flash_unwell(flash_current_pos_x,flash_current_pos_y)

                            
            elif instruction[1] == 'South':
                #now move according to direction and magnitude given in instructions
                for steps in range(instruction[2]):


                    if flash_current_pos_y <= -350:
                        pass
                    else:
                    #changing current position every time
                        flash_current_pos_y -= 100

                    #depending on if flash is healthy or not
                    if flash_health_status == 'Healthy':
                        flash_well(flash_current_pos_x,flash_current_pos_y)
                    else:
                        flash_unwell(flash_current_pos_x,flash_current_pos_y)
            else:
                #now moving 100 pixels for each square in grid
                for steps in range(instruction[2]):

                    #Before anything make sure the flash hasn't left his LGA
                    if superman_health_status == 'Unwell' and flash_current_pos_x <= 50:
                        flash_health_status = 'Unwell'
                    else:
                        pass

                    #Checks flash isn't going to escape the grid
                    if flash_current_pos_x <= -350:
                        pass
                    else:
                    #changing current position every time
                        flash_current_pos_x -= 100

                    #depending on if flash is healthy or not
                    if flash_health_status == 'Healthy':
                        flash_well(flash_current_pos_x,flash_current_pos_y)
                    else:
                        flash_unwell(flash_current_pos_x,flash_current_pos_y)
#
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  You
# should NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's data generation function if available, but
### otherwise creating a dummy function that returns an empty
### list
if isfile('entity_data.py'):
    print('\nData module found\n')
    from entity_data import entity_actions
    def actions(new_seed = None):
        seed(new_seed)
        return entity_actions(grid_width, grid_height)
else:
    print('\nNo data module available!\n')
    def actions(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(label_spaces = False)

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
title("DC Superheroes: Flash and Superman!")

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "actions" function with a fixed seed for the
# ***** random number generator, but your final solution must
# ***** work with "actions()" as the argument to "track_entities",
# ***** i.e., for any data set that can be returned by
# ***** calling function "actions" with no seed.
track_entities(actions()) # <-- no argument for "actions" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible when the program
# ***** terminates as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
