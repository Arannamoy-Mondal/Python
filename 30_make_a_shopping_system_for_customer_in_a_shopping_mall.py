class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'Sending SMS to: {phone+5}'
        return text


my_phone = Phone()
result = my_phone.send_sms(41524, 'Missy, I missed to miss you')
print(result)


# 448f6c48a51bb419c68c763b0e4eefc0449ad7bbad534de3f93b2f1a40308833 *pycharm-community-2024.2.3.tar.gz