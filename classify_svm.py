import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

def svm_disease_classifier(train_data, test_data, label_column, dataset_name="Dataset"):
    print(f"\nRunning SVM classifier for {dataset_name}...")

    try:
        # Drop missing values
        train_data = train_data.dropna()
        test_data = test_data.dropna()

        # Separate features and labels
        X_train = train_data.drop(columns=[label_column])
        y_train = train_data[label_column]
        X_test = test_data.drop(columns=[label_column])
        y_test = test_data[label_column]

        # Use only numeric columns
        X_train = X_train.select_dtypes(include=["number"])
        X_test = X_test[X_train.columns]

        # Feature scaling
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # SVM model
        clf = SVC(kernel='rbf', C=1.0, gamma='scale')
        clf.fit(X_train_scaled, y_train)

        # Evaluation
        y_pred = clf.predict(X_test_scaled)
        print(f"\n--- SVM Classification Report for {dataset_name} ---")
        print(classification_report(y_test, y_pred))
        print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(f"{dataset_name} - Confusion Matrix")
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.show()


    except Exception as e:
        print(f"Error during SVM classification for {dataset_name}: {e}")
svm_disease_classifier(heart_train, heart_test, "target", "Heart Disease")
svm_disease_classifier(diabetes_train, diabetes_test, "Outcome", "Diabetes")
