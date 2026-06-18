from sklearn.linear_model import LinearRegression
import numpy as np

class ForecastModel:

    def forecast(self, data):

        close = data["Close"].values

        x = np.arange(len(close)).reshape(-1, 1)

        y = close

        model = LinearRegression()

        model.fit(x, y)

        future_day = np.array([[len(close) + 1]])

        prediction = model.predict(future_day)

        return round(prediction[0], 2)
