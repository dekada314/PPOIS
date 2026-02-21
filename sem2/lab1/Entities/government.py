class Government:
    def __init__(self, prime_minister: str = '', prime_minister_deputies: list[str] = [] ):
        self.prime_minister = prime_minister
        self.prime_minister_deputies = prime_minister_deputies
        self.ministries: list[str] = []