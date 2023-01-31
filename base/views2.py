from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
myData = {
    'HighBP':'',
    'HighChol': '',
    'CholCheck':'',
    'BMI':'',
    'Smoker':'',
    'Stroke':'',
    'Diabetes':'',
    'PhysActivity':'',
    'HvyAlcCons':'',
    'AnyHlthCare':'',
    'GenHlth':'',
    'MentHlth':'',
    'DiffWalk':'',
    'Sex':''
}
myChoice= {
    '1.1':'MALE',
    '1.2':'FEMALE',
    '2.1': 'YES',
    '2.2': 'NO'
}
@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        steps = text.split("*")
        response = ""
        print("THIS IS YOUR SEQUENCE", text)
        
        response = "Welcome to the Heart Disease Prediction service!\n"
            
            # Ask the user for their age
        response += "Please enter your age: "
        age = request.get("text").split("*")[-1]
            
            # Ask the user for their blood pressure
        response += "Please enter your blood pressure (systolic and diastolic, separated by a '/'): "
        blood_pressure = request.get("text").split("*")[-1]
            
            # Ask the user for their cholesterol levels
        response += "Please enter your cholesterol levels (HDL and LDL, separated by a '/'): "
        cholesterol = request.get("text").split("*")[-1]
            
            # Ask the user about their family history of heart disease
        response += "Do you have a family history of heart disease? (Yes or No): "
        family_history = request.get("text").split("*")[-1]
            
            # Calculate the user's risk of developing heart disease based on their answers
       # risk = calculate_risk(age, blood_pressure, cholesterol, family_history)
            
            # Provide recommendations for reducing the risk of heart disease
        response += "Based on your answers, your risk of developing heart disease is {}. Here are some recommendations to help reduce your risk:\n".format(risk)
        response += "- Eat a healthy diet low in saturated and trans fats, salt, and sugar\n"
        response += "- Exercise regularly\n"
        response += "- Don't smoke\n"
        response += "- Maintain a healthy weight\n"
        response += "- Control your blood pressure and cholesterol levels\n"
    return HttpResponse(response)

