from datetime import date, datetime, timedelta

class WeaningGroup(object):
    def __init__(self, wean_date):
        self._wean_date = self._standardise_wean_date(wean_date)
        self._litters = 0.0
        self._weaners = 0.0

    def _standardise_wean_date(self, dt):
        _wean_day = 4
        weekday = dt.isoweekday()
        if weekday < _wean_day:
            day_diff = 7 + weekday - _wean_day
        else:
            day_diff = weekday - _wean_day
        std_date = dt - timedelta(days=day_diff)
        return std_date

    @property
    def wean_date(self):
        return self._wean_date

    @property
    def pigs_per_litter(self):
        try:
            ppl = self._weaners / self._litters
        except ZeroDivisionError:
            ppl = 0.0
        return ppl

    @property
    def litters(self):
        return self._litters

    @litters.setter
    def litters(self, n):
        self._litters = n

    @property
    def weaners(self):
        return self._weaners

    @weaners.setter
    def weaners(self, n):
        self._weaners = n


if __name__ == '__main__':
    dt = date.today()
    print(dt)
    wg = WeaningGroup(dt)
    print(wg.pigs_per_litter)

    dt_late = date(2018, 2, 3)
    wg = WeaningGroup(dt_late)
    print(dt_late)
    print(wg._standardise_wean_date(dt_late))
    dt_last = date(2018, 1, 29)
    wg = WeaningGroup(dt_last)
    print(dt_last)
    print(wg._standardise_wean_date(dt_last))
