class LaunchTime:
    def __init__(self,day,month,time = '10:00',year = '2020'):
        self.time = time
        self.day = day
        self.month = month     
        self.year = year

    def get_day(self):
        return float(self.day)
    def get_month(self):
        return float(self.month)
    def get_year(self):
        return float(year)
    def get_hour(self):
        return float(self.time[0:self.time.index(":")])
    def get_minute(self):
        return float(self.time[self.time.index(":")+1 : ])

    def compare_to(self,other):
        if(self.get_year() > other.get_year()):
            return 1
        elif(self.get_year() < other.get_year()):
            return -1
        else:
            if(self.get_month() > other.get_month()):
                return 1
            elif(self.get_month() < other.get_month()):
                return -1
            else: 
                if(self.get_day() > other.get_day()):
                    return 1
                elif(self.get_day() < other.get_day()):
                    return -1
                else:
                    if(self.get_hour() > other.get_hour()):
                        return 1
                    elif(self.get_hour() < other.get_hour()):
                        return -1
                    else:    
                        if(self.get_minute() > other.get_minute()):
                            return 1
                        elif(self.get_minute() < other.get_minute()):
                            return -1
                        else:  
                            return 0                 
    def __str__(self):
        return "{}-{}-{} {}".format(self.month,self.day,self.year,self.time)
    def __repr__(self):
        return 'LaunchTime(day=\'%s\',month=\'%s\',time=\'%s\',year=\'%s\')' % (self.day,self.month,self.time,self.year)

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