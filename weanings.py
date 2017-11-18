class WeaningGroup(object):
    def __init__(self, num_litters, num_weaners):
        self._num_litters = num_litters
        self._num_weaners = num_weaners

    @property
    def pigs_per_litter(self):
        return self._num_weaners / self._num_litters

    @property
    def num_litters(self):
        return self._num_litters

    @property
    def num_weaners(self):
        return self._num_weaners
