import pytest
import json

from invoice import statement


@pytest.fixture
def invoice():
    return json.loads("""
    {
        "customer": "BigCo",
        "performances": [
            {
                "playID": "hamlet",
                "audience": 55
            },
            {
                "playID": "as-like",
                "audience": 35
            },
            {
                "playID": "othello",
                "audience": 40
            }
        ]
    }""")


@pytest.fixture
def plays():
    return json.loads("""
    {
        "hamlet": {
            "name": "Hamlet",
            "type": "tragedy"
        },
        "as-like": {
            "name": "As You Like It",
            "type": "comedy"
        },
        "othello": {
            "name": "Othello",
            "type": "tragedy"
        }
    }""")


def test_statement(invoice, plays):
    expected = """Statement for BigCo\n  Hamlet: $650.00 (55 seats)\n  As You Like It: $580.00 (35 seats)\n  Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n"""

    assert statement(invoice, plays) == expected
