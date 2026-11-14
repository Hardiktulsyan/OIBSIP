# BMI Calculator
# Asks for weight and height, shows the BMI and category, and saves every result to a file.

HISTORY_FILE = "bmi_history.txt"


def get_number(message, minimum, maximum):
    # Keep asking until the user types a number between minimum and maximum
    while True:
        text = input(message)
        if text.replace(".", "", 1).isdigit():
            number = float(text)
            if minimum <= number <= maximum:
                return number
        print("Invalid input. Enter a number between", minimum, "and", maximum)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def save_result(name, weight, height, bmi, category):
    file = open(HISTORY_FILE, "a")
    file.write(name + "," + str(weight) + "," + str(height) + "," + str(bmi) + "," + category + "\n")
    file.close()


def show_history(name):
    try:
        file = open(HISTORY_FILE, "r")
    except FileNotFoundError:
        print("No history yet.")
        return

    found = False
    for line in file:
        parts = line.strip().split(",")
        if parts[0] == name:
            print("Weight:", parts[1], "kg | Height:", parts[2], "m | BMI:", parts[3], "|", parts[4])
            found = True
    file.close()

    if not found:
        print("No history for", name)


def calculate(name):
    weight = get_number("Enter weight in kg: ", 2, 500)
    height = get_number("Enter height in metres: ", 0.5, 2.5)

    bmi = round(weight / (height * height), 1)
    category = get_category(bmi)

    print("Your BMI is", bmi, "-", category)
    save_result(name, weight, height, bmi, category)


# ---------- Main program ----------
name = input("Enter your name: ").strip()

while True:
    print()
    print("1. Calculate BMI")
    print("2. View my history")
    print("3. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        calculate(name)
    elif choice == "2":
        show_history(name)
    elif choice == "3":
        print("Goodbye.")
        break
    else:
        print("Please choose 1, 2 or 3.")
