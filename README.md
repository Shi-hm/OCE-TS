# **OCE-TS**

### *Beyond MSE: Ordinal Cross-Entropy for Probabilistic Time Series Forecasting*

OCE-TS is a novel probabilistic time series forecasting framework that replaces traditional Mean Squared Error (MSE) regression with an Ordinal Cross-Entropy (OCE) classification paradigm. The method provides more stable optimization, improved robustness, and inherent uncertainty estimation across multiple benchmark datasets.

---

## 🚀 Features

* **Probabilistic forecasting** with uncertainty estimation
* **Ordinal Cross-Entropy (OCE) loss** to preserve temporal ordering
* **Robust to noise** and outliers
* **Supports multiple datasets** (ETTh, ETTm, Exchange, Weather, ILI, etc.)
* **Lightweight backbone** based on DLinear

---

## 📦 Environment & Requirements

This project was implemented in the following environment:

* Python **3.8.20**
* PyTorch **2.0.0** (CUDA 11.8)
* GPU: **NVIDIA RTX 4060**
* CPU: **Intel i7-14700F**
* RAM: **16 GB**

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🏃 Usage

### **Run (Train + Test)**
Running the script below will automatically perform both training and testing:

```bash
python run_longExp.py

MyLinear/
│── Da/ # Data augmentation or auxiliary data
│── data_provider/ # Data loading and preprocessing
│── dataset/ # Dataset files and utilities
│── exp/ # Experiment manager (training/testing)
│── layers/ # Model layers
│── logs/ # Training logs
│── loss/ # Loss functions (OCE, CE, Gaussian, etc.)
│── models/ # Forecasting models (DLinear, OCE-TS modules)
│── results/ # Result figures, MAE/MSE plots, tables
│── scripts/ # Helper scripts / run scripts
│── test_results/ # Saved test outputs
│── utils/ # Utility functions (Gaussian, noise, lookback, etc.)
│
│── distribution.py
│── Gaussian.py
│── lookback.py
│── loss_compare.py
│── ModelComparisonPlot.py
│── noise.py
│── OCE vs CE.py
│── Parameter.py
│── Probability Distribution Comparison.py
│── run_longExp.py # Main entry script (train+test)
│── sh.py
│── result.txt
│── *.png # Visualization images


---

## 📊 Results

Our method (OCE-TS) consistently outperforms strong baselines such as  
Autoformer, DLinear, iTransformer, TimeXer, and TimeBridge across multiple datasets.

For detailed experimental results, tables, and comparisons,  
**please refer to the paper**.


## 📚 Citation

If you use this repository, please cite:

```bibtex
@misc{wang2025mseordinalcrossentropyprobabilistic,
	title={Beyond MSE: Ordinal Cross-Entropy for Probabilistic Time Series Forecasting}, 
	author={Jieting Wang and Huimei Shi and Feijiang Li and Xiaolei Shang},
	year={2025},
	eprint={2511.10200},
	archivePrefix={arXiv},
	primaryClass={cs.LG},
	url={https://arxiv.org/abs/2511.10200}, 
}
```

---

## 📄 License

MIT License

---
