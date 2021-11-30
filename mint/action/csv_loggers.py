import os
import csv
import datetime as dt
from loguru import logger 
from base import Action
from config import LOG_DIR


class CSVLogger(Action):
    def __init__(self,*args, **kwargs):
        now = dt.datetime.now()
        date_string = f"{now.year}{now.month}{now.day}{now.hour}{now.minute}.csv"
        
        self.file_name = os.path.join(LOG_DIR, date_string)  
        
         
              
    def run(self,data):
        """

            Basic logger that writes a 
            timestamp and a message
        """
        logger.debug("CSVLogger called")
        
        
        #writing data into th csv
        with open(self.file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([dt.datetime.now().isoformat(),data])
            logger.info(f"File written with:2 {data} ")