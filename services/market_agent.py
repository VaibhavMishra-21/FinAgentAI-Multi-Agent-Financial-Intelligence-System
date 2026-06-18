from services.yahoo_finance import YahooFinanceService

class MarketAgent:

    def analyze_stock(self, symbol):

        data = YahooFinanceService.get_stock_data(symbol)

        latest_price = data["Close"].iloc[-1]

        highest = data["High"].max()

        lowest = data["Low"].min()

        return {
            "symbol": symbol,
            "latest_price": round(latest_price, 2),
            "highest": round(highest, 2),
            "lowest": round(lowest, 2)
        }
