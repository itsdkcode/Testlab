# Testlab

This repository contains a simple script for fetching stock prices from Yahoo Finance.

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with a stock symbol to print the current price:

```bash
python get_price.py AAPL
```

### Run as a web service

Start a simple Flask server that exposes the price endpoint:

```bash
python server.py
```

The server listens on port `5000` by default. Set the `PORT` environment
variable to change it.

Once running, fetch prices via HTTP:

```bash
curl "http://localhost:5000/price?symbol=AAPL"
```

### Docker

You can build a Docker image for deployment:

```bash
docker build -t price-app .
docker run -p 5000:5000 price-app
```
