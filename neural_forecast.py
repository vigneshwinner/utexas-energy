import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import NeuralForecast components
from neuralforecast.models import NBEATS
from neuralforecast.core import NeuralForecast

# Step 1: Simulate energy price data (e.g., daily crude oil prices)
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
prices = 80 + np.cumsum(np.random.normal(0, 0.5, size=len(dates)))  # Base price with noise

# Step 2: Format data for NeuralForecast
df = pd.DataFrame({
    'unique_id': ['oil'] * len(dates),
    'ds': dates,
    'y': prices
})

# Step 3: Create the forecasting model
model = NBEATS(h=7, input_size=14, max_steps=300)  # Predict 7 days ahead using 14 past days
nf = NeuralForecast(models=[model], freq='D')

# Step 4: Fit the model
nf.fit(df)

# Step 5: Generate forecasts
forecast = nf.predict()

# Step 6: Print forecast values
print("\n Forecasted Energy Prices for the Next 7 Days:\n")
print(forecast)

# Step 7: Plot actual + forecasted prices
plt.figure(figsize=(10, 5))
plt.plot(df['ds'], df['y'], label='Historical Prices', linewidth=2)
plt.plot(forecast['ds'], forecast['NBEATS'], label='7-Day Forecast', linestyle='--', marker='o', color='orange')
plt.title('Energy Price Forecast (NBEATS)')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()