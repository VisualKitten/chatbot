print("What your name blyat")
user_name = input()
print("Hello, "+ user_name)
print("Where are you from?")
location = input()
print("I see, you are "+user_name+" and from "+location)
print("What's the weather like (rainy, clear, storm)")
weather = input()
if weather == "rainy":
    print("Rain must suck, doesn't it, "+user_name+"?")
elif weather == "sunny":
    print("Aren't sunny days great,"+user_name+"?")
elif weather == "clear":
    print("Days without clouds are sometimes weird, right, "+user_name+"?")
elif not weather == "clear" or "sunny" or "clear":
    print("Same here!")
print("How do you like this chatbot so far on a scale from 0 to 5, "+user_name+"?")
rating = input()
if rating == "0":
    print("Why so, "+user_name+" If you are encountering issues, report it on our GitHub repository")
elif rating == "1":
    print("Less than average, huh. Please report issues at github.com/VisualKitten/chatbot/issues.")
elif rating == "2":
    print("It's fine, "+user_name+" We get it, may be frustrating to understand the bot Report issues at our repository")
elif rating == "3":
    print("Thank you for the average, "+user_name+"! Your opinion matters.")
elif rating == "4" or "5":
    print("Thank you for the amazing feedback, "+user_name+"!")
print("Thank you for introducing yourself so far, "+user_name+"!")
print("My name is Kyle, I'm a Chatbot designed to put you out of miser- I MEAN out of boredom. I know how")
print("boredom feels. It sucks. Meanwhile I'm initializing code, may you solve this math problem for me?")
print("35+6 = ?")
math_answer1 = input()
if math_answer1 == "41":
    print("Thank you! That's the correct answer! Let's proceed.")
elif not math_answer1 == "41":
    print("No, not even close! Let's proceed anyways I guess.")
print("███████╗  ██╗    ██╗ ██╗ ███████╗")
print("██╔═══██╗ ██║    ██║ ██║ ╚══███╔╝")
print("██║   ██║ ██║    ██║ ██║   ███╔╝")
print("██║   ██║ ██║    ██║ ██║  ███╔╝")
print("╚████████╚ ██████╔╝  ██║ ███████╗")
print("        █               ")
print("If you didn't make out the above, we are gonna do a quiz.")
print("This concludes the chatbot. Stay tuned for more updates to this bot!")

