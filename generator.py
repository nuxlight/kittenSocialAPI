import requests
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    url = "http://127.0.0.1:5000/cat"
    resutl = ""
    payload = "{\n\t\"cat_name\": \""+faker.first_name()+"\",\n\t\"cat_description\": \""+faker.text()+"\",\n\t\"cat_age\": "+str(faker.random.randrange(1,10))+"\n}"
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", url, data=payload, headers=headers)
    resutl += payload
    if response:
        print("Generating cats profile ok - "+resutl)
    else:
        print("Fail in generating profile - error : "+response.text+" - Query :"+resutl)