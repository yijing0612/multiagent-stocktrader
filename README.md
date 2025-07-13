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
  - OpenAI GPT 
  - Postgre Database 
  - Redis

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

### 3. Run the Simulation

```bash
python main.py
```

Simulation results and logs will be printed to the console and optionally saved in the results/ directory.

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
