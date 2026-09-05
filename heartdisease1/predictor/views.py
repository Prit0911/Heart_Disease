from django.shortcuts import render
import joblib
# Create your views here.

model = joblib.load("../heart_disease_model.pkl")
scaler = joblib.load("../scaler.pkl")
def base(req):
    return render(req,'base.html')

def index(req):
    result = None
    if req.method == "POST":
        try: 
            data = [
                float(req.POST['age']),
                float(req.POST['sex']),
                float(req.POST['cp']),
                float(req.POST['trestbps']),
                float(req.POST['chol']),
                float(req.POST['fbs']),
                float(req.POST['restecg']),
                float(req.POST['thalach']),
                float(req.POST['exang']),
                float(req.POST['oldpeak']),
                float(req.POST['slope']),
                float(req.POST['ca']),
                float(req.POST['thal']),
            ]
            scaled_data = scaler.transform([data])

            prediction = model.predict(scaled_data)[0]
            result = "Heart disease detected" if prediction == 1 else "No heart disease"
        except Exception as e:
            result = f'Error:{e}'

    return render(req,'index.html',{'result':result})

def result(req):
    return render(req,'result.html')