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
    def play_for(a_performace):
        play = plays[a_performace["playID"]]
        return play

    def amount_for(a_performance):
        result = 0
        if play_for(a_performance)["type"] == "tragedy":
            result = 40000
            if a_performance["audience"] > 30:
                result += 1000 * (a_performance["audience"] - 30)
        elif play_for(a_performance)["type"] == "comedy":
            result = 30000
            if a_performance["audience"] > 20:
                result += 10000 + 500 * (a_performance["audience"] - 20)
            result += 300 * a_performance["audience"]
        else:
            raise ValueError(f"unknown type: {play_for(a_performance)['type']}")
        return result

    def volume_credits_for(a_performance):
        result = 0
        result += max(a_performance["audience"] - 30, 0)
        if play_for(a_performance)["type"] == "comedy":
            result += a_performance["audience"] // 5
        return result

    def usd(a_number):
        return f"${a_number/100:,.2f}"

    def total_volume_credits():
        result = 0
        for perf in invoice["performances"]:
            result += volume_credits_for(perf)
        return result

    def total_amount():
        result = 0
        for perf in invoice["performances"]:
            result += amount_for(perf)
        return result

    result = f"Statement for {invoice['customer']}\n"
    for perf in invoice["performances"]:
        result += f"  {play_for(perf)['name']}: {usd(amount_for(perf))} ({perf['audience']} seats)\n"
    result += f"Amount owed is {usd(total_amount())}\n"
    result += f"You earned {total_volume_credits()} credits\n"
    return result


if __name__ == "__main__":
    print(statement(invoices, plays))
