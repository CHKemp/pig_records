from datetime import date

class Pig(object):
    def __init__(self, mgmt_tag):
        self._mgmt_tag = mgmt_tag

    @property
    def mgmt_tag(self):
        return self._mgmt_tag


class Sow(Pig):
    def __init__(self, mgmt_tag, gilt=False):
        super(Sow, self).__init__(mgmt_tag)
        self._litters = []
        if gilt is not False:
            pass
        else:
            self._service_dates = []

    def add_litter(self, litter):
        self._litters.append(litter)


class Litter(object):
    def __init__(self, born_alive, born_dead, mummified, farrow_date=False):
        self._born_alive = born_alive
        self._born_dead = born_dead
        self._mummified = mummified
        if farrow_date is False:
            self._farrow_date = date.today()
        else:
            self._farrow_date = farrow_date

        self._num_alive = self._born_alive
        self._death_ages = {}

    def add_mortality(self, num_dead, mort_date=False):
        self._num_alive -= num_dead


if __name__ == '__main__':
    dt = date.today()
    lt = Litter(12, 1, 1)

    sw = Sow(333)
    sw.add_litter(lt)

    lt.add_mortality(1)