PRICE_CLASS = "//div[@class = 'ncss-brand pb6-sm fs14-sm fs16-md']"
from datetime import datetime
class Snipe:
    def __init__(self,price,day, month = datetime.now().strftime('%d')):
        self.price = price
        self.day = day
        self.month = month
        