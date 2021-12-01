froom typing import Optional
from mint.action.base_analysis import Analysis

class WebsocketFeeder:
    def __init__(self,analyzes: Optional[Analysis] = None,*args,**kwargs):
        self._analyzer= analyzer
        self.ws= None
        
    def close(self):
        """
        stops listening to the websocket
        """
        raise NotImplementedError
    
    def connect(self):
        raise NotImplementedError
        
    def on_message(self,message):
        """
        processes a new incoming message
        """
        if self._analyzer:
            self._analyzer.on_message