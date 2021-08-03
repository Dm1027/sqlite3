class Mortgage:

    def __init__(self,houseNum,street,city,state,zip,sellPrice,listPrice):
        self.houseNumber = houseNum
        self.streetName = street
        self.city = city
        self.state = state
        self.zip = zip
        self.sellPrice = sellPrice
        self.listPrice = listPrice
        
    
    @classmethod
    def from_string(cls, house_string):
        house_num, street_name, city, state, zipcode, sell_price, list_price = house_string.split(',')
        return cls(house_num, street_name, city, state, zipcode, sell_price, list_price)

objs = list()
def objs_from_file(path):
    f = open(path, 'r')
    houses = f.readlines()

    for line in houses:
        objs.append(Mortgage.from_string(line))

objs_from_file('houses.txt')

