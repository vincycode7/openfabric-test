import pytest
from chatter import Chatter


@pytest.fixture(scope="module")
def chatter():
    return Chatter()


def test_is_trained(chatter):
    assert chatter.is_trained() == True


def test_chat(chatter):
    response = chatter.chat("what's the laws of thermodynamics in simple english?")
    assert response != ""


def test_train_corpus(chatter):
    assert chatter.train() == "ChatterBot training completed successfully."
    assert chatter.train(corpus_names=['chatterbot.corpus.english.science']) == "ChatterBot training completed successfully."
    assert chatter.is_trained() == True


def test_train_conversation(chatter):
    conversation_list = [
        "Hello", "Hi there!",
        "What is your name?", "My name is ScienceBot.",
        "How are you?", "I'm doing great.",
        "That is good to hear.", "Yes it is.",
    ]
    assert chatter.train(conversation_list=conversation_list) == "ChatterBot training completed successfully."
    assert chatter.is_trained() == True
