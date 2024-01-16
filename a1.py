#Name: Anas Sajid
#Student ID: 501167312
#Description: It is very hard for many people to determine whether or not buying an electric car would be a good financial decision. This program will compare the cost and 
#efficiency of an electric and a traditional car and will return an approximation of how many kilometers it will take for the electric car to become more (or less) cost efficient than the standard car
#to help determine whether the user should buy the standard or electric car.

#Function to welcome user and explain the program.
def welcome():
  print("Hello, this program will help you determine how many kilometers it will take for an electric car to be more cost efficient (or inefficient) than a regular car.\n")
  return None

#Function to write an appropriate farewell message.
def exit():
  print("\nThank you for using this program! Goodbye!")
  return None

#Function to get input from the user for the cost of the electric car.
def get_e_car_cost():
  #Loop to keep asking the user for input until they input a valid number.
  while True:
    try:
      e_car_cost=float(input("Please enter the cost of the electric car you wish to purchase (in CAD): "))
      break
    except:
      pass
  #Return the inputted cost of the electric car.
  return e_car_cost


#Function to get input from the user for the cost of the electricity.
def get_e_cost():
  #Loop to keep asking the user for input until they input a valid number.
  while True:
    try:
      e_cost=float(input("Please enter the cost of one KWh of electricity (in CAD): "))
      break
    except:
      pass
  #Return the inputted cost of electricity.
  return e_cost


#Function to get input from the user for the efficiency of the car (Km/KWh).
def get_e_car_efficiency():
  #Loop to keep asking the user for input until they input a valid number.
  while True:
    try:
      e_efficiency=float(input("Please enter the efficiency of the electric car you wish to purchase (in Km/KWh): "))
      break
    except:
      pass
  #Return the inputted efficiency of the electric car.
  return e_efficiency


#Function to get input for the cost of the regular car from the user.
def get_reg_cost():
  #Loop to keep asking the user for input until they input a valid number.
  while True:
    try:
      reg_cost=float(input("\nPlease enter the cost of the regular car you wish to purchase (in CAD): "))
      break
    except:
      pass
  #Return the inputted cost of the regular car.
  return reg_cost


#Function to get the price of gas (per liter) from the user.
def get_gas_price():
  #Loop to keep asking the user for input until they input a valid number.
  while True:
    try:
      gas_price=float(input("Please enter the cost of 1 liter of gas (in CAD): "))
      break
    except:
      pass
  #Return the inputted gas price.
  return gas_price


#Function to get the efficiency of the regular car from the user (Km/L).
def get_reg_efficiency():
  #Loop to keep asking the user for input until they input a valid number.
  while True:
    try:
      reg_efficiency=float(input("Please enter the cost efficiency of the regular car you wish to purchase (in Km/L): "))
      break
    except:
      pass
  #Return the inputted efficiency of the regular car.
  return reg_efficiency


#Function to calculate the cost for one kilometer of driving for the electric car.
def get_e_car_cost_per_km(e_cost, e_efficiency):
  #Return the cost per kilometer of driving of the electric car.
  return (e_cost/e_efficiency)


#Function to calculate the cost for one kilometer of driving for the regular car.
def get_reg_car_cost_per_km(gas_price, reg_efficiency):
  #Return the cost per kilometer of driving of the regular car.
  return (gas_price/reg_efficiency)

if __name__=="__main__":
  #Call upon the welcome function to greet the user.
  welcome()
  #Set a variable for the average daily drive distance of a Canadian driver.
  avg_daily_canadian_drive=15200/365

  #Set the boolean variable 'run' as True.
  run=True

  #Keep running the following code while the variable 'run' is True.
  while run==True:

    #Create a variable for the cost of the electric car and run the 'get_e_car_cost' function to assign it a value.
    e_car_cost=get_e_car_cost()
    #Create a variable for the cost of electricity and run the 'get_e_cost' function to assign it a value.
    e_cost=get_e_cost()
    #Create a variable for the efficiency of the electric car and run the 'get_e_car_efficiency' function to assign it a value.
    e_car_efficiency=get_e_car_efficiency()

    #Create a variable for the cost of the regular car and run the 'get_reg_cost' function to assign it a value.
    reg_car_cost=get_reg_cost()
    #Create a variable for the cost of gas and run the 'get_gas_price' function to assign it a value.
    gas_price=get_gas_price()
    #Create a variable for the efficiency of the regular car and run the 'get_reg_efficiency' function to assign it a value.
    reg_efficiency=get_reg_efficiency()

    #Create a variable for the cost to drive one kilometer in the electric car and assign it a value by calling the 'get_e_car_cost_per_km' function.
    e_car_cost_per_km=get_e_car_cost_per_km(e_cost, e_car_efficiency)
    #Create a variable for the cost to drive one kilometer in the regular car and assign it a value by calling the 'get_reg_car_cost_per_km' function.
    reg_car_cost_per_km=get_reg_car_cost_per_km(gas_price, reg_efficiency)

    #Calculate the difference in cost between the electric car and regular car.
    car_cost_diff=e_car_cost-reg_car_cost
    #Calculate the difference in the cost per kilometer between the regular car and the electric car.
    cost_efficiency_diff= reg_car_cost_per_km-e_car_cost_per_km

    #Print an appropriate message if both cars cost the same and have the same cost per kilometer of driving.
    if e_car_cost==reg_car_cost and e_car_cost_per_km==reg_car_cost_per_km:
      print("\nThe electric car will always be equally cost efficient.")

    #Print an appropriate message if the electric car costs more and has a lower cost per kilometer of driving.
    elif e_car_cost>reg_car_cost and e_car_cost_per_km<reg_car_cost_per_km:
      print(f"\nThe electric car will be more cost efficient after {round((car_cost_diff/cost_efficiency_diff), 2)}km.\nThat is approximately {round((car_cost_diff/cost_efficiency_diff)/avg_daily_canadian_drive)} days for the average Canadian driver.")

    #Print an appropriate message if the electric car costs more than or equal to the regular car and has a greater or equal cost per kilometer of driving.
    elif e_car_cost>=reg_car_cost and e_car_cost_per_km>=reg_car_cost_per_km:
      print("\nThe electric car will never be more cost efficient.")

    #Print an appropriate message if the electric car costs less than or equal to the regular car and has a lesser or equal cost per kilometer of driving.
    elif e_car_cost<=reg_car_cost and e_car_cost_per_km<=reg_car_cost_per_km:
      print("\nThe electric car will always be more cost efficient.")

    #Print an appropriate message if the electric car costs less than the regular car but has a greater cost per kilometer of driving.
    elif e_car_cost<reg_car_cost and e_car_cost_per_km>reg_car_cost_per_km:
      print(f"\nThe electric car will be more cost efficient until {round((car_cost_diff/cost_efficiency_diff), 2)}km.\nThat is approximately {round((car_cost_diff/cost_efficiency_diff)/avg_daily_canadian_drive)} days for the average Canadian driver.")

    #Prompt the character to input whether they would like to continue using the program or if they would like to exit.
    quit_or_cont=input("\nPlease enter \'n\' if you wish to quit and any other key if you wish to use the program again: ")

    #Set run=False to quit the program if the user inputted 'n'.
    if quit_or_cont=='n':
      run=False
    #If the user did not input 'n', print two blank lines so the program looks neater when it runs again.
    else:
      print("\n\n")
  #Print an appropriate farewell message using the 'exit' function
  exit()