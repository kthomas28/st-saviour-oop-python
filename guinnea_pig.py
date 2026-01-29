
class GuinneaPig:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.legs = 4

    def squeak(self):
        return f'{self.name} the {self.color} guinnea pig squeaks!'
    
if __name__ == '__main__':
    # print('new dawn, new day')
    pipsqueak = GuinneaPig('Pipsqueak', 'calico')
    print(pipsqueak.squeak())

    potato = GuinneaPig('Potato', 'brown')
    print(potato.squeak()) 


        
