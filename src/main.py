def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("Hello, World!")
    print("Термометр:")
    c = 25
    print(f"{c}°C дорівнює {celsius_to_fahrenheit(c)}°F")

if __name__ == "__main__":
    main()