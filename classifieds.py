
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



#-----Assignment Description-----------------------------------------#
#
#  Classified Ads
#
#  In this assignment you will combine your knowledge of HTMl/CSS
#  mark-up languages with your skills in Python scripting, pattern
#  matching, databases and Graphical User Interface design to produce
#  a robust, interactive application that allows its user to view
#  and save items currently for sale from multiple online sources.
#
#  See the client's requirements accompanying this file for full
#  details.
#
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#

# Import standard Python 3 modules needed to complete this assignment.
# You should not need to use any modules other than those provided
# in a standard Python 3 installation for your solution.
#
# In particular, you may NOT use any Python modules that need to be
# downloaded and installed separately, such as "Beautiful Soup" or
# "Pillow", because the markers will not have access to such modules
# and will not be able to run your code.  Only modules that are part
# of a standard Python 3 installation may be used.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via the "download" function below.)
from urllib.request import urlopen

# Some standard Tkinter functions.  (You WILL need to use
# SOME of these functions in your solution.)  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label".)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  (You do not necessarily need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  (You WILL need to use this function
# in your solution.)
from webbrowser import open as urldisplay

# All the standard SQLite functions.
from sqlite3 import *

# Confirm that the student has declared their authorship.
# You must NOT change any of the code below.
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

#
#--------------------------------------------------------------------#



#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  (You are not required to use this function, but it may
# save you some effort.)
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                               'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            print("Warning - Request does not reveal client's true identity.")
            print("          This is both unreliable and unethical!")
            print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.

# write websites as variables for simplicity
amazon_vinlys = 'https://www.amazon.com.au/gp/bestsellers/music/5363597051'
ebay_phones = 'https://www.ebay.com.au/b/Mobile-Phones/9355/bn_504059?rt=nc&_sop=10'
dealnews_toys = 'https://www.dealnews.com/c186/Gaming-Toys/?sort=time'


# Establish scollers first state
current_order = 'First'

#functions

#URL Display command
def url_open():
    
    #checks to see the category selected (if any) and then opens up the corresponding url
    try:
        if current_selection == 'Vinyls':
            urldisplay(amazon_vinlys)
        elif current_selection == 'Phones':
            urldisplay(ebay_phones)
        elif current_selection == 'Toys':
            urldisplay(dealnews_toys)
    except NameError:
        #making this application robust
        selection_label2.configure(state='normal')
        selection_label2.delete('1.0', 'end')
        selection_label2.insert('1.0', 'Show Details Error: A category selection must be made first!')
        selection_label2.configure(state='disabled')

def save_sel_clicked():
    #This captures the instance when the user wishes to save the selection

    #gets the three required elements to put into the db
    source = selection_label3['text']
    #gets rid of the, ' to be safe about SQL statement being executed
    description = selection_label2.get('1.0', 'end').strip().replace("'",'')
    item_price = selection_label1['text']
    
    if check_state.get() == 1:
        # connect to the database
        connection = connect(database = 'classifieds.db')
        classifieds_db = connection.cursor()
        # Sql statements
        SQL_Source ="UPDATE current_selection SET Source = '" + source[8:] + "'"
        SQL_Desc ="UPDATE current_selection SET Description = '" + description + "'"
        SQL_Price ="UPDATE current_selection SET Price = '" + item_price + "'"
        #execute sql statement
        classifieds_db.execute(SQL_Source)
        classifieds_db.execute(SQL_Desc)
        classifieds_db.execute(SQL_Price)

        #commit the update
        connection.commit()
        #close db
        classifieds_db.close()
        connection.close()
    else:
        #checkbutton has not been ticked
        pass

