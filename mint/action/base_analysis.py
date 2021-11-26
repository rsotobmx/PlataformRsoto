from mint.action.base import Action
from loguru import logger 

class Analysis(Action):
    def __init__(self,action:Action =None):
        
        self._action = action
        
        
    def calculate(self):
        """main operations of the class

       
        """
        raise NotImplementedError 
    def on_message(self,message):
        """
            processes a new incoming message
       
        """
        incoming_data = self.parse_message(message)
        self.calculate(incoming_data)
        
        
    def parse_message(self,message):
        """
            parses the incoming message data
        """
        raise NotImplementedError
        
    def send_signal(self):
        logger.info(f"New signal: {message}")
        if self.action:
            self._action.run(message)
        pass