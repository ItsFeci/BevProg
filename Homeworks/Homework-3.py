
def division ():
    num_a = int(input("Enter 'a' value: "))
    num_b = int(input("Enter 'b' value: "))
    num_c = 0
    try:
        num_c = num_a / num_b
        print(num_c)
    except ZeroDivisionError:
        print("Division by Zero not allowed")
    finally:
        print("Out of try excpet blocks")

def main():
    while True:
        division()

if __name__ == "__main__":
    main()

    


