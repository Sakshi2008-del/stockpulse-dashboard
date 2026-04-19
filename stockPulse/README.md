# StockPulse - Stock Data Intelligence Dashboard

## Overview
StockPulse is a mini stock market data platform built using FastAPI and Python. It provides real-time stock insights using Yahoo Finance data.

## Features
- List available companies
- Last 30 days stock data
- 52-week high/low summary
- Compare two stocks
- Interactive API docs

## Tech Stack
- Python
- FastAPI
- yfinance
- Uvicorn

## Run Project

uvicorn main:app --reload

## Endpoints
- /companies
- /data/{symbol}
- /summary/{symbol}
- /compare?symbol1=INFY&symbol2=TCS
- /docs
