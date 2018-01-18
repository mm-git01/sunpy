from __future__ import absolute_import, division, print_function

from astropy.time import Time


def test_utime_t0():
    t = Time('1979-01-01T00:00:00')
    assert t.utime == 0.0


def test_utime_random_date():
    t = Time('2018-01-13T13:32:56')
    assert t.utime == 1231853576.0
