# Topic 04 Collaborative Assignment
# Your Name: Lauren Grogean 
# Date: 6/20/26

# --- STARTER CODE ---
# This starter program checks if a temperature is hot, warm, or cold.
# Extend it, change the theme, or use it as inspiration for your own idea. 

temp_input = input("Enter a temperature in Fahrenheit: ")
temperature = float(temp_input)

if temperature >= 90:
    print("It is hot outside.")
elif temperature >= 60:
    print("It is warm outside.")
else:
    print("It is cold outside.")

# --- YOUR EXTENSION BELOW THIS LINE ---
# Ideas: Add more conditions, change the topic entirely,
# or add a second input and a second set of branches.

hours_input = input("How many hours do you plan to spend outside today?")
hours = int(hours_input)

if hours >= 5:
  print("Don't forget sunscreen and plenty of water.")
elif hours >= 2:
  print("Sounds like a good amount of time outside.")
else:
  print("You won't be outside for very long.")

if temperature >= 90 and hours >= 5:
  print("Be careful in the heat and hydrate!")
elif temperature < 60:
  print("Consider having a jacket.")
else:
  print("Have an amazing day.")
