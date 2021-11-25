import os
import csv
import datetime as dt
from loguru import logger 
from base import Action
from config import LOG_DIR

class CSVLogger(Action):
    def __init__(self,*args, **kwargs):
        now = dt.datatime.now()
        date_string = str(now.year) + str(now.month) +str(now.day)+str(now.hour) + str(now.minute)+'.csv'
        
        self.file_name = os.path.join(LOG_DIR, date_string)  
        
         
              
    def run(self,data):
        """

            Basic logger that writes a 
            timestamp and a message
        """
        logger.debug("CSVLogger called")
        
        
        #writing data into th csv
        with open(self.file_name,'w') as f:
            writer = csv.writer(f)
            writer.writerow([dt.datetime.now().isoformat(),data])
            logger.info("File written with:2 {data} ")