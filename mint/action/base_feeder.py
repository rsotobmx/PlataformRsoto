from typing import Any, Counter, Dict, Optional
from base_analysis import Analysis
from threading import Thread
import json
from loguru import logger
from time import sleep
from ssl import SSLError


class WebsocketFeeder:
    def __init__(self,analyzer: Optional[Analysis] = None,*args,**kwargs):
        self._analyzer= analyzer
        self.counter =0
        self.listening=False
        self.ws= None
        
    def close(self):
        """
            stops listening to the websocket
        """
        self._stop_listening()
        logger.debug("Stop listening before closing the connection")
        sleep(1)
        
        #closing connection
        self.ws.close()
        logger.info("websocket connection closed")
    
    
    def connect(self):
        raise NotImplementedError
    
    def listen(self):
        """
        listens to the websocket using a new thread.
        """
        thread = Thread(target=self._listen)
        thread.start()
        
    def _listen(self):
        """
        listens for new messages comming through the connection
        """
        self.listening = True
        logger.info("listening to the websocket")
        while self.listening:
            try:
                message= self.ws.recv()
                data = json.loads(message)
                logger.debug(f"new message: {data}")
                self.on_message(message=data)
            
            except json.JSONDecodeError:
                logger.debug("json error")
                
            except KeyboardInterrupt:
                self.close()
                break
            
            except SSLError:
                logger.debug("SSL error") 
                
                 
        
    def on_message(self,message: Dict[str,Any]):
        """
        processes a new incoming message
        """
        if self._analyzer:
            self._analyzer.on_message(message)
        self.counter+=1 
            
    def _stop_listening(self):
        self.listening = False
               
    
    def subscribe(self):
        raise NotImplementedError
