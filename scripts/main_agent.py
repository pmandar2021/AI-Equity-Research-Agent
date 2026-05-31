# =========================================
# AI Equity Research Agent
# Main Controller
# =========================================

# Import modules

from technical_analysis import technical_analysis
from fundamental_analysis import fundamental_analysis
from news_analysis import news_analysis
from scoring_engine import scoring_engine
from explainability_engine import explainability_engine


print("\n================================")

print(" AI EQUITY RESEARCH AGENT ")

print("================================")


stock=input(
    "\nEnter stock symbol: "
).strip().upper()


print("\nRunning Technical Analysis...")

tech=technical_analysis(stock)


print("\nRunning Fundamental Analysis...")

fund=fundamental_analysis(stock)

print("\nRunning News Analysis...")

news = news_analysis(stock)

print("\nCalculating AI Score...")

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

print("\n================================")

print("FINAL AI REPORT")

print("================================")


print(
"\nTechnical Score:",
score["technical_score"],
"/100"
)

print(
"Fundamental Score:",
score["fundamental_score"],
"/100"
)

print(
"News Score:",
score["news_score"],
"/100"
)

print(
"\nFinal AI Score:",
score["ai_score"],
"/100"
)

print(
"\nRecommendation:"
)

print(
score["recommendation"]
)

print("\nReasons")

for reason in reasons:

    print(reason)