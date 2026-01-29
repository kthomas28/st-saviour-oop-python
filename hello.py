class GuinneaPig: 
     def __init__(self, name: str, color: str):
        self.name = name 
        self.color = color 
        self.eyes = 2
        def squeak(self):
            return f' {self.name} the [self.color] guinnea pig squeaks!'
        if __name__ == '__main__':
            #print('new dawn, new day')
            potato = GuinneaPig('Potato', 'brown')
            print(potato.squeak())
            