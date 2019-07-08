from functions import *

import pytest

def test_is_question():
    """Tests for the 'is_question' function"""
    
    # test if input question contains 'magic conch' and '?'
    assert is_question("magic conch will the Chargers win the SuperBowl?") == True

def test_is_or_question():
    """Tests for the 'is_or_question' function"""
    
    # test if input question containing the word 'or'
    assert is_or_question("magic conch should i eat sushi or steak for lunch?") == True

def test_is_how_question():
    """Tests for the 'is_how_question' function"""
    
    # test if input question contains the word 'how'
    assert is_how_question("magic conch how will I become a millionaire?") == True

def test_remove_punctuation():
    """Tests for the 'remove_punctuation' function"""
    
    # tests if punctuation will be removed from input
    assert remove_punctuation("hi, nice to meet you!") == "hi nice to meet you"

def test_prepare_text():
    """Tesets for the 'prepare_text' function"""
    
    # tests if input text will become lower case, punctuation will be removed, and text will be separated 
    assert prepare_text("Hey! What's going on, man?") == ["hey", "whats", "going", "on", "man"]

def test_selector():
    """Tests for the 'selector' function"""
    
    # tests if output would be returned if input text is in a list 
    assert selector(["hi", "hello"], ["hello"], ["in"]) == 'in'
    assert selector(["hi", "hello"], ["hey"], ["in"]) == None

def test_string_concatenator():
    """Tests for the 'string_concatenator' function"""
    
    # tests if string will be joined with a specified separator
    assert string_concatenator("a", "b", " ") == "a b"
    assert string_concatenator("Howdy", "partner", "~") == "Howdy~partner"

def test_list_to_string():
    """Tests for the 'list_to_string' function"""
    
    # Tests if a lists of strings will be joined with a specified separator
    assert list_to_string(["hey", "whats", "up"], ' ') == "hey whats up"

def test_end_chat():
    """Tests for 'end_chat' function"""
    
    # Tests if 'quit' will return True
    assert end_chat("quit") == True

def test_is_buffalo_joke():
    """Tests for 'is_buffalo_joke' function"""

    # Tests if 'bison' will return True
    assert is_buffalo_joke("bison") == True
