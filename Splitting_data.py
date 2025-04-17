import pandas as pd
from sklearn.model_selection import train_test_split

def analyze_and_split_dataset(filepath, dataset_name, label_column, test_size=0.2, validation_size=0.2):
    """Analyzes a single CSV dataset, splits it, and prints relevant information."""
    try:
        data = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return

    classes = data[label_column].unique()
    num_classes = len(classes)

    print(f"\nAnalysis of {dataset_name} dataset:")
    print(f"Number of classes: {num_classes}")
    print(f"Total dataset size: {len(data)}")

    train_data, temp_data = train_test_split(
        data, test_size=(test_size + validation_size), stratify=data[label_column]
    )
    val_data, test_data = train_test_split(
        temp_data, test_size=test_size / (test_size + validation_size), stratify=temp_data[label_column]
    )

    print(f"Train set size: {len(train_data)}")
    print(f"Validation set size: {len(val_data)}")
    print(f"Test set size: {len(test_data)}")
    return train_data, val_data, test_data

#giving file path
heart_filepath = "dataset/heart.csv"
diabetes_filepath = "dataset/diabetes.csv"

heart_label_column = "target"  
diabetes_label_column = "Outcome"  

# Calling the dataset split function and store results
heart_train, heart_val, heart_test = analyze_and_split_dataset(heart_filepath, "Heart", heart_label_column)
diabetes_train, diabetes_val, diabetes_test = analyze_and_split_dataset(diabetes_filepath, "Diabetes", diabetes_label_column)
