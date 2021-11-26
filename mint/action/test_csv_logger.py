import csv
from csv_loggers import CSVLogger

class TestCSVLogger(CSVLogger):
    def __init__(self):
        raise NotImplementedError
        
    def test_run(self):
        
        # initializing component
        logs = self.CSVLogger()
        
        #writing a message
        message = "test"
        logs.run(data=message)
        
        
        #assertions
        with open(logs.file_name,'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    assert row[-1]== message 
                