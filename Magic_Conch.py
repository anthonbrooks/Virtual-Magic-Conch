
# coding: utf-8

# In[5]:


import string
import random
import nltk
import pytest


# In[2]:


def is_question(input_string):
    """
    
    Determine if user input is a question that includes a critical term.
    
    Parameters
    ----------
    input_string : string
        String to be determined is a question or not
        
    Returns
    -------
    output : boolean
        True if the input string contains 'magic conch' and '?'
        False if the input string does not include these strings
    
    """
    
    output = ''
    
    if '?' and 'magic conch' in input_string:
        
        output = True
    
    else:
        output = False
        
    return output


# In[3]:


def test_is_question():
    """Tests for the 'is_question' function"""
    
    # test if input question contains 'magic conch' and '?'
    assert is_question("magic conch will the Chargers win the SuperBowl?") == True


# In[4]:


def is_or_question(input_string):
    """
    
    Determine if user input is a question that includes the word 'or'
    
    Parameters
    ----------
    input_string : string
        String to be determined is a comparison question or not
        
    Returns
    -------
    output : boolean
        True if the input string contains 'or'
        False if the input string does not include this string
    
    """
    
    output = ''
    
    if 'or' in input_string:
        output = True
        
    else:
        output = False
        
    return output


# In[5]:


def test_is_or_question():
    """Tests for the 'is_or_question' function"""
    
    # test if input question containing the word 'or'
    assert is_or_question("magic conch should i eat sushi or steak for lunch?") == True


# In[6]:


def is_how_question(input_string):
    """
    
    Determine if user input is a question that includes the word 'how'
    
    Parameters
    ----------
    input_string : string
        String to be determined is a 'how' question or not
        
    Returns
    -------
    output : boolean
        True if the input string contains 'how'
        False if the input string does not include this string
    
    """
    
    output = ''
    
    if 'how' in input_string:
        output = True
        
    else:
        output = False
        
    return output


# In[7]:


def test_is_how_question():
    """Tests for the 'is_how_question' function"""
    
    # test if input question contains the word 'how'
    assert is_how_question("magic conch how will I become a millionaire?") == True


# In[7]:


def remove_punctuation(input_string):
    """
    
    Check for and remove punctuation from a string
    
    Parameters
    ----------
    input_string : string
        String to remove punctuation from so the virtual magic conch can understand the input
        
    Returns
    -------
    out_string : string
        Same string as input_string without any punctuation symbols
    
    """
    
    out_string = ''
    
    for char in input_string:
        if char not in string.punctuation:
            out_string = out_string + char
            
    return(out_string)


# In[9]:


def test_remove_punctuation():
    """Tests for the 'remove_punctuation' function"""
    
    # tests if punctuation will be removed from input
    assert remove_punctuation("hi, nice to meet you!") == "hi nice to meet you"


# In[10]:


def prepare_text(input_string):
    """
    
    Makes an input string all lower case, removes punctuation, and separates that string into a list of words
    
    Parameters
    ----------
    input_string : string
        String to remove punctuation from, make lower case, and separate so the virtual magic conch can understand the input
        
    Returns
    -------
    out_list : list
        list of separated lower case strings without punctuation
    
    """
    
    out_list = []
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return(out_list)


# In[12]:


def test_prepare_text():
    """Tesets for the 'prepare_text' function"""
    
    # tests if input text will become lower case, punctuation will be removed, and text will be separated 
    assert prepare_text("Hey! What's going on, man?") == ["hey", "whats", "going", "on", "man"]


# In[13]:


def selector(input_list, check_list, return_list):
    """
    
    Take a list of words that we got as input, a list of words to check for if they appear in the input,
    and a list of possible outputs to return if something from the list to check is in the input list
    
    Parameters
    ----------
    input_list : list
        A list of strings returned from the 'prepare_text' function
        
    check_list : list
        A list of strings that are checked if the strings are included in 'input_list'
        
    return_list : list
        A list of words to return if 'check_list' is in 'input_list'
    
    Returns
    -------
    output : string
        A selected string from 'return_list'
    
    """
    
    output = None
    
    for element in input_list:
        if element in check_list:
            output = random.choice(return_list)
            break
            
    return output


# In[14]:


def test_selector():
    """Tests for the 'selector' function"""
    
    # tests if output would be returned if input text is in a list 
    assert selector(["hi", "hello"], ["hello"], ["in"]) == 'in'
    assert selector(["hi", "hello"], ["hey"], ["in"]) == None


# In[15]:


def string_concatenator(string1, string2, separator):
    """
    
    Concatenates two strings, combining them with a specified separator
    
    Parameters
    ----------
    string1 : string
        String to be joined with 'string2' and 'separator'
    
    string2 : string
        String to be joined with 'string1' and 'separator'
    
    separator : string
        Separator to be joined in between 'string1' and 'string2'
        
    Returns
    -------
    output : string
        A string of 'string1', 'string2', and 'separator' joined together 
    
    """
    
    output = '' or None
    
    output = string1 + separator + string2
    
    return output


