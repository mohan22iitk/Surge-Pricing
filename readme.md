# Uber Surge Pricing Prediction

This project aims to predict surge pricing multipliers for Uber rides using historical ride and weather data. It includes data preprocessing, merging, model training, and evaluation — all organized in a modular Python project.

---

## 📁 Project Structure
Uber-Surge-Pricing/
│
├── data/
│ ├── rides.csv
│ └── weather.csv
│
├── src/
│ ├── merge.py # Functions to merge ride and weather data
│ ├── preprocess.py # Data cleaning, feature extraction, label encoding, train-test split, SMOTE
│ ├── training.py # Random Forest training
│ └── testing.py # Evaluation (accuracy, precision, recall, f1-score)
│
├── main.py 
├── requirements.txt 
└── README.md 


---

##  How to Run the Project

### 1.  Install dependencies

Make sure you're using Python 3.8+ and install dependencies with:

```bash
pip install -r requirements.txt

2. 📂 Prepare the data
Place your CSV files in the data/ directory:

data/rides.csv

data/weather.csv

3. Run the project

```bash
python main.py data/rides.csv data/weather.csv
```

This script will:

    • Merge ride and weather data.

    • Clean and preprocess the dataset.

    • Encode surge multipliers.

    • Train a Random Forest classifier.

    • Evaluate the model.

# Features Used
    • distance

    • day

    • hour

    • temp

    • clouds

    • pressure

    • humidity

    • wind

    • rain

# Model Details
 • Model: Random Forest Classifier

 • Balancing: SMOTE used for class imbalance

 • Evaluation Metrics:

    • Accuracy

    • Precision

    • Recall

    • F1 Score

    • Confusion Matrix

# Dependencies

```bash
pandas
scikit-learn
imblearn
numpy
```

Install with:

```bash
pip install -r requirements.txtnumpy
```

# Notes
    • Surge multipliers ≥ 3.0 are ignored due to insufficient samples.

    • Missing rows are dropped during cleaning.

    • Timestamps are converted and merged based on location and hour.
