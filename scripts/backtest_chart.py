
# =========================================
# Backtest Visualization Engine
# =========================================

import plotly.graph_objects as go


# =========================================
# Equity Curve Chart
# =========================================

def backtest_chart(data):


    fig = go.Figure()


    # =========================================
    # Strategy Curve
    # =========================================

    fig.add_trace(

        go.Scatter(

            x=data.index,

            y=data["Cumulative_Strategy"],

            mode="lines",

            name="Quant Strategy",

            line=dict(
                color="cyan",
                width=3
            )

        )

    )


    # =========================================
    # Benchmark Curve
    # =========================================

    fig.add_trace(

        go.Scatter(

            x=data.index,

            y=data["Cumulative_Market"],

            mode="lines",

            name="Buy & Hold",

            line=dict(
                color="orange",
                width=2
            )

        )

    )


    # =========================================
    # Layout
    # =========================================

    fig.update_layout(

        template="plotly_dark",

        height=600,

        title="Quant Strategy vs Buy & Hold",

        xaxis_title="Date",

        yaxis_title="Growth of ₹1",

        hovermode="x unified"

    )


    return fig

