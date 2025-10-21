def horoscope():
    horoscope = {
        "aries": "You're going to crush today’s Python class! LOOPS WILL FEAR YOU!",
        "taurus": "Your persistence will pay off when debugging that tricky syntax error.",
        "gemini": "Your curiosity will lead to some awesome discoveries in Python today.",
        "cancer": "Your creativity will shine when writing your first function.",
        "leo": "Everyone will admire your confidence when your code runs perfectly!",
        "virgo": "Your attention to detail will make your program flawless.",
        "libra": "You’ll find perfect balance between print statements and logic today.",
        "scorpio": "Your focus will help you master the while loop like a pro.",
        "sagittarius": "Adventure awaits! You’ll explore new Python concepts fearlessly!",
        "capricorn": "Your discipline will make today’s lesson look easy.",
        "aquarius": "You’ll have a brilliant idea that makes everyone say WHOA!",
        "pisces": "Your imagination will make your Python code surprisingly elegant."
    }

    while True:
        sign = input("Enter your zodiac sign: ").lower()

        if sign in horoscope:
            print(horoscope[sign])
            break
        else:
            print("That’s not a valid sign! Try again.\n")

# Run the function
horoscope()
