import requests
import json

def get_information():
    #Getting user input
    person = input("Enter the first name of the record you'd like to search for: ")
    
    #Performing get request 
    response = requests.get(f"http://127.0.0.1:5000/people/{person}")
    
    #Printing 
    print(response.text)

def post_information(): 
    #Getting user input
    firstname = input("Enter the first name of the record you'd like to post: ")
    lastname = input("Enter the last name of the record you'd like to post: ")
    country = input("Enter the country of the record you'd like to post: ")
    email = input("Enter the email of the record you'd like to post: ")
    
    #Send post request and serialize data in to json format
    response = requests.post("http://127.0.0.1:5000/people", json={"firstname" : firstname, "lastname" : lastname, "country" : country, "email" : email})
    print(response.status_code)
    print(response.json())

def main():
    get_information()
    post_information()

if __name__ == "__main__":
    main()