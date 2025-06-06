# -*- coding: utf-8 -*-
"""main

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w8suPOVd_dJVtBLJL4ZXN6SSUQuzXTBl
"""

import sys
from src.merge import load_and_prepare_data, merge_rides_with_weather
from src.preprocess import clean_and_extract_features, encode_labels, split_and_balance_data
from src.training import train_random_forest, save_model
from src.testing import evaluate_model

def main(rides_csv, weather_csv):
    # Load and merge data
    rides, weather = load_and_prepare_data(rides_csv, weather_csv)
    merged_df = merge_rides_with_weather(rides, weather)

    #############delete it later
    #  TEMP: Add day and hour columns so we can filter
    merged_df['day'] = merged_df['date_time'].dt.dayofweek
    merged_df['hour'] = merged_df['date_time'].dt.hour

    #  TEMP: Extract real surge > 1 examples for test input
    feature_cols = ['distance', 'day', 'hour', 'temp', 'clouds', 'pressure', 'humidity', 'wind', 'rain']
    surge_examples = merged_df[merged_df['surge_multiplier'] > 1]
    surge_examples = surge_examples[feature_cols].dropna().head(5)

    print("📈 High surge examples from training data:")
    print(surge_examples.to_dict(orient='records'))


    # Preprocess data
    X, y_raw, features = clean_and_extract_features(merged_df)
    y, le = encode_labels(y_raw)
    x_train, x_test, y_train, y_test = split_and_balance_data(X, y)

    # Train model
    model = train_random_forest(x_train, y_train)

    # Save model and label encoder
    save_model(model, le)

    # Evaluate model
    evaluate_model(model, x_test, y_test, le)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <rides_csv_path> <weather_csv_path>")
        sys.exit(1)
    rides_csv_path = sys.argv[1]
    weather_csv_path = sys.argv[2]
    main(rides_csv_path, weather_csv_path)

