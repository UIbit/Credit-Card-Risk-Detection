# Notebooks — Credit Card Risk Detection

Interactive Jupyter notebooks for comparing fraud detection models.  
Maintained by **[UIbit](https://github.com/UIbit)**.

## Notebooks

| Notebook | Algorithm | Highlights |
|----------|-----------|------------|
| `K-Nearest Neighbor.ipynb` | KNN | K-value tuning, error-rate plot |
| `Support Vector Machines.ipynb` | SVM | ROC & precision-recall curves |
| `Logistic Regression.ipynb` | Logistic Regression | Baseline linear classifier |
| `Decision Tree.ipynb` | Decision Tree | Tree visualization |

## Setup

```bash
pip install -r ../requirements.txt
jupyter notebook
```

Place `creditcard.csv` in this folder before running.

## Visual Theme

Charts use the shared UIbit palette from `plot_style.py`:

```python
from plot_style import apply_uibit_theme, COLORS
apply_uibit_theme()
```

- **Primary blue** — main series and accents  
- **Green / red** — legitimate vs fraudulent classes  
- **Light grid background** — readable notebook output

## Keywords

Credit card fraud detection, imbalanced classification, KNN, SVM, logistic regression, decision tree, scikit-learn.
