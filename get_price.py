import sys
import requests

def get_price(symbol: str) -> float:
    """Fetch the current market price for the given symbol from Yahoo Finance."""
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    result = data.get("quoteResponse", {}).get("result", [])
    if not result:
        raise ValueError(f"Symbol {symbol} not found")
    return result[0].get("regularMarketPrice")

def main():
    if len(sys.argv) != 2:
        print("Usage: python get_price.py SYMBOL")
        sys.exit(1)
    symbol = sys.argv[1]
    try:
        price = get_price(symbol)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    print(f"Current price for {symbol}: {price}")

if __name__ == "__main__":
    main()