def current_order_spin():
    current_order = item_spin.get()

    #checks the order chosen on the spin box
    if current_order == 'Second':
        index = 1
    elif current_order == 'Third':
        index = 2
    else:
        index = 0

    #clears the description box
    selection_label2.configure(state='normal')
    selection_label2.delete('1.0', 'end')

    
    try:
        if current_selection == 'Vinyls':
            #inbuilt function from the boffins to help with the downloading process
            webpage = download(amazon_vinlys)
            # uses regex statement to find the album name
            album = findall('<div class="p13n-sc-truncate p13n-sc-line-clamp-1"[ A-Za-z0-9-="]*>\n *(.*)\n[ ]*<\/div>',webpage)
            # uses regex statement to find the artists name
            artist = findall('<span class="a-size-small a-color-base"[ A-Za-z0-9-="]*[>]([A-Za-z0-9-$&,\/\s.]*)<\/span>',webpage)
            #combines the two results
            item = album[index] + ' by ' + artist[index]
            # it was common for a ' to be in the html as '&rsquo;' this just replaces it
            desc = item.replace('&rsquo;',"'")
            # displays description
            selection_label2.insert('1.0', desc)
            # Regex to find the price
            price = findall("<span class='p13n-sc-price' [ A-Za-z0-9-=]*[>]([0-9\.\$]*)<\/span>",webpage)
            #displays price
            selection_label1['text'] = price[index]
            
        elif current_selection == 'Phones':
            #inbuilt function from the boffins to help with the downloading process
            webpage = download(ebay_phones)
            #regex finds the decription of the mobile
            desc = findall('''<h3 class="s-item__title"[ A-Za-z0-9-="]*[>]([A-Za-z 0-9()\-\+\s\'\"\,. ]*)<\/h3>''',webpage)
            #chooses the desired description from the array created above and displays the description
            item = desc[index]
            selection_label2.insert('1.0', item)
            #finds and displays the price
            price = findall('<span class="s-item__price"[ A-Za-z0-9-="]*[>]([A-Za-z 0-9()\-\$\.]*)<\/span>',webpage)
            selection_label1['text'] = price[index]

        else:
            #inbuilt function from the boffins to help with the downloading process
            webpage = download(dealnews_toys)
            #finds the description for the toys/games and displays it also checking if there is an amp; to get rid of
            desc = findall('<a class="title-link"[ A-Za-z0-9-=":\/\.\?,_]*[>]\n +(.*)<\/a>',webpage)
            item = desc[index].replace('amp;','')
            # there was odd spacing in the regex so this just prevents odd descriptions
            selection_label2.insert('1.0', item.strip())
            #finds and diplats the price of the item
            price = findall('<div class="callout limit-height limit-height-large-1 limit-height-small-1"[ A-Za-z0-9-=":\/\.\?,_]*[>]\n([\s\$0-9a-z\%+]*)<[ A-Za-z0-9-=":\/\.\?,_]*>',webpage)
            selection_label1['text'] = price[index].strip()
    except NameError:
        #making robust
        selection_label2.insert('1.0', 'Description Error: Choose a category first!')
    except TypeError:
        #its so robust
        selection_label2.insert('1.0', 'Offline Error: Sites cannot be connected. Confirm your internet connection is working')

    #checks to see if the save selection button has been pressed
    # if so the information will be saved to the db
    save_sel_clicked()

    #doesn't allow the user to make edits to the textbox
    selection_label2.configure(state='disabled')

def current_selection_vinyl():
    #Function occurs when clicked on the vinyl category button
    global current_selection
    current_selection = 'Vinyls'
    #changes source and url to respective source and url depending on category
    selection_label3['text'] = 'Source: Amazon Bestsellers'
    selection_label4['text'] = 'URL: ' + amazon_vinlys
    # goes through the process to fill in price and description
    current_order_spin()


def current_selection_phones():
    #Function occurs when clicked on the mobile phones category button
    global current_selection
    current_selection = 'Phones'
    #changes source and url to respective source and url depending on category
    selection_label3['text'] = 'Source: eBay'
    selection_label4['text'] = 'URL: ' + ebay_phones
    # goes through the process to fill in price and description
    current_order_spin()
    
    
def current_selection_toys():
    #Function occurs when clicked on the toys and game category button
    global current_selection
    current_selection = 'Toys'
    #changes source and url to respective source and url depending on category
    selection_label3['text'] = 'Source: Deal News'
    selection_label4['text'] = 'URL: ' + dealnews_toys
    # goes through the process to fill in price and description
    current_order_spin()

# Create a window
window = Tk()

# Give the window a title
window.title('eBargins: Classified Ads')

#application image & heading
img = PhotoImage(file = 'handshaking.png')
main_label = Label(window, image = img,text = 'eBargins:\nClassified Ads', font = ('Times', 40), compound = 'right')
main_label.grid(row = 1, column = 1,sticky = 'we',padx = 5, columnspan = 2)


