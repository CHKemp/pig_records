class DataConnection(object):

    def __init__(self):
        self.weanings = [[1, 2, 3]]

    def save_weaning(self, n_litters, n_weaned, weaned_per_litter):
        self.weanings.append([n_litters, n_weaned, weaned_per_litter])

    def get_weanings(self):
        return self.weanings
