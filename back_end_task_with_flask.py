from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset (Replace 'dataset.csv' with your file)
df = pd.read_csv("C:\\Users\\vikas\\Downloads\\superstore_data.csv",encoding="latin1")

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

# Endpoint to return all data
@app.route('/data', methods=['GET'])
def get_data():
    return df.to_json(orient="records")

# Endpoint to get data by row index
@app.route('/data/<int:row_id>', methods=['GET'])
def get_data_by_id(row_id):
    if row_id < 0 or row_id >= len(df):
        return jsonify({"error": "Row ID out of range"}), 404
    return jsonify(df.iloc[row_id].to_dict())

if __name__ == '__main__':
    app.run(debug=True)