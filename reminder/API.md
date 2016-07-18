System Requirements
1. Python
2. Rabbitmq
3. pip

Installation Steps
1. Clone this project
2. Go to reminder directory
3. pip install -r requirements.txt

Accepted JSON Format

{
    "date":"mm/dd/yyyy",
    "time": "hh:mm pm",        # date time would be considered of UTC timezone
    "message": "MESSAGE-BODY",
    "channel": ["email", "sms"],
    "email": "EMAILID"
    "mobile_phone": "MOBILEPHONE"
}