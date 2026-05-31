import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
from scripts.backtest_engine import backtest_strategy

from scripts.backtest_chart import backtest_chart

from scripts.forecast_engine import forecast_stock
# =========================================
# Bloomberg Style AI Equity Research Dashboard
# =========================================

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf
import sys
import os

from datetime import datetime


# =========================================
# PATH SETUP
# =========================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "scripts"
        )
    )
)


# =========================================
# IMPORTS
# =========================================

from technical_analysis import technical_analysis
from fundamental_analysis import fundamental_analysis
from news_analysis import news_analysis
from scoring_engine import scoring_engine
from explainability_engine import explainability_engine
from chart_engine import create_chart
from financial_analysis import financial_analysis
from risk_analysis import risk_analysis
from forecast_engine import forecast_stock


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(

    page_title="Terminal",

    page_icon="",

    layout="wide",

    initial_sidebar_state="expanded"

)


# =========================================
# CUSTOM CSS
# =========================================

st.markdown(
    """

<style>

.main {
    background-color: #0e1117;
}

h1,h2,h3,h4 {
    color: white;
}

[data-testid="metric-container"] {
    background-color: #161b22;
    border: 1px solid #30363d;
    padding: 15px;
    border-radius: 12px;
}

.stTextInput input {
    background-color: #161b22;
    color: white;
}

</style>

""",

    unsafe_allow_html=True

)


# =========================================
# HEADER
# =========================================

st.title(
    "Equity Research Terminal"
)

st.caption(
    "Professional AI-Powered Equity Research Platform"
)


# =========================================
# LOAD NSE STOCK DATABASE
# =========================================

stocks_df = pd.read_csv(
    "data/nse_symbols.csv"
)


# =========================================
# SIDEBAR SEARCH
# =========================================

st.sidebar.title(
    "Search Stock"
)


search = st.sidebar.selectbox(

    "Search Indian Company",

    stocks_df["NAME"]

)


# =========================================
# GET STOCK SYMBOL
# =========================================

selected_row = stocks_df[
    stocks_df["NAME"] == search
]


stock = (

    selected_row["SYMBOL"]
    .values[0]

    + ".NS"

)


# =========================================
# FORMAT LARGE NUMBERS
# =========================================

def format_large_number(number):

    try:

        number = float(number)

        if number >= 10000000:

            return f"₹ {number/10000000:.2f} Cr"

        elif number >= 100000:

            return f"₹ {number/100000:.2f} L"

        else:

            return f"{number:,.0f}"

    except:

        return number


# =========================================
# LOAD ANALYSIS
# =========================================

@st.cache_data(ttl=300)

def load_analysis(stock):

    tech = technical_analysis(stock)

    fund = fundamental_analysis(stock)

    news = news_analysis(stock)

    financial = financial_analysis(stock)

    risk = risk_analysis(stock)

    forecast = forecast_stock(stock)

    backtest = backtest_strategy(stock)

    score = scoring_engine(
        tech,
        fund,
        news
    )

    reasons = explainability_engine(
        tech,
        fund,
        news
    )

    return (
        tech,
        fund,
        news,
        financial,
        risk,
        forecast,
        backtest,
        score,
        reasons
    )


# =========================================
# RUN ANALYSIS BUTTON
# =========================================

