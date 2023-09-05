import sms  

def main():
    print("Welcome to the SMS Automation System")
    phone_number = input("Enter the phone number here: ")
    message = input("Enter the message: ")

    if sms.validate_phone_number(phone_number) and sms.validate_message_length(message):
        sms.send_sms(phone_number, message)
        print("SMS sent successfully!")
    else:
        print("Invalid phone number or message length.")

if _name_ == "_main_":
    main()
