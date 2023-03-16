

import logging
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.storage import SQLStorageAdapter

logger = logging.getLogger(__name__)


class Chatter:
    """
    A wrapper class for ChatterBot, an open source chatbot engine.

    Attributes:
    - database_uri (str): URI of the database to use for storage
    - chatbot (ChatBot): instance of the ChatterBot engine
    """

    def __init__(self, database_uri: str = None):
        """
        Initialize the ChatterBot instance and load the language model if available.

        Args:
        - database_uri (str): URI of the database to use for storage (defaults to a SQLite database)
        - path_to_chatter (str): path to the JSON configuration file for the chatbot
        """
        self.database_uri = database_uri or 'sqlite:///sciencebotdb.db'
        self.chatbot = ChatBot(
            'ScienceBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri=self.database_uri,
        )
        
        # Check if the chatbot has been trained
        if self.is_trained():
            logger.info(f"The chatbot has been trained on {self.chatbot.storage.count()} statements.")
        else:
            logger.info("The chatbot has not been trained yet.")
            self.train()

    def is_trained(self) -> bool:
        """
        Check if the chatbot has been trained.

        Returns:
        - bool: True if the chatbot has been trained, False otherwise.
        """
        return self.chatbot.storage.count() > 0

    def set_trainer(self,trainer_type):
        """
        Description: This method sets the trainer for the ChatBot instance.

        Parameters:

        trainer_type: The type of the trainer to be set.
        Return Type: None
        """ 
        self.chatbot.trainer = trainer_type(self.chatbot)
        
    def train(self, trainer_type=ChatterBotCorpusTrainer, corpus_names: list = None,
              conversation_list: list = None) -> str:
        """
        Train the chatbot on the specified corpus or conversation list.

        Args:
        - trainer_type (type): the type of trainer to use (defaults to ChatterBotCorpusTrainer)
        - corpus_names (list): the names of the corpora to train on (defaults to ['chatterbot.corpus.english.science'])
        - conversation_list (list): a list of conversation tuples to train on (defaults to None)

        Returns:
        - str: a message indicating that the training has completed successfully.
        """
        if conversation_list is not None:
            trainer_type = ListTrainer
        else:
            corpus_names = corpus_names or ['chatterbot.corpus.english.science']
        
        self.set_trainer(trainer_type)    
        
        if conversation_list is not None:
            self.chatbot.trainer.train(conversation_list)
        else:
            for corpus_name in corpus_names: self.chatbot.trainer.train(corpus_name)

        return "ChatterBot training completed successfully."

    def chat(self, text: str) -> str:
        """
        Get a response from the chatbot for the specified text.

        Args:
        - text (str): the input text to respond to

        Returns:
        - str: the response text from the chatbot
        """
        # Get a response from the chatbot
        response = self.chatbot.get_response(text)

        # Train on new user data and bot response
        self.train(conversation_list=[text, response.text])

        return response.text

if __name__ == '__main__':
    chatter = Chatter()
    chatter.chatbot.logger.info(f"Question: 'what's the laws of thermodynamics in simple english?' \n Response: {chatter.chat('whats the laws of thermodynamics in simple english?')}")