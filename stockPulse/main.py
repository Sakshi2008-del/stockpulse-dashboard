from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import yfinance as yf

app = FastAPI(title="StockPulse API")

# Homepage
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>StockPulse Dashboard</title>
        <style>
            body{
                margin:0;
                padding:0;
                font-family:Arial, sans-serif;
                background:linear-gradient(135deg,#0f172a,#1e293b);
                color:white;
                text-align:center;
            }

            .container{
                margin-top:70px;
            }

            h1{
                font-size:55px;
                margin-bottom:10px;
            }

            p{
                font-size:24px;
                color:#cbd5e1;
                margin-bottom:40px;
            }

            .box{
                width:60%;
                margin:auto;
                background:#111827;
                padding:35px;
                border-radius:18px;
                box-shadow:0 0 20px rgba(0,0,0,0.4);
            }

            a{
                display:block;
                margin:18px;
                padding:18px;
                background:#38bdf8;
                color:black;
                text-decoration:none;
                font-size:24px;
                border-radius:12px;
                font-weight:bold;
                transition:0.3s;
            }

            a:hover{
                background:#0ea5e9;
                transform:scale(1.03);
            }

            footer{
                margin-top:40px;
                font-size:18px;
                color:#94a3b8;
            }

        </style>
    </head>

    <body>

        <div class="container">
            <h1>📈 StockPulse</h1>
            <p>Intelligent Stock Data Dashboard</p>

            <div class="box">
                <a href="/companies">📌 View Companies</a>
                <a href="/summary/INFY">📊 INFY Stock Summary</a>
                <a href="/data/INFY">📅 Last 30 Days Data</a>
                <a href="/compare?symbol1=INFY&symbol2=TCS">⚖ Compare INFY vs TCS</a>
                <a href="/docs">📘 API Documentation</a>
            </div>

            <footer>
                Built with FastAPI + Python + Yahoo Finance
            </footer>
        </div>

    </body>
    </html>
    """

# Companies API
@app.get("/companies")
def companies():
    return {
        "INFY": "Infosys",
        "TCS": "Tata Consultancy Services",
        "RELIANCE": "Reliance Industries",
        "ITC": "ITC Limited",
        "HDFCBANK": "HDFC Bank"
    }

# Summary API
@app.get("/summary/{symbol}")
def summary(symbol: str):
    stock = yf.Ticker(symbol + ".NS")
    df = stock.history(period="1y")

    return {
        "symbol": symbol,
        "52_week_high": round(df["High"].max(), 2),
        "52_week_low": round(df["Low"].min(), 2),
        "average_close": round(df["Close"].mean(), 2)
    }

# Data API
@app.get("/data/{symbol}")
def data(symbol: str):
    stock = yf.Ticker(symbol + ".NS")
    df = stock.history(period="30d")

    result = []

    for index, row in df.iterrows():
        result.append({
            "date": str(index.date()),
            "close": round(row["Close"], 2)
        })

    return result

# Compare API
@app.get("/compare")
def compare(symbol1: str, symbol2: str):
    stock1 = yf.Ticker(symbol1 + ".NS")
    stock2 = yf.Ticker(symbol2 + ".NS")

    df1 = stock1.history(period="30d")
    df2 = stock2.history(period="30d")

    return {
        symbol1: round(df1["Close"].iloc[-1], 2),
        symbol2: round(df2["Close"].iloc[-1], 2)
    }
