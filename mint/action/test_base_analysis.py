from base_analysis import Analysis
from base import Action

class mockAction(Action):
    def run(self,data):
        self.data = data 
        
class TestAnalysis:
    def test_send_signal(self):
        
        #initialiazind components
        action = mockAction()
        analyzer = Analysis(action=action)
        message = "test"
        
        #sending signal
        
        analyzer.send_signal(message)
        
        #assert self.data 
        assert action.data == message
        