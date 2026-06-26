# Credit Card Risk Detection

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-2563EB?logo=python&logoColor=white)](requirements.txt)
[![Maintained by UIbit](https://img.shields.io/badge/Maintained%20by-UIbit-10B981)](https://github.com/UIbit)

Machine learning project for detecting fraudulent credit card transactions using classical ML algorithms on the [Kaggle Credit Card Fraud dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).

---

## About This Project

Credit card fraud causes billions in losses every year. **Credit Card Risk Detection** compares four supervised learning models to flag suspicious transactions early, with clear metrics and visualizations in Jupyter notebooks.

Built and maintained by **[UIbit](https://github.com/UIbit)** as a practical ML portfolio project focused on imbalanced classification and model comparison.

## Features

- End-to-end workflow: load data, preprocess, train, evaluate
- Four algorithms: KNN, SVM, Logistic Regression, Decision Tree
- Class imbalance handling (under-sampling / over-sampling)
- Confusion matrices, ROC curves, and precision-recall plots
- Shared **UIbit** plot theme for consistent notebook visuals

## Quick Start

```bash
git clone https://github.com/UIbit/Credit-Card-Risk-Detection.git
cd Credit-Card-Risk-Detection
pip install -r requirements.txt
```

1. Download [`creditcard.csv`](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) from Kaggle.
2. Place the file in the `notebook/` folder.
3. Open any notebook in `notebook/` and run all cells.

## Project Structure

```
Credit-Card-Risk-Detection/
├── README.md
├── LICENSE
├── requirements.txt
└── notebook/
    ├── README.md
    ├── plot_style.py          # Shared UIbit chart styling
    ├── K-Nearest Neighbor.ipynb
    ├── Support Vector Machines.ipynb
    ├── Logistic Regression.ipynb
    └── Decision Tree.ipynb
```

## Dataset

| Feature | Description |
|---------|-------------|
| **Time** | Seconds since the first transaction |
| **V1–V28** | PCA-transformed features (anonymized) |
| **Amount** | Transaction amount |
| **Class** | `0` = legitimate, `1` = fraudulent |

The dataset contains **284,807** transactions from European cardholders (September 2013). Fraud cases are heavily under-represented (~0.17%).

## Model Results

| Algorithm | Accuracy |
|-----------|----------|
| K-Nearest Neighbors | ~100% |
| Decision Tree | ~100% |
| Support Vector Machine | 97.59% |
| Logistic Regression | 93.51% |

> Results are from the original notebook experiments. Always validate on held-out data before production use.

## Methodology

1. **Preprocessing** — clean missing values, scale `Time` and `Amount`, balance classes
2. **Training** — train/test split, fit each model
3. **Evaluation** — accuracy, precision, recall, F1, confusion matrix
4. **Comparison** — pick the strongest approach for this dataset

## Roadmap

- [ ] Random Forest & Gradient Boosting benchmarks
- [ ] Cross-validation and hyperparameter tuning
- [ ] Flask/Streamlit demo for live scoring
- [ ] Real-time inference pipeline

## Contributing

Issues and pull requests are welcome. Please open an issue first for larger changes.

## License

Apache License 2.0 — see [LICENSE](LICENSE).

## Author

**UIbit** — [github.com/UIbit](https://github.com/UIbit)  
Repository: [UIbit/Credit-Card-Risk-Detection](https://github.com/UIbit/Credit-Card-Risk-Detection)
