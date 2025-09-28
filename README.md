# Stock Market Time Series Analysis with Pandas

| Project Status | License | Environment |
| :--- | :--- | :--- |
| **Active Development** | [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) | [![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) |

## Introduction & Project Vision

Welcome to **`stock-time-series-analysis-with-pandas`**!

This repository serves as a **beginner-to-intermediate friendly, step-by-step guide** to mastering financial time series analysis using the powerful capabilities of the **Pandas** library in Python. Our approach is uniquely focused on **Data Exploration, Pandas Mastery, and Storytelling through Visualization**, providing deep, actionable insights without relying on complex Machine Learning models.

### **Focus Areas**

* **Pandas Mastery:** Deep-dive into time-series specific functions like Indexing, Slicing, `.resample()`, and `.rolling()`.
* **Financial Metrics:** Accurate calculation and interpretation of Returns, Volatility, and Liquidity.
* **Visualization:** Using `matplotlib`, `seaborn`, and `plotly` to create powerful, insightful financial charts.
* **Storytelling:** Every analysis is accompanied by clear, educational markdown explanations and final business-like conclusions.

---

## Repository Structure

The project is organized as a sequential learning path via Jupyter Notebooks.

```
stock-time-series-analysis-with-pandas/
│
├── README.md                 <- This file
├── LICENSE                   <- Project's MIT License
├── requirements.txt          <- All necessary dependencies (frozen versions)
├── data/                     <- Local storage for downloaded CSVs (ignored by git)
└── notebooks/
├── 01_fetch_inspect_data.ipynb
├── 02_working_with_datetime.ipynb
├── 03_visualize_stock_prices.ipynb
├── 04_returns_and_log_returns.ipynb
├── 05_resampling_and_trends.ipynb
├── 06_rolling_statistics_moving_averages.ipynb
├── 07_volume_analysis.ipynb
├── 08_multi_stock_comparison.ipynb
├── 09_manual_technical_indicators.ipynb
└── 10_case_study_end_to_end.ipynb (Capstone)
```

---

## Getting Started

To run the notebooks locally, follow these steps.

### **1. Prerequisites**

* **Python:** Version 3.8 or higher.
* **Git:** For cloning the repository.

### **2. Setup Instructions**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/prakash-ukhalkar/stock-time-series-analysis-with-pandas.git
    
    cd stock-time-series-analysis-with-pandas
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    # Using venv (standard Python)
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch Jupyter:**
    ```bash
    jupyter notebook
    # OR
    jupyter lab
    ```

### **3. Running the Analysis**

Start with the notebook `01_fetch_inspect_data.ipynb` and proceed sequentially through the numbered files in the `notebooks/` directory.

---

## Notebooks: A Detailed Roadmap

| Notebook | Title | Key Learning Outcomes |
| :--- | :--- | :--- |
| **01** | **Data Loading & Inspection** | Fetching live data (`yfinance`), initial data quality checks (`.isna()`), understanding data columns. |
| **02** | **Indexing and Time Slicing** | Converting and setting the DateTime Index, powerful time-based slicing (`df['YYYY']`), extracting time features (weekday, month). |
| **03** | **Powerful Time Series Plots** | Line plots, dual-axis plots, introductory interactive **Candlestick Charts** (`Plotly`), and event annotation. |
| **04** | **Percent & Log Returns** | Calculating Daily Returns, Cumulative Returns, Log Returns, and analyzing return distribution (volatility, skewness, kurtosis). |
| **05** | **Resampling and Trends** | Aggregating data across time periods (`.resample('W')`, `'M'`), applying aggregation functions (`.mean()`, `.ohlc()`), and trend visualization. |
| **06** | **Rolling Statistics** | Computing Rolling Mean (SMA) and Rolling Standard Deviation (Volatility), identifying moving average crossovers. |
| **07** | **Volume and Liquidity Analysis** | Analyzing volume trends, calculating **Volume-Weighted Average Price (VWAP)**, and high-volume anomaly detection. |
| **08** | **Multi-Stock Comparison** | Normalizing multiple stocks for comparison, analyzing relative performance, and calculating/visualizing return correlation. |
| **09** | **Manual Technical Indicators** | Programming fundamental indicators (SMA, EMA, Bollinger Bands, RSI) entirely with Pandas (`.ewm()`). |
| **10** | **Case Study: End-to-End** | A capstone project covering data loading to final business conclusion, including key risk metrics like **Maximum Drawdown**. |

---

## Dependencies (`requirements.txt`)

The core libraries used are:
* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`
* `plotly`
* `yfinance`
* `scipy`

---

#### Contributions

Contributions are welcome! If you'd like to improve examples, add topics, or fix something, feel free to open a pull request.

Happy Learning!

---

## Author

**stock-time-series-analysis-with-pandas** is created and maintained by [**Prakash Ukhalkar**](https://github.com/prakash-ukhalkar)

---

<div align="center">
  <sub>Built with ❤️ for the Python community</sub>
</div>

