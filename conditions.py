# age = int(input("What's your age? "))
# if age >= 18:
#     print("You can vote or be voted for")
# else:
#     print("You cant vote")

light_color = input("What is the color of the light: ")
light_color = light_color.lower()
if light_color == "yellow":
    print("Ready to go")
elif light_color == "red":
    print("Stop")
elif light_color == "green":
    print("Go")
else:
    print('Invalid Input')



