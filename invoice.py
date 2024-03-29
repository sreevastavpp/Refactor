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


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice['customer']}\n"
    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        this_amount = 0
        if play["type"] == "tragedy":
            this_amount = 40000
            if perf["audience"] > 30:
                this_amount += 1000 * (perf["audience"] - 30)
        elif play["type"] == "comedy":
            this_amount = 30000
            if perf["audience"] > 20:
                this_amount += 10000 + 500 * (perf["audience"] - 20)
            this_amount += 300 * perf["audience"]
        else:
            raise ValueError(f"unknown type: {play['type']}")
        volume_credits += max(perf["audience"] - 30, 0)
        if play["type"] == "comedy":
            volume_credits += perf["audience"] // 5
        result += (
            f"  {play['name']}: ${this_amount/100:.2f} ({perf['audience']} seats)\n"
        )
        total_amount += this_amount
    result += f"Amount owed is ${total_amount/100:.2f}\n"
    result += f"You earned {volume_credits} credits\n"
    return result


if __name__ == "__main__":
    print(statement(invoices, plays))
