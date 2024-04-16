from typing import Dict

plays = {
    "hamlet": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"},
}
invoices = {
    "customer": "BigCo",
    "performances": [
        {"playID": "hamlet", "audience": 55},
        {"playID": "as-like", "audience": 35},
        {"playID": "othello", "audience": 40},
    ],
}


def _play_for(a_perfornance: Dict) -> Dict:
    return plays[a_perfornance["playID"]]


def _amount_for(a_performance: Dict) -> int:
    result = 0
    if _play_for(a_performance)["type"] == "tragedy":
        result = 40000
        if a_performance["audience"] > 30:
            result += 1000 * (a_performance["audience"] - 30)
    elif _play_for(a_performance)["type"] == "comedy":
        result = 30000
        if a_performance["audience"] > 20:
            result += 10000 + 500 * (a_performance["audience"] - 20)
        result += 300 * a_performance["audience"]
    else:
        raise ValueError(f"unknown type: {_play_for(a_performance)['type']}")
    return result


def _usd(amount: int) -> str:
    return f"${amount/100:,.2f}"


def _volume_credit_for(perf: Dict) -> int:
    result = 0
    result += max(perf["audience"] - 30, 0)
    if _play_for(perf)["type"] == "comedy":
        result += perf["audience"] // 5
    return result


def _total_volume_credits(invoice: Dict) -> int:
    result = 0
    for perf in invoice["performances"]:
        result += _volume_credit_for(perf)
    return result


def _total_amount(invoice: Dict) -> int:
    result = 0
    for perf in invoice["performances"]:
        result += _amount_for(perf)
    return result


def statement(invoice, plays):
    result = f"Statement for {invoice['customer']}\n"
    for perf in invoice["performances"]:
        result += f"  {_play_for(perf)['name']}: {_usd(_amount_for(perf))} ({perf['audience']} seats)\n"
    result += f"Amount owed is {_usd(_total_amount(invoice))}\n"
    result += f"You earned {_total_volume_credits(invoice)} credits\n"
    return result


if __name__ == "__main__":
    print(statement(invoices, plays))
