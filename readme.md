# Surge Pricing Prediction

This project aims to predict surge pricing multipliers for cab rides using historical ride and weather data. It includes data preprocessing, merging, model training, and evaluation — all organized in a modular Python project.

---

## Project Structure

```plaintext
Surge-Pricing/
│
├── app/
│   └── api.py              
│
├── data/
│   ├── cab_rides.csv
│   └── weather.csv
│
├── model/
│   ├── random_forest_model.pkl
│   └── label_encoder.pkl
│
├── src/
│   ├── merge.py  
│   ├── preprocess.py  
│   ├── training.py  
│   └── testing.py  
│
├── .gitignore
├── main.py
├── requirements.txt
├── test_model.py
├── Dockerfile
└── readme.md
```
Note: The 'cab_rides.csv' and 'label_encoder.pkl' file is excluded from this repository due to its large size.
You can download it separately from this https://drive.google.com/drive/folders/1ci9ndrPcPioSb4NHnaI3Ey7FSz_oq2Yf Drive link.

---

##  How to Run the Project Locally

### 1.  Install dependencies

Make sure you're using Python 3.8+ and install dependencies with:

```bash
pip install -r requirements.txt
```

### 2.  Prepare the data
Place your CSV files in the data/ directory:

    • data/rides.csv

    • data/weather.csv


### 3. Train the Model

```bash
python main.py data/rides.csv data/weather.csv
```

This script will:

    • Merge ride and weather data.

    • Clean and preprocess the dataset.

    • Encode surge multipliers.

    • Train a Random Forest classifier.

    • Evaluate the model.

---

### Run the FastAPI server locally
After training the model, run the API:

```bash
uvicorn app.api:app --reload
```

## Test the API
• Open in browser: http://127.0.0.1:8000/docs

• Use Swagger UI to test the '/predict' endpoint

Sample Input (JSON)
```bash
{
    "distance": 3.5,
    "day": 5,
    "hour": 18,
    "temp": 22.5,
    "clouds": 20,
    "pressure": 1012,
    "humidity": 60,
    "wind": 3.5,
    "rain": 0.0
}
```

##  How to Run the Project using Docker Container

Prerequisites

    • Docker Desktop or Rancher Desktop installed and running
    • Basic command-line knowledge

Build the Docker Image

Run this in your project root directory:
```bash
docker build -t surge-pricing .
```
Run the Dokcer Container
```bash
docker run -p 8000:8000 surge-pricing
```

---

## Testing the Model Locally
You can test the model locally without Docker by running:

```bash
python test_model.py
```
Make sure model files (random_forest_model.pkl and label_encoder.pkl) are present in the model/ folder.

---


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

---


# Model Details
 • Model: Random Forest Classifier

 • Balancing: SMOTE used for class imbalance

 • Evaluation Metrics:

    • Accuracy

    • Precision

    • Recall

    • F1 Score

    • Confusion Matrix

---


# Dependencies

```bash
pandas
scikit-learn
imblearn
numpy
fastapi
uvicorn
joblib
```

Install with:

```bash
pip install -r requirements.txt
```

# Notes
    • Surge multipliers ≥ 3.0 are ignored due to insufficient samples.

    • Missing rows are dropped during cleaning.

    • Timestamps are converted and merged based on location and hour.
