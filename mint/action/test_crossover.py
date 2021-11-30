from crossover import Crossover

class TestCrossover:
    def test_calculate(self):
        #initializing components
        
        #sending message
        messages = [
            {
                'data':{
                    'timestamp': '2019-04-01',
                    'price':10
                    
                }
            },
            {
                'data':{
                    'timestamp': '2019-04-01',
                    'price':9
                    
                }
                
            },
            {
                'data':{
                    'timestamp': '2019-04-01',
                    'price':11
                    
                }
                
            },
   
            
        ]
        analyzer = Crossover(short_ma=1, long_ma=3)
        
        #sending message
        for m in messages:
            analyzer.on_message(m)
            
        