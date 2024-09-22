class Mobile:
    def __init__(self,m,v):
        self.model=m
        self.volume=v
        print(self.model)
        print(self.volume)
    def feature(self,p):
        self.price=p
        print(f"The Model of mobile is:{self.model}, volume of mobile is:{self.volume} and price of mobile is:{self.price}")
redmi=Mobile('redmi note 8','120g')
redmi.feature(10000)
redmi.__init__('redmi note 9','140g')
