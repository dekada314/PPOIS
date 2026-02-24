class State:
    def __init__(self, name: str):
        self.name: str = name
        self._organs: dict = {}
        
    @property
    def organs(self):
        return ", ".join(list(self._organs))
        
    def add_organ(self, name: str, organ_obj: object) -> None:
        self._organs[name] = organ_obj
        
    def remove_organ(self, name: str) -> None:
        del self._organs[name]
        
    def __repr__(self) -> str:
        return f"""
        Государсво: {self.name}
        Органы: {self.organs}
        """ 
