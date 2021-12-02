
from typing import List, SupportsBytes
from loguru import logger
from base_feeder import WebsocketFeeder
from config import BITA_USER,BITA_PASSWORD
import requests
import websocket as ws
import json

class BitaFeeder(WebsocketFeeder):
    def __init__(self,
                 assets = List[str],
                 *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.token = self.login()
        self.connect()
    
        #subscribing to assets.
        for asset in assets:
            self.subscribe(asset)
        self.listen()
    

    def connect(self):
        url = "wss://ws.bitadata.com"
        header = {'api_key': self.token}
        self.ws = ws.create_connection(url, header=header)
        logger.info("Connection with the websocket established")

    def login(self):
        """
        log into the rest api
        """
        #making loging request.
        url ="https://api.bitadata.com/v1/login/"
        payload = {'user': BITA_USER,
                   'password': BITA_PASSWORD}
        res = requests.post(url, data=payload)
        
        #return token
        if res.ok:
            data = json.loads(res.text)
            token = data['token']
            logger.info("bita login sucess")
            return token 
        else:
            logger.debug("Bita login failed")
            
            
            
    def subscribe(self,asset):
        """
        subscribes to an asset channel of the websocket
        """
        subscription = '{"event" :"subscribe", "id": "' + asset + '", "channel": "live"}'
        self.ws.send(subscription)
        logger.debug(f"subcription message sent for {asset}")         