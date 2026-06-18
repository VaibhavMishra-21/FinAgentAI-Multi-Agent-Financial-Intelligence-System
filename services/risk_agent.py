import numpy as np

class RiskAgent:

    def calculate_volatility(self, data):

        returns = data["Close"].pct_change().dropna()

        volatility = np.std(returns)

        return round(volatility * 100, 2)

    def risk_level(self, volatility):

        if volatility < 2:
            return "Low"

        elif volatility < 4:
            return "Medium"

        return "High"
