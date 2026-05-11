# Financial News Sentiment Analysis for Stock Market Prediction

## Overview

This project analyzes the relationship between financial news sentiment and stock market movements. By combining Natural Language Processing (NLP) techniques with quantitative financial analysis, the project aims to determine whether news headlines can help predict future stock price behavior.

The project was developed as part of the Nova Financial Solutions analytics challenge.

---

## Business Objective

Financial markets react rapidly to news. Some headlines significantly influence investor sentiment and market prices, while others have little impact.

This project aims to:

- Quantify sentiment from financial news headlines
- Compute technical indicators from historical stock prices
- Measure correlations between sentiment and stock returns
- Generate actionable insights for predictive investment strategies

---

## Project Goals

### Task 1 — Exploratory Data Analysis (EDA)

- Analyze headline lengths and publication frequency
- Identify top publishers and publishing trends
- Extract common keywords and topics from headlines
- Visualize news activity over time

### Task 2 — Quantitative Financial Analysis

- Compute technical indicators using TA-Lib
- Analyze stock price trends and momentum
- Visualize market behavior using RSI, MACD, SMA, and EMA

### Task 3 — Sentiment & Correlation Analysis

- Perform sentiment analysis on financial headlines
- Align news publication dates with stock trading dates
- Calculate daily stock returns
- Measure Pearson correlation between sentiment and returns
- Develop insights for investment strategy recommendations

---
### Project Structure
```
news-driven-stock-analysis/
├── .github/
│   └── workflows/
│       └── unittests.yml
├── notebooks/
│   ├── __init__.py
│   ├── aapl_quantitative_analysis.ipynb
│   ├── amzn_quantitative_analysis.ipynb
│   ├── eda.ipynb
│   ├── google_quantitative_analysis.ipynb
│   ├── meta_quantitative_analysis.ipynb
│   └── nvda_quantitative_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   └── data_loader.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
---

# Dataset Description

## Financial News Dataset

The news dataset contains:

| Column | Description |
|---|---|
| headline | News article headline |
| url | Link to article |
| publisher | Article publisher |
| date | Publication timestamp |
| stock | Stock ticker symbol |

---

## Historical Stock Price Dataset

The stock dataset includes:

| Column | Description |
|---|---|
| Date | Trading date |
| Open | Opening price |
| High | Highest price |
| Low | Lowest price |
| Close | Closing price |
| Adj Close | Adjusted closing price |
| Volume | Trading volume |

---

# Technologies Used

## Programming Language

- Python 3.11

## Data Analysis

- pandas
- numpy

## Visualization

- matplotlib
- seaborn

## NLP & Sentiment Analysis

- nltk
- TextBlob
- VADER Sentiment

## Financial Analysis

- TA-Lib
- PyNance
- yfinance

## Machine Learning / NLP

- scikit-learn

## Development Tools

- Git
- GitHub
- GitHub Actions
- Jupyter Notebook
- pytest

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd news-sentiment-analysis
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the notebooks directory and run:

- `eda.ipynb`
- all `quantitative_analysis.ipynb` for all companies

---

# Technical Indicators Implemented

The following indicators are used in the analysis:

## Simple Moving Average (SMA)

Used to identify trend direction.

## Exponential Moving Average (EMA)

Gives more weight to recent prices.

## Relative Strength Index (RSI)

Used to identify overbought and oversold conditions.

## Moving Average Convergence Divergence (MACD)

Used to detect momentum and trend reversals.

---

# Sentiment Analysis Methodology

The project uses VADER and TextBlob sentiment analyzers to assign sentiment scores to news headlines.

Sentiment categories:

| Score Range | Sentiment |
|---|---|
| > 0 | Positive |
| = 0 | Neutral |
| < 0 | Negative |

Daily sentiment scores are aggregated per stock symbol and compared against daily stock returns.

---

# Correlation Analysis

Daily stock returns are calculated using:

:contentReference[oaicite:0]{index=0}

Pearson correlation is then computed between:

- Average daily sentiment scores
- Daily percentage stock returns

The goal is to evaluate whether positive or negative news sentiment correlates with future stock movement.

---

# Key Features

- Financial news sentiment analysis
- Stock technical indicator computation
- Correlation analysis between sentiment and returns
- Publication trend analysis
- Topic modeling and keyword extraction
- Automated CI/CD pipeline with GitHub Actions

---

# CI/CD Pipeline

The project uses GitHub Actions for continuous integration.

The pipeline automatically:

- Installs dependencies
- Runs unit tests
- Validates notebooks
- Ensures reproducibility

Workflow file:

```bash
.github/workflows/unittests.yml
```

---

# Testing

Run tests using:

```bash
pytest tests/
```

---

# Example Visualizations

The project includes:

- News publication frequency over time
- Top publishers analysis
- Word clouds and TF-IDF keyword plots
- Stock prices with moving averages
- RSI and MACD charts
- Sentiment vs stock return scatter plots
- Correlation heatmaps

---

# Challenges & Limitations

- Financial headlines may be ambiguous
- Correlation does not imply causation
- Market movement depends on many external variables
- News timing and after-hours releases can affect alignment
- Sentiment models may misinterpret financial language

---

# Future Improvements

- Use transformer-based sentiment models (FinBERT)
- Incorporate intraday stock data
- Build predictive ML models
- Add event-driven trading simulations
- Deploy dashboards using Streamlit

---

# Contributors

- Melkishi Tesfaye

---

# References

## NLP

- NLTK Documentation
- TextBlob Documentation

## Technical Analysis

- TA-Lib Documentation
- PyNance Documentation

## CI/CD

- GitHub Actions Documentation

---

# License

This project is for educational and research purposes.
