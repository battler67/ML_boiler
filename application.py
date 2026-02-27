# from src.components.data_ingestion import DataIngestion

# if __name__ == "__main__":
#     obj = DataIngestion()
#     obj.initiate_data_ingestion()


from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
from flask import jsonify

application  = Flask(__name__)
app = application
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict",methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template("home.html",results=None)
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        pred_df = data.get_data_as_data_frame()
        pred_df.rename(
            columns={"race_ethnicity":"race/ethnicity",
                    "parental_level_of_education":"parental level of education",
                    "test_preparation_course":"test preparation course",
                    "reading_score":"reading score",
                    "writing_score":"writing score"
                    },inplace=True)
        print(pred_df)
        print("Before Prediction")
        Predict_Pipeline = PredictPipeline()
        print("Mid prediction")
        results = Predict_Pipeline.predict(pred_df)
        print("After prediction")
        return render_template('home.html',results = results[0])
        # return jsonify({"prediction": results[0]})
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0")#removed debug =True