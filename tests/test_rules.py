import pytest
from datetime import date
from src.rules import defect_rate, compliance, days_since

def test_weighted_components():
    assert defect_rate(10, 1000) == 0.01

def test_bad_counts():
    with pytest.raises(ValueError): defect_rate(3, 2)

def test_missing_and_boundaries():
    assert compliance(None, .01) == 'REVIEW'
    assert compliance(.01, .01) == 'PASS'
    assert compliance(.01, .01, inclusive=False) == 'FAIL'

def test_date_boundary():
    assert days_since(date(2026, 10, 1), date(2026, 10, 15)) == 14
