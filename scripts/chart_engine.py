# =========================================
# Professional Chart Engine
# =========================================

import plotly.graph_objects as go
from plotly.subplots import make_subplots


# =========================================
# Create chart
# =========================================

def create_chart(data, stock):

    # Create subplots

    fig = make_subplots(

        rows=3,
        cols=1,

        shared_xaxes=True,

        vertical_spacing=0.03,

        row_heights=[0.6, 0.2, 0.2],

        subplot_titles=(

            f"{stock} Price",
            "RSI",
            "MACD"

        )

    )


    # =========================================
    # Candlestick chart
    # =========================================

    fig.add_trace(

        go.Candlestick(

            x=data.index,

            open=data["Open"],

            high=data["High"],

            low=data["Low"],

            close=data["Close"],

            increasing_line_color="green",

            decreasing_line_color="red",

            name="Price"

        ),

        row=1,
        col=1

    )


    # =========================================
    # Moving averages
    # =========================================

    fig.add_trace(

        go.Scatter(

            x=data.index,

            y=data["MA20"],

            line=dict(
                color="orange",
                width=2
            ),

            name="MA20"

        ),

        row=1,
        col=1

    )


    fig.add_trace(

        go.Scatter(

            x=data.index,

            y=data["MA50"],

            line=dict(
                color="blue",
                width=2
            ),

            name="MA50"

        ),

        row=1,
        col=1

    )


    # =========================================
    # RSI
    # =========================================

    fig.add_trace(

        go.Scatter(

            x=data.index,

            y=data["RSI"],

            line=dict(
                color="purple"
            ),

            name="RSI"

        ),

        row=2,
        col=1

    )


    # Overbought / oversold

    fig.add_hline(

        y=70,

        line_dash="dash",

        line_color="red",

        row=2,
        col=1

    )


    fig.add_hline(

        y=30,

        line_dash="dash",

        line_color="green",

        row=2,
        col=1

    )


    # =========================================
    # MACD
    # =========================================

    fig.add_trace(

        go.Scatter(

            x=data.index,

            y=data["MACD"],

            line=dict(
                color="cyan"
            ),

            name="MACD"

        ),

        row=3,
        col=1

    )


    fig.add_trace(

        go.Scatter(

            x=data.index,

            y=data["Signal_Line"],

            line=dict(
                color="yellow"
            ),

            name="Signal"

        ),

        row=3,
        col=1

    )


    # =========================================
    # Layout
    # =========================================

    fig.update_layout(

        template="plotly_dark",

        height=900,

        xaxis_rangeslider_visible=False,

        hovermode="x unified",

        title=f"{stock} Technical Analysis",

        legend=dict(
            orientation="h"
        )

    )


    return fig