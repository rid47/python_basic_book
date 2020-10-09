import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

capital_list = list(capitals_dict.items())

state, true_capital = random.choice(capital_list)


while True:
    print(f"What is the capital of {state}?")
    input_capital = input("\nEnter Capital Name:")
    if input_capital.lower() == true_capital.lower():
        print("Correct")
        break
    elif input_capital.lower() == "exit":
        print(f"Correct Answer: {true_capital}")
        print("Goodbye")
        break
    # else:
    #     continue # its a while True loop; unless u break out force fully it will run contineously
