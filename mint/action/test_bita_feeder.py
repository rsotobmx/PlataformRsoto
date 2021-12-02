from bita_feeder import BitaFeeder
from time import sleep
import pytest

class TestBitaFeeder:
    def test_init(self):
        
        #initializing components
        assets = ['BTC']
        bita = BitaFeeder(assets)
        sleep(5)
        bita.close()
        
        #Assetions
        assert bita.token
        assert bita.counter >0 
        assert not bita.listening