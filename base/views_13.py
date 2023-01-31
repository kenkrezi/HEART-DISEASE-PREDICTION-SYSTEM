from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import random
from .prediction import predict
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
    '0.1':'MALE',
    '0.2':'FEMALE',
    '1.1': 'High Cholesterol',
    '1.2': 'High Blood Pressure',
    '1.3': 'BOTH',
    '1.4': 'No',
    '2.1': 'LESS THAN 18.5 (Underweight)',
    '2.2': '18.5 - 24.9 (Normal)',
    '2.3': '25.0 - 29.9 (Overweight)',
    '2.4': '30.0 OR HIGHER (Obese)',
    '3.1': 'Smoke',
    '3.2': 'Drink',
    '3.3': 'Both',
    '3.4': 'No',
    '4.1': 'Type-A',
    '4.2': 'Type-B',
    '4.3': 'No',
    '5.1': 'Yes',
    '5.2': 'No',
    '6.1': 'Yes',
    '6.2': 'No',
    '7.1': 'Yes',
    '7.2': 'No',
    '8.5': 'GREAT (all)',
    '8.4': 'GOOD (majority)',
    '8.3': 'NORMAL (half)',
    '8.2': 'NOT SURE',
    '8.1': 'BAD (none)'

}
def get_pred_values(response):
    myData = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    response_data = response.split('*')
    print("This response data", response_data)
    for n in response_data:
        print("this value of n", n)
        if (n=='1'):
            value = 1.0
            myData[12] = value
        elif (n=='2'):
            value = 0.0
            myData[12] = value
        elif (n=='3'):
            hbp = 0.0
            hch = 1.0
            myData[0] = hbp
            myData[1] = hch
        elif (n=='4'):
            hbp = 1.0
            hch = 0.0
            myData[0] = hbp
            myData[1] = hch
        elif (n=='5'):
            hbp = 1.0
            hch = 1.0
            myData[0] = hbp
            myData[1] = hch
        elif (n=='6'):
            hbp = 0.0
            hch = 0.0
            myData[0] = hbp
            myData[1] = hch
        elif (n=='7'):
        
            num1 = random.randint(14, 18)
            bmi = num1
            myData[3] = bmi
            print(num1)
        elif (n=='8'):
            
            num1 = random.randint(19, 24)
            bmi = num1
            myData[3] = bmi
            print(num1)
        elif (n=='9'):
            
            num1 = random.randint(25, 29)
            bmi = num1
            myData[3] = bmi
            print(num1)
        elif (n=='10'):
            
            num1 = random.randint(30, 58)
            bmi = num1
            myData[3] = bmi
            print(num1)
        elif (n=='11'):
            drink = 0.0
            smoke = 1.0
            myData[8] = drink
            myData[4] = smoke
        elif (n=='12'):
            drink = 1.0
            smoke = 0.0
            myData[8] = drink
            myData[4] = smoke
        elif (n=='13'):
            drink = 1.0
            smoke = 1.0
            myData[8] = drink
            myData[4] = smoke
        elif (n=='14'):
            drink = 0.0
            smoke = 0.0
            myData[8] = drink
            myData[4] = smoke
        elif (n=='15'):
            Diabetes = 1.0
            myData[6] = Diabetes
        elif (n=='16'):
            Diabetes = 2.0
            myData[6] = Diabetes
        elif (n=='17'):
            Diabetes = 0.0
            myData[6] = Diabetes
        elif (n=='18'):
            Stroke = 1.0
            myData[5] = Stroke
        elif (n=='19'):
            Stroke = 0.0
            myData[5] = Stroke
        elif (n=='20'):
            Physically_active = 1.0
            myData[7] = Physically_active
        elif (n=='21'):
            Physically_active = 0.0
            myData[7] = Physically_active
        elif (n=='22'):
            Healthcare = 1.0
            myData[9] = Healthcare
        elif (n=='23'):
            Healthcare = 0.0
            myData[9] = Healthcare
        elif (n=='24'):
            Gen_Health = 5.0
            myData[10] = Gen_Health
        elif (n=='25'):
            Gen_Health = 4.0
            myData[10] = Gen_Health
        elif (n=='26'):
            Gen_Health = 3.0
            myData[10] = Gen_Health
        elif (n=='27'):
            Gen_Health = 2.0
            myData[10] = Gen_Health
        elif (n=='28'):
            Gen_Health = 1.0
            myData[10] = Gen_Health
        elif (n=='29'):
            Difficulty_walking = 1.0
            myData[11] = Difficulty_walking
        elif (n=='30'):
            Difficulty_walking = 0.0
            myData[11] = Difficulty_walking
        elif (n=='31'):
            chol_check = 1.0
            myData[2] = chol_check
        elif (n=='32'):
            chol_check = 0.0
            myData[2] = chol_check
    print(myData)
    return myData


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
        response = "CON Welcome to the Heart Disease Prediction service! \n Choose Gender: \n"
        response += "1 Male \n"
        response += "2 Female \n"

    elif len(steps) == 1 and text != "":
        response = "CON Do you have high blood pressure and/or high cholesterol? \n"
        response += "3 High Cholesterol \n"
        response += "4 High Blood Pressure \n"
        response += "5 BOTH \n"
        response += "6 NO\n"

    elif len(steps) == 2 :
        response = "CON What is your BMI range? \n"
        response += "7 LESS THAN 18.5 (Underweight) \n"
        response += "8 18.5 - 24.9 (Normal) \n"
        response += "9 25.0 - 29.9 (Overweight) \n"
        response += "10 30.0 OR HIGHER (Obese) \n"

    elif len(steps) == 3:
        response = "CON Do you smoke tobacco or use other tobacco products or consume excessive amounts of alcohol?\n"
        response += "11 Smoke \n"
        response += "12 Drink  \n"
        response += "13 Both \n"
        response += "14 No \n"

    elif len(steps) == 4:
        response = "CON Do you have Diabetes?\n"
        response += "15 Type-1 \n"
        response += "16 Type-2 \n"
        response += "17 No \n"

    elif len(steps) == 5:
        response = "CON Do you have a personal or family history of stroke? \n"
        response += "18 Yes \n"
        response += "19 No \n"

    elif len(steps) == 6:
        response = "CON Are you physically active (running,jogging,hiking,walks)? \n"
        response += "20 Yes \n"
        response += "21 No \n"

    elif len(steps) == 7 :
        response = "CON Doyou have Healthcare? \n"
        response += "22 Yes \n"
        response += "23 No \n"

    elif len(steps) == 8 :
        response = "CON how is your health generally? (enough sleep,hydrated,healthy diet,exercising)? \n"
        response += "24 GREAT (all) \n"
        response += "25 GOOD (majority) \n"
        response += "26 NORMAL (half)\n"
        response += "27 NOT SURE \n"
        response += "28 BAD (none)\n"

    elif len(steps) == 9 :
        response = "CON Do you have Difficulty in walking? \n"
        response += "29 Yes \n"
        response += "30 No \n"

    elif len(steps) == 10 :
        response = "CON Do you have cholesterol check ups? \n"
        response += "31 Yes \n"
        response += "32 No \n"

    elif len(steps) == 11 :
        response = "CON RESULTS WILL BE SENT SHORTLY. THANK YOU. \n A HEALTHY HEART IS A HEALTHY LIFE. \n"
        data_array = get_pred_values(text)
        result = predict(data_array)
        print(result)
        response += " RESULTS: {} \n".format(result)
        response += "11 Done \n"
        print (text)
        

    elif len(steps) ==  12:
        response = "END Best cardiovascular hospital in kenya:\n"
        response += "- Heart Clinic - Aga Khan University Hospital Nairobi | 0111 011888.\n"
        response += "- Kenya Cardiovascular Centre | Kiambu road | 0726 245140.\n"
        response += "- Nairobi Heart Clinic | 020 2715807. \n"
        response += "- Aga Khan University Hospital Nairobi | 0111 011888. \n"
        response += "- UpperHill Cardiovascular Centre | 0736 362282 \n"
        response += "- Nakuru Heart Centre | 0716 862144\n"

    return HttpResponse(response)

