import pandas as pd

class TechnicalAgent:

    def calculate_rsi(self, data, period=14):

        delta = data["Close"].diff()

        gain = delta.where(delta > 0, 0)

        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(period).mean()

        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

        return rsi.iloc[-1]

    def moving_average(self, data):

        return data["Close"].rolling(20).mean().iloc[-1]
