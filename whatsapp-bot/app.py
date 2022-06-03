from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gsheet_func import *

from dateutil.parser import parse

app = Flask(__name__)
count=0

@app.route("/sms", methods=['POST'])

def reply():

    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    message = response.message()
    responded = False
    words = incoming_msg.split('@')

    if "Hello" in incoming_msg:
        reply = "Helooooo! \nHatırlatıcı ayarlamak ister misin?"
        message.body(reply)
        responded = True
    
    if len(words) == 1 and "evet" in incoming_msg:
        reminder_string = "Lütfen hatırlatıcı için tarihi aşağıdaki formatta giriniz.\n\n"\
            "*Tarih @* _tarih tipi_ "
        message.body(reminder_string)
        responded = True

    if len(words) == 1 and "hayır" in incoming_msg:
        reply="Tamam. İyi günler :)"
        message.body(reply)
        responded = True

    elif len(words) != 1:
        input_type = words[0].strip().lower()
        input_string= words[1].strip()

        if input_type == "tarih":
            reply="Lütfen hatırlatıcı için mesajı aşağıdaki formatta giriniz.\n\n"\
                "*Hatırlatıcı @* _mesaj tipi_"
            set_reminder_date(input_string)
            message.body(reply)
            responded = True

        if input_type == "hatırlatıcı":
            reply="Hatırlatıcı ayarlandı!"
            set_reminder_body(input_string)
            message.body(reply)
            responded = True
        
    if not responded:
        message.body('Yanıt formatınız yanlış. Lütfen doğru yanıt formatı giriniz.')

    return str(response)


def set_reminder_date(msg):
    p=parse(msg)
    date=p.strftime('%d/%m/%Y')
    save_reminder_date(date)
    return 0

def set_reminder_body(msg):
    save_reminder_body(msg)
    return 0


if __name__ == "__main__":
    app.run(debug=True)