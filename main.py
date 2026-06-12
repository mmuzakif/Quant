import yfinance as yf

data = yf.download("BBRI.JK",period="1mo")
print(data.head())
