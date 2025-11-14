class Myclass:
    def __init__(self, value):
        self.value = value
        
    def __lt__(self, other: 'Myclass'):
        return self.value < other.value
    
    def __eq__(self, other: 'Myclass'):
        return self.value == other.value
    
    def __gt__(self, other: 'Myclass'):
        return self.value > other.value
    
    