import pandas as pd
from loguru import logger
from base_analysis import Analysis
from typing import Any

class Crossover(Analysis):
    def __init__(self,
                short_ma: int, 
                long_ma: int,
                *args,**kwargs):
        super().__init__(*args,*kwargs)
        self.data = pd.Series()
        
        #strategy attibutes.
        self.short_ma = short_ma
        self.long_ma = long_ma
        self.short_ma_above = None
        
    def calculate(self, data: pd.Series):
        """
        Crossover logic

        
        """
        self.data = self.data.append(data)
        #calculating moving averages
        short_ma = self.data[-self.short_ma:].mean()
        long_ma = self.data[-self.long_ma:].mean()
        
        #checking thgew Mas state in the first itertation
        if self.short_ma_above == None:
            if short_ma > long_ma:
                self.short_ma_above = True
            else:
                self.short_ma_above = False
            logger.debug("Moving averages initial state checked")
            
        #calculating signal
        logger.info(f"Short MA: {short_ma}")
        logger.info(f"Short MA: {long_ma}")
        if short_ma < long_ma and self.short_ma_above:
            self.short_ma_above = False
            self.send_signal(message="short crossover")
            
        if short_ma > long_ma and not self.short_ma_above:
            self.short_ma_above = True
            self.send_signal(message="long crossover")
        
    def parse_message(self,message: Any) :
        """

        """
        try:
        
            timestamp = pd.Timestamp(message['data']['timestamp'])
            data = pd.Series(data=[message['data']['price']],
                            index=[timestamp])
            logger.debug(f"New data point:{data}")
            
            return data
        except KeyError:
            logger.warning(f"Message not treated: {message}")
            
        