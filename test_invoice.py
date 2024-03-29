from invoice import invoices, plays, statement


def test_statement():
    expected = """Statement for BigCo\n  Hamlet: $650.00 (55 seats)\n  As You Like It: $580.00 (35 seats)\n  Othello: $500.00 (40 seats)\nAmount owed is $1730.00\nYou earned 47 credits\n"""

    assert statement(invoices, plays) == expected
