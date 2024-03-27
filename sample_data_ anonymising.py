users = [{'Name':'Tony', 'Country': 'France', 'Card Number':'3542-7583-7228-3788'},
{'Name':'Steve','Country':'Austria', 'Card Number':'3881-8829-5554-4875'},
{'Name':'Peter', 'Country':'Spain', 'Card Number':'8445-5556-9621-9962'}]


print("Name\t\tCountry\t\tCard Number")
for user in users:
    card_number = 'XXXXXXXXXXXX'+ user ['Card Number'][ -4:]
    print (user['Name']+"\t\t"+user['Country']+"\t\t"+user['Card Number'])