
class Product:
    def __init__(self,size,launch_time,link,name = None):
        self.name = name
        self.link = link
        self.size = size
        self.launch_time = launch_time

    def is_shoe(self):
        try:
            float(self.size)
            return True
        except ValueError:
            return False
    def get_countdown(self):
        #to be implemented
        return 

    def __str__(self):
        return "{}_{}_{}_{}".format(self.name,self.size,str(self.launch_time),self.link)
    
    def __repr__(self):
        return 'Product(size=\'%s\',launch_time=%s,link=\'%s\',name=\'%s\')' % (self.size,repr(self.launch_time),self.link,self.name)
