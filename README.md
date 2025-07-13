# Multi-Agent Stock Trader

Multi-Agent Stock Trader is a simulation framework designed to evaluate and compare various trading strategies across multiple autonomous agents. The project provides an environment where different stock trading agents, each employing distinct methodologies, interact with a simulated market using historical stock data.

---

## 🔧 Key Features

- **Multi-Agent Framework**  
  Simulate and analyze the behavior of multiple trading agents operating concurrently in a unified market environment.

- **Agent Strategy Evaluation**  
  Compare different algorithmic trading strategies by running simulations under identical market conditions, facilitating performance benchmarking.

- **Data-Driven Simulations**  
  Leverage historical stock data to drive realistic market scenarios, enabling rigorous backtesting and strategy validation.

- **Modular Architecture**  
  Designed with modular components to allow easy integration of new trading strategies or agents, as well as customization of market parameters.

---

## 📌 Use Cases

- **Strategy Research**  
  Serve as a research tool for testing and evaluating algorithmic trading strategies in a controlled, simulated market.

- **Educational Platform**  
  Provide a hands-on environment for students and enthusiasts to learn about multi-agent systems and stock trading dynamics.

- **Performance Benchmarking**  
  Enable developers to compare the efficacy of various trading rules and execution strategies in a consistent simulation framework.

---

## 🛠 Tech Stack

- **Programming Language:** Python  
- **Libraries:**  
  - `pandas`, `numpy` – Data processing and numerical computations  
  - `matplotlib`, `seaborn` – Visualization of trading performance  
  - Standard Python libraries for file handling and agent control

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yijing0612/multiagent-stocktrader.git
cd multiagent-stocktrader
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare the Dataset

Place your historical stock price data in the data/ directory.
Ensure the data files follow a consistent format, such as:

```bash
Date,Open,High,Low,Close,Volume
2022-01-01,100,105,95,102,1000000
...
```

### 4. Run the Simulation

```bash
python main.py
```

Simulation results and logs will be printed to the console and optionally saved in the results/ directory.

---

## ⚙️ Configuration

You can modify simulation settings in `config.py` (if available) or directly within the codebase:

- **Agent Settings** – Define number and type of agents  
- **Trading Rules** – Set buy/sell thresholds, holding limits, etc.  
- **Market Settings** – Configure time periods, stock selection, and initial capital

---

## 📊 Outputs

After running simulations, the framework will generate:

- **Agent Performance Metrics** – Total return, volatility, win rate, etc.  
- **Portfolio Value Plots** – Line graphs showing portfolio value over time  
- **Trade Logs** – CSV logs of buy/sell actions and portfolio state  

Visualizations can be found in the `plots/` or `results/` folder.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Add new agent strategies  
- Improve data preprocessing or analysis  
- Refactor code for scalability or performance  

Please open an issue or submit a pull request for proposed changes.
