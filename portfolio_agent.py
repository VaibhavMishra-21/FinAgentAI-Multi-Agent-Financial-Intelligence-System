class PortfolioAgent:

    def recommend(self, rsi, risk):

        if rsi < 30 and risk == "Low":
            return "BUY"

        elif rsi > 70:
            return "SELL"

        return "HOLD"
