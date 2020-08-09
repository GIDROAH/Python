class Siblings:
    __brother = None
    __sister = None
    
    def set_value(self, brother, sister):
        self.__brother = brother
        self.__sister = sister
        
    def get_brother(self):
        return self.__brother
    def get_sister(self):
        return self.__sister
        
class Male(Siblings):
    def name(self):
        return self.get_brother()
        
class Female(Siblings):
    def name(self):
        return self.get_sister()
        
m = Male()
f = Female()
m.set_value("Suraj", "Rashi")
f.set_value("Suraj", "Rashi")
print(m.name())
print(f.name())