# In[16]:


def test_string_concatenator():
    """Tests for the 'string_concatenator' function"""
    
    # tests if string will be joined with a specified separator
    assert string_concatenator("a", "b", " ") == "a b"
    assert string_concatenator("Howdy", "partner", "~") == "Howdy~partner"


# In[17]:


def list_to_string(input_list, separator):
    """
    
    Takes a list of strings, concatenates them, adds a specified separator in between
    
    Parameters
    ----------
    input_list : string
        List of separated strings
        
    separator : string
        A string of a specified separator
        
    Returns
    -------
    output : string
        String of words separated by 'separator'
    
    """
    
    output = input_list[0]
    
    for element in input_list[1:]:
        output = string_concatenator(output, element, separator)
        
    return output


# In[18]:


def test_list_to_string():
    """Tests for the 'list_to_string' function"""
    
    # Tests if a lists of strings will be joined with a specified separator
    assert list_to_string(["hey", "whats", "up"], ' ') == "hey whats up"


# In[19]:


def end_chat(input_list):
    """
    
    End the conversation if the word 'quit' appears
    
    Parameters
    ----------
    input_list : list
        A list of strings

    Returns
    -------
    output : boolean
        return 'True' if 'input_list' contains 'quit'
    
    """
    
    output = ''
    
    if 'quit' in input_list:
        output = True
        
    else:
        output = False
        
    return output

def is_buffalo_joke(input_string):
    """
    
    End the conversation if the word 'bison' appears
    
    Parameters
    ----------
    input_string : string
        A string input by user

    Returns
    -------
    output : boolean
        return 'True' if 'input_string' contains 'bison'
    
    """
    
    output = ''
    
    if 'bison' in input_string:
        output = True
        
    else:
        output = False
        
    return output


# In[20]:


def test_end_chat():
    """Tests for 'end_chat' function"""
    
    # Tests if 'quit' will return True
    assert end_chat("quit") == True

def test_is_buffalo_joke():
    """Tests for 'is_buffalo_joke' function"""

    # Tests if 'bison' will return True
    assert is_buffalo_joke("bison") == True


# In[21]:


def is_in_list(list_one, list_two):
    """
    
    Check if any element of list_one is in list_two.
    
    Parameters
    ----------
    list_one : list
        A list of strings

    list_two : list
        A list of strings
        
    Returns
    -------
    output : boolean
        return 'True' if 'list_two' contains elements in 'list_one'
    
    """
    
    for element in list_one:
        if element in list_two:
            return True
    
    return False

def find_in_list(list_one, list_two):
    """
    
    Find and return an element from list_one that is in list_two, or None otherwise.
    
    Parameters
    ----------
    list_one : list
        A list of strings

    list_two : list
        A list of strings
        
    Returns
    -------
    element : string
        return element if that element is in both 'list_one' and 'list_two'
    
    """
    
    for element in list_one:
        if element in list_two:
            return element
    return None


# In[22]:


# Inputs that the magic conch will recognize, and ouputs that it will respond with 

GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings', 'hola']
GREETING_OUT = ["Hello, I am a virtual magic conch, "
                 "I can answer any question that you may have in life.                                 "
                 "To get started, begin your question with 'magic conch ...'"]

COMP_IN = ['python']
COMP_OUT = ["Python is what I'm made of."]

JOKES_IN = ['funny', 'joke', 'jokes']
JOKES_OUT = ["What did the buffalo say when his son left?", 
             "The first time I got a universal remote control, I thought to myself 'This changes everything.'",
            "I refused to believe my road worker father was stealing from his job, but when I got home, all the signs were there"]

OR_QUESTION = ["both", "neither"]

LIFE = ["life", "where"]

PERSONAL = ["you", "your"]

UNKNOWN = ['Huh?']

QUESTION = ["Yes!", "No!",
            "You'll figure it out.", "Not a chance.", 
            "Repeat the question, please."]


# In[23]:


def magic_conch():
    """Main function to run the magic conch chatbot."""
    
    chat = True
    
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False
        
        # Check if the answer to the buffalo joke is correct, if so, return end msg
        if is_buffalo_joke(msg):
            out_msg = 'Bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETING_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))

            # Check if the input looks like a joke, add a joke output if so
            if is_in_list(msg, JOKES_IN):
                outs.append(list_to_string(random.choice(JOKES_OUT), ''))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = random.choice(QUESTION)
            
            # check if the question looks philosphical, return the out_msg if so
            if is_in_list(msg, LIFE):
                out_msg = "Sorry, I can't help you with that."
            
            # check if the question contains 'or', return an or question output if so
            if is_or_question(msg):
                out_msg = random.choice(OR_QUESTION)
            
            # check if the question seems too personal, return the out_msg if so
            if is_in_list(msg, PERSONAL):
                out_msg = "I'm sorry, that's a little too personal."
            
            # check if the input is a how question, return the out_msg if so
            if is_how_question(msg):
                out_msg = "look within."

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)


# In[24]:


# magic conch chatbot
magic_conch()

