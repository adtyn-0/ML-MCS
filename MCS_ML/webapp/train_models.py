import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle

data = pd.read_csv('../data/simulated_malware_dataset.csv')

data = data.drop('Timestamp', axis=1)  # Can't use it so dropped

if 'Class_Label' in data.columns:
    X = data.drop('Class_Label', axis=1)
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(data['Class_Label'])
else:
    print(f"'Class_Label' column not found.")
    raise KeyError("'Class_Label' column not found in dataset.")

features = list(X.columns)
print("Feature names during training:", features)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

'''This is for RandomForest'''
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
pickle.dump(rf_model, open('../models/rf_model.pkl', 'wb'))

'''This is for gradient'''
gb_model = GradientBoostingClassifier()
gb_model.fit(X_train, y_train)
pickle.dump(gb_model, open('../models/gb_model.pkl', 'wb'))

'''and this for XGB.Don't get confused'''
xgb_model = XGBClassifier()
xgb_model.fit(X_train, y_train)
pickle.dump(xgb_model, open('../models/xgb_model.pkl', 'wb'))

pickle.dump(scaler, open('../models/scaler.pkl', 'wb'))

pickle.dump(label_encoder, open('../models/label_encoder.pkl', 'wb'))

with open('../models/feature_names.pkl', 'wb') as f:
    pickle.dump(features, f)

print("All models, scaler, encoder, and feature names saved successfully.")
