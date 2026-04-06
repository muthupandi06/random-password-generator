from password_generator import generate_password

def main():
    try:
        length = int(input("Enter password length: "))
        
        if length <= 0:
            print("Please enter a valid positive number.")
            return
        
        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()