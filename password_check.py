def main():
    password = input("pwd")
    if len(password) < 8 or len(password) > 20:
        print("Invalid")

main()