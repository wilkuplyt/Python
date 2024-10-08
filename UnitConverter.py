def length_converter(value, from_unit, to_unit):
    units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
    }
    
    if from_unit not in units or to_unit not in units:
        return None
    
    value_in_meters = value * units[from_unit]
    converted_value = value_in_meters / units[to_unit]
    return converted_value

def weight_converter(value, from_unit, to_unit):
    units = {
        'grams': 1,
        'kilograms': 1000,
        'pounds': 453.592,
        'ounces': 28.3495,
    }

    if from_unit not in units or to_unit not in units:
        return None
    
    value_in_grams = value * units[from_unit]
    converted_value = value_in_grams / units[to_unit]
    return converted_value

def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return None

def main():
    while True:
        print("\nUnit Converter")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        choice = input("Choose a conversion type (1-4): ")

        if choice == '1':
            value = float(input("Enter value: "))
            from_unit = input("Convert from (meters, kilometers, centimeters, millimeters, miles, yards, feet): ").lower()
            to_unit = input("Convert to (meters, kilometers, centimeters, millimeters, miles, yards, feet): ").lower()
            result = length_converter(value, from_unit, to_unit)
            if result is not None:
                print(f"{value} {from_unit} is {result} {to_unit}.")
            else:
                print("Invalid units.")

        elif choice == '2':
            value = float(input("Enter value: "))
            from_unit = input("Convert from (grams, kilograms, pounds, ounces): ").lower()
            to_unit = input("Convert to (grams, kilograms, pounds, ounces): ").lower()
            result = weight_converter(value, from_unit, to_unit)
            if result is not None:
                print(f"{value} {from_unit} is {result} {to_unit}.")
            else:
                print("Invalid units.")

        elif choice == '3':
            value = float(input("Enter value: "))
            from_unit = input("Convert from (celsius, fahrenheit, kelvin): ").lower()
            to_unit = input("Convert to (celsius, fahrenheit, kelvin): ").lower()
            result = temperature_converter(value, from_unit, to_unit)
            if result is not None:
                print(f"{value} {from_unit} is {result} {to_unit}.")
            else:
                print("Invalid units.")

        elif choice == '4':
            print("Exiting the converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
