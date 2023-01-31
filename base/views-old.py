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
        
        if text == "":
            response = "CON HELLO, WELCOME TO HEARTGUARD. \n CHOOSE GENDER. \n"
            response += "1.1 MALE \n"
            response += "1.2 FEMALE \n"
        elif len(steps) == 1 and text != "":
            response = "CON DO YOU HAVE HIGH BLOOD PRESSURE? \n"
            response += "2.1 YES \n"
            response += "2.2 NO \n"
        elif len(steps) == 2 :
            response = "CON DO YOU HAVE HIGH CHOLESTEROL? \n"
            response += "3.1 YES \n"
            response += "3.2 NO \n"
        elif len(steps) == 3 :
            response = "CON HAVE YOU HAD A CHOLESTEROL CHECK? \n"
            response += "4.1 YES \n"
            response += "4.2 NO \n"
        elif len(steps) == 4:
            response = "CON WHAT IS YOUR BMI RANGE? \n"
            response += "5.1 LESS THAN 18.5 (UNDERWEIGHT) \n"
            response += "5.2 18.5 - 24.9 (NORMAL) \n"
            response += "5.3 25.0 - 29.9 (OVERWEIGHT) \n"
            response += "5.4 30.0 OR HIGHER (OBESE) \n"
        elif len(steps) == 5 :
            response = "CON DO YOU SMOKE? \n"
            response += "6.1 YES \n"
            response += "6.2 NO \n"
        elif len(steps) == 6 :
            response = "CON HAVE YOU HAD A STROKE RECENTLY? \n"
            response += "7.1 YES \n"
            response += "7.2 NO \n"
        elif len(steps) == 7 :
            response = "CON DO YOU HAVE DIABETES? \n"
            response += "8.1 TYPE-1 \n"
            response += "8.2 TYPE-2 \n"
            response += "8.3 NO \n"
        elif len(steps) == 8 :
            response = "CON DO YOU DO PHYSICAL ACTIVITIES \n (running,jogging,hiking...etc)? \n"
            response += "9.1 YES \n"
            response += "9.2 NO \n"
        elif len(steps) == 9 :
            response = "CON WHAT IS YOUR ALCOHOL CONSUMPTION RATE? \n"
            response += "10.1 HIGH \n"
            response += "10.2 LOW-NONE \n"
        elif len(steps) == 10 :
            response = "CON DO YOU HAVE HEALTHCARE? \n"
            response += "11.1 YES \n"
            response += "11.2 NO \n"
        elif len(steps) == 11 :
            response = "CON HOW IS YOUR HEALTH GENERALLY \n(sleeping well, exercising, healthy diet, hydrating)? \n"
            response += "12.5 GREAT (all) \n"
            response += "12.4 GOOD (majority) \n"
            response += "12.3 NORMAL (half)\n"
            response += "12.2 NOT SURE \n"
            response += "12.1 BAD (none)\n"
        elif len(steps) == 12 :
            response = "CON DO YOU HAVE DIFFICULTY IN WALKING? \n"
            response += "13.1 YES \n"
            response += "13.2 NO \n"
        elif len(steps) == 13 :
            response = "CON HOW IS YOUR MENTAL HEALTH? \n"
            response += "14.1 1-10 (depression, PTSD) \n"
            response += "14.2 11-20 (stress, anxiety) \n"
            response += "14.3 21-30 (calm,high self-esteem,manage emotions) \n"
        elif len(steps) == 14 :
            response = "END RESULTS WILL BE SENT SHORTLY. THANK YOU. \n A HEALTHY HEART IS A HEALTHY LIFE. \n"
    return HttpResponse(response)

