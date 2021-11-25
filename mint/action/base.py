from typing import Any 


class Action:
    def run(self, data: Any):
        """
            main method of the class. 
            executes any action using the incoming
            data
        """
        raise NotImplementedError
    
        