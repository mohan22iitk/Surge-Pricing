# -*- coding: utf-8 -*-
"""testing

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DTlbTTGgNrYSLMOsWGvh91sK0TcrAU7c
"""

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(model, x_test, y_test, label_encoder):
    """
    Predicts on test data, prints confusion matrix and classification metrics.
    """
    y_pred = model.predict(x_test)

    # Inverse transform to original labels for confusion matrix display
    y_test_labels = label_encoder.inverse_transform(y_test)
    y_pred_labels = label_encoder.inverse_transform(y_pred)

    # Confusion matrix as DataFrame for pretty print
    cm = pd.crosstab(y_test_labels, y_pred_labels, rownames=['Actual'], colnames=['Predicted'])
    print("Confusion Matrix:\n", cm)

    # Calculate and print metrics
    print("Accuracy Score =", accuracy_score(y_test, y_pred))
    print("Precision Score =", precision_score(y_test, y_pred, average='weighted'))
    print("Recall Score =", recall_score(y_test, y_pred, average='micro'))
    print("F1 Score =", f1_score(y_test, y_pred, average='weighted'))

    # Mean Absolute Error (note: classes are integers here)
    errors = abs(y_pred - y_test)
    print('Mean Absolute Error:', round(np.mean(errors), 2))


##########################################



    # --- To extract feature rows where actual=2.0 and predicted=2.0 ---
    actual_val = 2.0
    pred_val = 2.0


    matching_indices = np.where((y_test_labels == actual_val) & (y_pred_labels == pred_val))[0]

    matching_features = x_test.iloc[matching_indices]

    print(f"\nNumber of test samples where actual={actual_val} and predicted={pred_val}: {len(matching_features)}")
    print("Sample feature rows for these cases:")
    print(matching_features.head(5))

    # Save to CSV for further testing
    matching_features.to_csv("actual2_pred2_features.csv", index=False)