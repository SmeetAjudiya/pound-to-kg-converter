def pounds_TO_kilograms(pounds):
    conversion_factor = 0.453592
    kilograms = pounds * conversion_factor
    return kilograms

def main():
    pounds = float(input("Enter Weight in Pounds:"))
    kilograms = pounds_TO_kilograms(pounds)
    print(f"{pounds} is equal to {kilograms:.2f} kilograms")

if __name__ == "__main__":
    main()