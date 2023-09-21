import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier



def train_evaluate_classifier(model, X, y):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Train the model
    model.fit(X_train, y_train)

    # Convert X_test to a NumPy array
    X_test_np = X_test.to_numpy()

    # Make predictions
    y_pred = model.predict(X_test_np)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return accuracy, confusion, report






df = pd.read_csv("./Data/BankChurners.csv")

# Define the features (X) and the target (y)
X = df[['Customer_Age', 'Gender', 'Dependent_count', 'Education_Level',
        'Marital_Status_Unknown',"Marital_Status_Single","Marital_Status_Married", 'Income_Category', 'Card_Category', 'Months_on_book',
        'Total_Relationship_Count', 'Months_Inactive_12_mon', 'Contacts_Count_12_mon',
        'Credit_Limit', 'Total_Revolving_Bal', 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1',
        'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio']]
y = df['Attrition_Flag']

# Create instances of different classifiers
logistic_regression = LogisticRegression()
knn_classifier = KNeighborsClassifier()
decision_tree = DecisionTreeClassifier()
random_forest = RandomForestClassifier()

# Train and evaluate each classifier using the function
models = [logistic_regression, knn_classifier, decision_tree, random_forest]
for model in models:
    accuracy, confusion, report = train_evaluate_classifier(model, X, y)
    print(f"Model: {model.__class__.__name__}")
    print("Accuracy:", accuracy)
    print("Confusion Matrix:\n", confusion)
    print("Classification Report:\n", report)
    print("\n")

