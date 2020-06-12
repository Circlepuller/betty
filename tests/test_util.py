import datetime

from betty.util import is_na


def test_is_na_str():
    assert is_na(None) == 'N/A'
    assert is_na('string') == 'string'


def test_is_na_cls():
    now = datetime.datetime.utcnow()

    assert is_na(now, datetime.date) == now
    assert is_na(None, datetime.date, now) == now
