from datetime import date


def defect_rate(defects: int, production: int) -> float:
    """Weighted rate component; fail closed on invalid counts."""
    if not isinstance(defects, int) or not isinstance(production, int):
        raise TypeError('counts must be integers')
    if production <= 0 or defects < 0 or defects > production:
        raise ValueError('invalid production/defects')
    return defects / production


def compliance(rate: float | None, max_rate: float, *, inclusive: bool = True) -> str:
    """Return PASS/FAIL/REVIEW; missing rate is not zero."""
    if rate is None:
        return 'REVIEW'
    if not 0 <= rate <= 1 or not 0 <= max_rate <= 1:
        raise ValueError('rate outside [0,1]')
    ok = rate <= max_rate if inclusive else rate < max_rate
    return 'PASS' if ok else 'FAIL'


def days_since(check_date: date, as_of: date) -> int:
    if check_date > as_of:
        raise ValueError('future inspection date')
    return (as_of-check_date).days
