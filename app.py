import os
import sys
from flask import Flask, request, render_template, jsonify

# # Add the path to the parent directory of the pipelines package folder
# module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(module_path)

from source.pipelines.prediction_pipeline import CustomData, PredictPipeline
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

@app.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    if request.method == "GET":
        return render_template('form.html')
    else: 
        pass
