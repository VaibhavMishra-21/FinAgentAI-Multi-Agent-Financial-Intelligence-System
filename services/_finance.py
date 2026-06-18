import yfinance as yf

class YahooFinanceService:

    @staticmethod
    def get_stock_data(symbol, period="1y"):

        stock = yf.Ticker(symbol)

        df = stock.history(period=period)

        return df