#Creating all the frames
category = LabelFrame(window, relief = 'groove', font = ('Times', 30), borderwidth = 2, text = 'Category')
category.grid(row = 2, column = 1, columnspan = 2, sticky = 'we', padx = 35)

item = LabelFrame(window, relief = 'groove', font = ('Times', 30), borderwidth = 2, text = 'Item')
item.grid(row = 3, column = 2,sticky = 'nswe',padx = (5,35))

options = LabelFrame(window, relief = 'groove', font = ('Times', 30), borderwidth = 2, text = 'Options')
options.grid(row = 3, column = 1,sticky = 'nswe', padx = (35,5))

selection = LabelFrame(window, relief = 'groove', font = ('Times', 30), borderwidth = 2, text = 'Selection')
selection.grid(row = 4, column = 1, columnspan = 2, sticky = 'we', padx = 5, pady = 5)

#category push buttons
cat_button1 = Button(category, text = 'Vinyls', width = 15, font = ('Times', 20), command = current_selection_vinyl)
cat_button2 = Button(category, text = 'Mobile Phones', width = 15, font = ('Times', 20), command = current_selection_phones)
cat_button3 = Button(category, text = 'Toys & Gaming', width = 15, font = ('Times', 20), command = current_selection_toys)

cat_button1.grid(row = 1, column = 1)
cat_button2.grid(row = 2, column = 1)
cat_button3.grid(row = 3, column = 1)

# category labels
cat_label1 = Label(category, text = '@ Amazon Best Sellers', font = ('Times', 20))
cat_label2 = Label(category, text = '@ eBay', font = ('Times', 20),)
cat_label3 = Label(category, text = '@ Deal News', font = ('Times', 20))

cat_label1.grid(row = 1, column = 2, sticky = 'w')
cat_label2.grid(row = 2, column = 2, sticky = 'w')
cat_label3.grid(row = 3, column = 2, sticky = 'w')


# item spinbox
item_spin = Spinbox(item, values = ('First','Second','Third'), font = ('Times', 15), command = current_order_spin)

item_spin.grid(row = 1, column = 1, sticky = 'we')

# selection labels
selection_label1 = Label(selection, text = '$00.00', font = ('Times', 25),bg = '#D3D3D3', relief = 'ridge', width = 25)
selection_label2 = ScrolledText(selection, font = ('Times', 20),bg = '#D3D3D3', relief = 'ridge', width = 25, height = 1)
selection_label2.insert('1.0','Description of selected item')
selection_label2.configure(state='disabled')
selection_label3 = Label(selection, text = 'Source: Name of classified ad site', font = ('Times', 15), bg = '#D3D3D3', relief = 'ridge', width = 25)
selection_label4 = Label(selection, text = 'URL: Address where item is listed', font = ('Times', 15), bg = '#D3D3D3', relief = 'ridge', width = 45)

selection_label1.grid(row = 1, column = 1, sticky = 'we')
selection_label2.grid(row = 1, column = 2, rowspan = 2, sticky = 'nswe')
selection_label3.grid(row = 2, column = 1, sticky = 'we')
selection_label4.grid(row = 3, column = 1, columnspan = 2, sticky = 'nsew')


#options components
show_det_button = Button(options, text = 'Show Details', font = ('Times', 15), command = url_open)
check_state = IntVar()
save_sel_check = Checkbutton(options, text = 'Save Selection', onvalue = 1, offvalue = 0, variable = check_state, font = ('Times', 15), command = save_sel_clicked)

show_det_button.grid(row = 1, column = 1)
save_sel_check.grid(row = 1, column = 2)

#colouring everything in
window['bg'] = '#ffe2a0'
main_label['bg'] = '#ffe2a0'
category['bg'] = '#ffe2a0'
cat_label1['bg'] = '#ffe2a0'
cat_label2['bg'] = '#ffe2a0'
cat_label3['bg'] = '#ffe2a0'
selection['bg'] = '#ffe2a0'
item['bg'] = '#ffe2a0'
options['bg'] = '#ffe2a0'
save_sel_check['bg'] = '#ffe2a0'
save_sel_check['activebackground'] = '#ffe2a0'

mainloop()