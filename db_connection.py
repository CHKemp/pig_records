from datetime import datetime

class DataConnection(object):

    def __init__(self):
        self.weanings = [[datetime.now()]]

    def save_weaning(self, wean_date, n_litters, n_weaned):
        self.weanings.append([wean_date, n_litters, n_weaned])

    def get_weanings(self):
        return self.weanings
