import getpass

# Dictionary to store passwords
passwords = {}

def add_password(service, username, password):
  passwords[service] = (username, password)

def get_password(service):
  if service in passwords:
    return passwords[service]
  else:
    return None

def change_password(service, username, password):
  if service in passwords:
    passwords[service] = (username, password)
  else:
    print("Error: Service not found")

def delete_password(service):
  if service in passwords:
    del passwords[service]
  else:
    print("Error: Service not found")

def main():
  while True:
    print("Enter 1 to add a password")
    print("Enter 2 to retrieve a password")
    print("Enter 3 to change a password")
    print("Enter 4 to delete a password")
    print("Enter 0 to exit")
    choice = int(input())

    if choice == 1:
      service = input("Enter the service name: ")
      username = input("Enter the username: ")
      password = getpass.getpass("Enter the password: ")
      add_password(service, username, password)
    elif choice == 2:
      service = input("Enter the service name: ")
      password = get_password(service)
      if password is not None:
        print(f"Username: {password[0]}")
        print(f"Password: {password[1]}")
      else:
        print("Error: Service not found")
    elif choice == 3:
      service = input("Enter the service name: ")
      username = input("Enter the new username: ")
      password = getpass.getpass("Enter the new password: ")
      change_password(service, username, password)
    elif choice == 4:
      service = input("Enter the service name: ")
      delete_password(service)
    elif choice == 0:
      break
    else:
      print("Invalid choice")

if __name__ == "__main__":
  main()
