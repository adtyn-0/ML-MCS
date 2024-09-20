# ML-MCS
Machine Learning Driven Malware Classification System for Malware Analysis Hackathon (IIT-M) 2024

## Overview
A machine learning-based tool that classifies software as benign or malicious based on system usage metrics such as CPU usage, memory usage, and network activity.

## Features
- Classifies files using RandomForest, Gradient Boosting, and XGBoost models.
- Provides a simple web interface for real-time malware classification.
- Uses majority voting from multiple models to determine the final prediction.

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Models**: RandomForest, Gradient Boosting, XGBoost
- **Libraries**: scikit-learn, pandas, XGBoost, Flask

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/adtyn-0/ML-MCS.git
    cd ML-MCS
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Flask app:
    ```bash
    python app.py
    ```
4. Access the app at `http://127.0.0.1:5000`.

## How to Use
- Enter system metrics (CPU usage, memory, network activity) in the web form.
- Click "Classify" to get predictions from the trained models.

## License
This project is licensed under the MIT License.

