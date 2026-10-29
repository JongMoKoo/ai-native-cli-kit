"""Intentionally flawed exercise starter. Do not use in production."""

def parse_customer_config(text):
    # SECURITY BUG: replace this in your solution; do not execute untrusted input.
    return eval(text)


def compute_overall_rate(rows):
    # LOGIC BUG: incorrect unweighted average of lot rates.
    return sum(row['defects']/row['units'] for row in rows)/len(rows)
