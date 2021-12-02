from base import Action
from loguru import logger 
from typing import Any,Optional
            

class Analysis:
    def __init__(self,
                 action: Optional[Action] =None):
        
        self._action = action
        
        
    def calculate(self):
        """main operations of the class

       
        """
        raise NotImplementedError 
    def on_message(self,message:Any):
        """
            processes a new incoming message
       
        """
        incoming_data = self.parse_message(message)
        self.calculate(incoming_data)
        
        
    def parse_message(self, message: Any):
        """
            parses the incoming message data
        """
        raise NotImplementedError
        
    def send_signal(self,message: str):
        logger.info(f"New signal: {message}")
        if self._action:
            self._action.run(message)
        pass