if st.button("Run Institutional Analysis"):


    with st.spinner("Running AI Equity Research..."):

        tech, fund, news, financial, risk, forecast, backtest, score, reasons = load_analysis(stock)


    # =========================================
    # LIVE HEADER
    # =========================================

    st.subheader(f" {search}")


    top1,top2,top3 = st.columns(3)


    with top1:

        st.metric(

            "Current Price",

            f"₹ {tech['price']}"

        )


    with top2:

        st.metric(

            "AI Recommendation",

            score["recommendation"]

        )


    with top3:

        st.metric(

            "AI Confidence",

            f"{score['ai_score']}%"

        )


    # =========================================
    # INSTITUTIONAL KPI SECTION
    # =========================================

    st.subheader(
        "Institutional Metrics"
    )


    metrics_df = pd.DataFrame({

    "Metric":[

        "Market Cap",
        "PE Ratio",
        "RSI",
        "Sharpe Ratio",
        "Volatility"

    ],


    "Value":[

        format_large_number(
            fund["market_cap"]
        ),

        fund["pe"],

        tech["rsi"],

        risk["sharpe"],

        f'{risk["volatility"]}%'

    ]

})

    st.dataframe(

    metrics_df,

    use_container_width=True,

    hide_index=True

)
    st.markdown("---")


    # =========================================
    # AI SCORE GAUGE
    # =========================================

    st.subheader("AI Equity Score")


    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score["ai_score"],

            title={"text":"Institutional AI Score"},

            gauge={

                "axis":{
                    "range":[0,100]
                },

                "bar":{
                    "color":"cyan"
                },

                "steps":[

                    {
                        "range":[0,40],
                        "color":"red"
                    },

                    {
                        "range":[40,70],
                        "color":"orange"
                    },

                    {
                        "range":[70,100],
                        "color":"green"
                    }

                ]

            }

        )

    )


    gauge.update_layout(

        template="plotly_dark",

        height=350

    )


    st.plotly_chart(

        gauge,

        use_container_width=True

    )


    # =========================================
    # PROFESSIONAL CHART
    # =========================================

    st.subheader("Institutional Technical Analysis")


    fig = create_chart(

        tech["data"],

        stock

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


    # =========================================
    # FORECAST ENGINE
    # =========================================

    st.subheader("Forecast Engine")


    f1,f2,f3 = st.columns(3)


    with f1:

        st.metric(

            "Trend",

            forecast["trend"]

        )


    with f2:

        st.metric(

            "Bullish Probability",

            f"{forecast['bull_prob']}%"

        )


    with f3:

        st.metric(

            "Bearish Probability",

            f"{forecast['bear_prob']}%"

        )


    st.info(

        f'''

Forecasted Price Range:

₹ {forecast['lower']}

to

₹ {forecast['upper']}

'''

    )


    # =========================================
    # INSTITUTIONAL SIGNAL ENGINE
    # =========================================

    st.subheader(
        "Institutional Signal Engine"
    )


    bullish_signals = []

    bearish_signals = []

    neutral_signals = []


    # =========================================
    # SIGNAL CLASSIFICATION
    # =========================================

    if tech["signal"] == "BUY":

        bullish_signals.append(
            "Price structure indicates bullish momentum"
        )

    elif tech["signal"] == "SELL":

        bearish_signals.append(
            "Technical trend remains weak"
        )

    else:

        neutral_signals.append(
            "Market currently trading sideways"
        )


    if tech["macd"] == "Bullish":

        bullish_signals.append(
            "MACD crossover supports upward trend"
        )

    else:

        bearish_signals.append(
            "MACD indicates bearish pressure"
        )


    if tech["rsi"] < 30:

        bullish_signals.append(
            "RSI near oversold zone"
        )

    elif tech["rsi"] > 70:

        bearish_signals.append(
            "RSI indicates overbought conditions"
        )

    else:

        neutral_signals.append(
            "RSI remains in neutral zone"
        )


    if tech["volume"] == "Increasing":

        bullish_signals.append(
            "Institutional participation increasing"
        )

    else:

        bearish_signals.append(
            "Weak trading volume observed"
        )


    # =========================================
    # DISPLAY SIGNALS
    # =========================================

    col1,col2,col3 = st.columns(3)


    with col1:

        st.markdown("Bullish")

        for signal in bullish_signals:

            st.success(signal)


    with col2:

        st.markdown("Bearish")

        for signal in bearish_signals:

            st.error(signal)


    with col3:

        st.markdown("Neutral")

        for signal in neutral_signals:

            st.warning(signal)


    # =========================================
    # AI SUMMARY
    # =========================================

    st.subheader(
        "Institutional AI Summary"
    )


    summary = f'''

    The AI engine currently classifies {stock}
    under a {score["recommendation"]} structure
    with an institutional confidence score of
    {score["ai_score"]}%.

    Technical momentum, volatility structure,
    forecast trend and market participation
    have been evaluated to generate this view.

    '''


    st.info(summary)


        # =========================================
        # NEWS SECTION
        # =========================================

        # =========================================
    # NEWS SENTIMENT ENGINE
    # =========================================

    st.subheader(
        "Institutional News Sentiment"
    )


    news_df = pd.DataFrame({

        "Headline":[
            news["headline"]
        ],

        "Sentiment":[
            "Bullish"
            if score["ai_score"] > 70
            else "Neutral"
        ],

        "Impact":[
            "High"
        ]

    })


    st.dataframe(

        news_df,

        use_container_width=True,

        hide_index=True

    )


    st.markdown("---")


    # =========================================
    # QUANT BACKTEST ENGINE
    # =========================================

    # show_backtest = st.sidebar.checkbox(
    #     "Show Quant Backtesting Results",
    #     value=False
    # )

    # if show_backtest:

    #     st.subheader(
    #     "Quant Backtesting Engine"
    #     )


    # b1,b2,b3 = st.columns(3)


    # with b1:

    #     st.metric(

    #         "Strategy Return",

    #         f'{backtest["strategy_return"]}%'

    #     )


    # with b2:

    #     st.metric(

    #         "Benchmark Return",

    #         f'{backtest["benchmark_return"]}%'

    #     )


    # with b3:

    #     st.metric(

    #         "Sharpe Ratio",

    #         backtest["sharpe"]

    #     )


    # b4,b5 = st.columns(2)


    # with b4:

    #     st.metric(

    #         "Max Drawdown",

    #         f'{backtest["max_drawdown"]}%'

    #     )


    # with b5:

    #     st.metric(

    #         "Win Rate",

    #         f'{backtest["win_rate"]}%'

    #     )


    # # =========================================
    # # EQUITY CURVE
    # # =========================================

    # st.subheader(
    #     "Equity Curve Analysis"
    # )


    # backtest_fig = backtest_chart(

    #     backtest["data"]

    # )


    # st.plotly_chart(

    #     backtest_fig,

    #     use_container_width=True

    # )


        # =========================================
        # FOOTER
        # =========================================

    st.markdown("---")


    st.caption(

            "Built by Mandar Nikam"

        )
