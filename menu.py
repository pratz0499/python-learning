class menu(dict):
    pass

class order(dict):
    def __init__(self, menu1):
        dict.__init__(self)
        self.menu1=menu1
    def __setitem__(self,k,v):
        if k in self.menu1:
            raise Exception("{} Already Exist".format(k))
           
        else:
            dict.[k]=v
            	

        
    
m=menu()

m['idly'] = 20
m['vada'] = 20
o=order(m)
o['dosa']=40
o['upma']=10
print(o.__dict__)
#o/p-> item exits in menu
#m.additems('dosa',25)
#m.show()
