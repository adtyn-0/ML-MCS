import logging
from flask import Flask, request, render_template
import pickle
import pandas as pd
from collections import Counter

app = Flask(__name__)

rf_model = pickle.load(open('../models/rf_model.pkl', 'rb'))
gb_model = pickle.load(open('../models/gb_model.pkl', 'rb'))
xgb_model = pickle.load(open('../models/xgb_model.pkl', 'rb'))
scaler = pickle.load(open('../models/scaler.pkl', 'rb'))
label_encoder = pickle.load(open('../models/label_encoder.pkl', 'rb'))

with open('../models/feature_names.pkl', 'rb') as f:
    feature_names = pickle.load(f)
print("Feature names used during prediction:", feature_names)

'''Correct location of the models are given.This solves the File not found error'''


@app.route('/')
def home():
    return render_template('index.html')


logging.basicConfig(level=logging.DEBUG)


@app.route('/classify', methods=['POST'])
def classify():
    input_data = request.get_json(force=True)
    result = {}

    try:
        # Ultimately not needed. Caused too many issues.
        log_id = input_data.get('log_id')

        features = [
            float(input_data['cpu_usage']),
            float(input_data['memory_usage']),
            float(input_data['network_activity']),
            float(input_data['disk_io']),
            float(input_data['process_count']),
        ]

        expected_features_count = len(feature_names)
        if len(features) + 1 != expected_features_count:
            raise ValueError(
                f"Expected {expected_features_count} features, but got {len(features) + 1} (including log_id).")

        features_df = pd.DataFrame(
            [features + [log_id]], columns=feature_names)  # FINALLY SOLVED THE DATAFRAME ERROR...W

        scaled_features = scaler.transform(features_df)

        rf_prediction = rf_model.predict(scaled_features)[0]
        gb_prediction = gb_model.predict(scaled_features)[0]
        xgb_prediction = xgb_model.predict(scaled_features)[0]

        predictions = [rf_prediction, gb_prediction, xgb_prediction]
        prediction_counts = Counter(predictions)
        most_common = prediction_counts.most_common()

        if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
            final_class = "Tie between: " + ", ".join(
                [label_encoder.inverse_transform(
                    [item[0]])[0] for item in most_common if item[1] == most_common[0][1]]
            )
        else:
            final_class = label_encoder.inverse_transform(
                [most_common[0][0]])[0]

        result = {
            "rf_prediction": label_encoder.inverse_transform([rf_prediction])[0],
            "gb_prediction": label_encoder.inverse_transform([gb_prediction])[0],
            "xgb_prediction": label_encoder.inverse_transform([xgb_prediction])[0],
            "final_prediction": final_class
        }

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return {"error": f"Error: {str(e)}"}, 500

    return result


if __name__ == "__main__":
    app.run(debug=True)
