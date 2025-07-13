from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pickle
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = pickle.load(open(os.path.join(BASE_DIR, 'margapp/ml_model/model.pkl'), 'rb'))
scaler = pickle.load(open(os.path.join(BASE_DIR, 'margapp/ml_model/scaler.pkl'), 'rb'))

class_names = [
    'Lawyer', 'Doctor', 'Government Officer', 'Artist', 'Unknown',
    'Software Engineer', 'Teacher', 'Business Owner', 'Scientist',
    'Banker', 'Writer', 'Accountant', 'Designer',
    'Construction Engineer', 'Game Developer', 'Stock Investor',
    'Real Estate Developer'
]

def Recommendations(
    gender, part_time_job, absence_days, extracurricular_activities,
    weekly_self_study_hours, math_score, science_score, social_score,
    nepali_score, account_score, english_score, EPH_score,
    total_score, average_score
):
    gender_encoded = 1 if gender.lower() == 'female' else 0
    part_time_job_encoded = 1 if part_time_job else 0
    extracurricular_activities_encoded = 1 if extracurricular_activities else 0

    feature_array = np.array([[ 
        gender_encoded, part_time_job_encoded, absence_days,
        extracurricular_activities_encoded, weekly_self_study_hours,
        math_score, science_score, social_score,
        nepali_score, account_score, english_score, EPH_score,
        total_score, average_score
    ]])

    scaled_features = scaler.transform(feature_array)
    probabilities = model.predict_proba(scaled_features)
    top_classes_idx = np.argsort(-probabilities[0])[:3]
    return [(class_names[idx], probabilities[0][idx]) for idx in top_classes_idx]

@login_required(login_url='/accounts/login/')
def recommend_view(request):
    return render(request, 'marg/MargAI/recommend.html')

@login_required(login_url='/accounts/login/')
def result_view(request):
    if request.method == 'POST':
        try:
            gender = request.POST.get('gender', 'male')
            part_time_job = request.POST.get('part_time_job', 'false') == 'true'
            absence_days = int(request.POST.get('absence_days', 0) or 0)
            extracurricular_activities = request.POST.get('extracurricular_activities', 'false') == 'true'
            weekly_self_study_hours = int(request.POST.get('weekly_self_study_hours', 0) or 0)
            math_score = int(request.POST.get('math_score', 0) or 0)
            science_score = int(request.POST.get('science_score', 0) or 0)
            social_score = int(request.POST.get('social_score', 0) or 0)
            nepali_score = int(request.POST.get('nepali_score', 0) or 0)
            account_score = int(request.POST.get('account_score', 0) or 0)
            english_score = int(request.POST.get('english_score', 0) or 0)
            EPH_score = int(request.POST.get('EPH_score', 0) or 0)
            total_score = float(request.POST.get('total_score', 0) or 0)
            average_score = float(request.POST.get('average_score', 0) or 0)

            recommendations = Recommendations(
                gender, part_time_job, absence_days, extracurricular_activities,
                weekly_self_study_hours, math_score, science_score, social_score,
                nepali_score, account_score, english_score, EPH_score,
                total_score, average_score
            )
            return render(request, 'marg/MargAI/results.html', {'recommendations': recommendations})

        except Exception as e:
            print("Error:", e)
            return render(request, 'marg/MargAI/results.html', {'recommendations': []})

    return render(request, 'marg/MargAI/recommend.html')
