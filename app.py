from agents.market_agent import MarketAgent
from agents.technical_agent import TechnicalAgent
from agents.risk_agent import RiskAgent
from agents.portfolio_agent import PortfolioAgent
from models.forecasting import ForecastModel
from services.yahoo_finance import YahooFinanceService

symbol = "AAPL"

market = MarketAgent()
technical = TechnicalAgent()
risk = RiskAgent()
portfolio = PortfolioAgent()
forecast = ForecastModel()

data = YahooFinanceService.get_stock_data(symbol)

market_result = market.analyze_stock(symbol)

rsi = technical.calculate_rsi(data)

volatility = risk.calculate_volatility(data)

risk_status = risk.risk_level(volatility)

recommendation = portfolio.recommend(rsi, risk_status)

prediction = forecast.forecast(data)

print("Market Analysis")
print(market_result)

print("\nRSI:", round(rsi, 2))
print("Risk:", risk_status)
print("Recommendation:", recommendation)
print("Predicted Price:", prediction)
