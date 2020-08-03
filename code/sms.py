import requests

def send_sms(data):
    url = "https://www.fast2sms.com/dev/bulk"
    

    for student_data in data:
        correct=0

        for i in student_data[4]:

            if(i==True):
                correct=correct+1
            
        message="Dear {}, you have done {} questions correctly".format(student_data[0],correct)


        querystring = {"authorization":"gKyw815ARYiTZDqWkEJb4P0mza6XBle2CNd3fxHGLu7voItQOnOLhmwrUXK1AsbSv3af4Iq5tC0R9gDo","sender_id":"FSTSMS","message":smsmessage,"language":"english","route":"p","numbers":student_data[3]}
        
        headers = {
            'cache-control': "no-cache"
        }
        try:

            response = requests.request("GET", url, headers=headers, params=querystring)

        except:
            print("Internet not working most probably")

# must also check errors from fast2sms server
