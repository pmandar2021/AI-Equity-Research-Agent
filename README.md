# AI Equity Research Agent
## Quantitative Equity Research Platform for Indian Markets
## Dashboard Preview

### Bloomberg-Style Search Terminal

![Search Terminal](Screenshots/Search%20Terminal.png)

---

### Technical Analysis Dashboard

![Technical Analysis](Screenshots/Technical%20Analysis.png)

---

### Technical Indicators & Market Signals

![Technical Indicator](Screenshots/Technical%20Indicator.png)

---

### Forecast Engine

![Forecast Engine](Screenshots/Forecast%20Engine.png)

---

###  Institutional Signal Engine

![Institutional Signal](Screenshots/Institutional%20Signal.png)

---

### AI Summary & News Analysis

![AI Summary](Screenshots/AI%20Summary%20and%20News%20Analysis.png)
 

End-to-end quantitative equity research platform combining technical analysis, fundamental screening, multi-factor ranking, portfolio construction, and historical backtesting — built for data-driven investment decisions on Indian equities (NSE/BSE).
 
What This Project Does
Most retail investors rely on isolated indicators and gut feel. This platform brings institutional-grade quant research to individual stock analysis by combining:
Layer	What It Solves
Technical Analysis	Identify momentum, trend, and mean-reversion signals
Fundamental Analysis	Screen for quality, value, and growth characteristics
Factor Engine	Rank stocks using composite multi-factor scores
Portfolio Construction	Build risk-managed, diversified portfolios
 
 Key Features
Technical Analysis Engine
•	RSI, Moving Averages (SMA/EMA), Bollinger Bands
•	Trend identification, momentum scoring, volatility metrics
•	Cross-sectional signal generation across a stock universe
Fundamental Analysis Engine
•	Market cap, P/E ratio, ROE, revenue growth, debt-to-equity
•	Business quality assessment and financial health scoring
•	Data sourced via yFinance for real-time and historical fundamentals
Quantitative Factor Framework
•	Factor Engine: Computes momentum, quality, growth, and risk factors
•	Multi-Factor Ranking Model: Cross-sectional composite scoring
•	Portfolio Constructor: Selects top-ranked stocks with position sizing logic
•	Risk Framework: Volatility-adjusted allocation, drawdown controls
Interactive Streamlit Dashboard
•	Real-time stock screening and ranking
•	Portfolio visualizations with Plotly charts
•	Factor exposure analysis and performance analytics
•	Investment research output in a clean, shareable UI
 
System Architecture
Raw Stock Data (yFinance)
        ↓
Technical Signals  ←→  Fundamental Metrics
        ↓
    Factor Engine
        ↓
   Ranking Engine  (Cross-Sectional Composite Score)
        ↓
Portfolio Construction  (Position Sizing + Risk Controls)
        ↓
  Research Dashboard  (Streamlit + Plotly)
 
Tech Stack
Category	Tools
Language	Python 3.10+
Dashboard	Streamlit
Data & Analysis	Pandas, NumPy
Visualization	Plotly
Financial Data	yFinance
Statistical Analysis	Statsmodels
Version Control	Git, GitHub
 
Project Structure
AI-Equity-Research-Agent/
├── app/
│   └── dashboard.py              # Streamlit UI
├── scripts/
│   ├── technical_analysis.py     # RSI, MA, momentum signals
│   ├── factor_engine.py          # Factor computation
│   ├── factor_ranking_engine.py  # Cross-sectional ranking
│   ├── portfolio_constructor.py  # Portfolio building logic
│   ├── backtest_engine.          # Historical backtesting
│   ├── strategy_optimizer.py     # Parameter optimization
│   └── walk_forward_backtest.py  # Out-of-sample validation
├── charts/                       # Generated output charts
├── data/                         # Cached price/fundamental data
├── requirements.txt
└── README.md
 
 Getting Started
# Clone the repository
git clone https://github.com/pmandar2021/AI-Equity-Research-Agent.git
cd AI-Equity-Research-Agent

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run app/dashboard.py
 
Research Highlights
Walk-Forward Validation — Unlike simple backtests, this platform tests strategy parameters on rolling out-of-sample windows, providing a realistic estimate of live performance.
Multi-Factor Ranking — Stocks are scored across Momentum, Quality, Growth, and Risk dimensions. The composite score drives portfolio construction, similar to methodologies used by systematic hedge funds.
Strategy Optimization — Parameter sweep framework evaluates signal configurations across different market conditions, identifying robust setups rather than curve-fitted ones.
 
Roadmap
•	[ ] Monthly rebalancing engine with transaction cost modeling
•	[ ] Alpha & Beta attribution vs Nifty benchmark
•	[ ] Machine learning factor models (XGBoost, Random Forest)
•	[ ] Mean-variance portfolio optimization (Markowitz framework)
•	[ ] Factor attribution analysis (Fama-French style)
•	[ ] Institutional portfolio simulation
 
Skills Demonstrated
Equity Research · Quantitative Finance · Factor Investing · Portfolio Construction · Risk Management · Algorithmic Trading · Financial Modelling · Python · Data Analysis · Backtesting · Streamlit · Statistical Analysis · NSE/BSE Markets
 
Author
Mandar Nikam MBA — Business Analytics | CFA Level I Passed
Passionate about quantitative finance, systematic investing, equity research, and building data-driven tools for capital markets.
