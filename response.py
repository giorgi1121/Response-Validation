from validator_collection import validators

def main():
    email_address = input("What's your email address? ")
    print(validate(email_address))

def validate(email_address):
    try:
       if validators.email(email_address):
          return "Valid"
    
    except ValueError:
       return "Invalid"

if __name__ == "__main__":
  main()