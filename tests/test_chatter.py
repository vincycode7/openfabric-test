"""
This code uses the Pytest framework to test a ChatterBot class. Below are the details of each test function:

test_is_trained - This function tests whether the ChatterBot instance is trained or not. It asserts that the is_trained method of the ChatterBot instance returns True.

test_chat - This function tests whether the ChatterBot instance can generate a response for a given input. It asserts that the chat method of the ChatterBot instance returns a non-empty response for a given input.

test_train_corpus - This function tests whether the ChatterBot instance can be trained on a corpus. It asserts that the train method of the ChatterBot instance returns the message "ChatterBot training completed successfully" and that the is_trained method of the ChatterBot instance returns True after training.

test_train_conversation - This function tests whether the ChatterBot instance can be trained on a conversation list. It creates a conversation list and asserts that the train method of the ChatterBot instance returns the message "ChatterBot training completed successfully" and that the is_trained method of the ChatterBot instance returns True after training.

"""

import pytest
from chatter import Chatter

@pytest.fixture(scope="module")
def chatter():
    """
    Fixture function that returns a ChatterBot instance.
    """
    return Chatter()

def test_is_trained(chatter):
    """
    Test function to check if the ChatterBot instance is trained or not.
    """
    assert chatter.is_trained() == True

def test_chat(chatter):
    """
    Test function to check if the ChatterBot instance can generate a response for a given input.
    """
    response = chatter.chat("what's the laws of thermodynamics in simple english?")
    assert response != ""

def test_train_corpus(chatter):
    """
    Test function to check if the ChatterBot instance can be trained on a corpus.
    """
    assert chatter.train() == "ChatterBot training completed successfully."
    assert chatter.train(corpus_names=['chatterbot.corpus.english.science']) == "ChatterBot training completed successfully."
    assert chatter.is_trained() == True

def test_train_conversation(chatter):
    """
    Test function to check if the ChatterBot instance can be trained on a conversation list.
    """
    conversation_list = [
    "Hello", "Hi there!",
    "What is your name?", "My name is ScienceBot.",
    "How are you?", "I'm doing great.",
    "That is good to hear.", "Yes it is.",
    ]
    assert chatter.train(conversation_list=conversation_list) == "ChatterBot training completed successfully."
    assert chatter.is_trained() == True