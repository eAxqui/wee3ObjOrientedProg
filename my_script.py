# Third Week Script Demo

""" Working on variables and operators """

x = 22 #integer
floot = 99.9 #Float
team = "Calgary Flames" #String
is_flames_awesome = True #Bool
is_oilers_awesome = False #Bool
my_new_var = 87 # Int

# Printing values of variables
print(x)
print(floot)
print(team)
print(is_flames_awesome)
print(is_oilers_awesome)

# Printing the data types
print(type(x))
print(type(floot))
print(type(team))
print("This statement is 100% true.", type(is_flames_awesome))
print(type(is_oilers_awesome))

# Input function
year_of_birth = input("Input your year of birth please: ")
output_year = 2025 - int(year_of_birth)
print("Your age is: ", output_year)

# Functions
# Functions called and used: print, input, int, float, str, bool

# Salary per hour calculator

hours_worked = input("How many hours did you work today?")
hourly_wage = 30

output_salary = hourly_wage * int(hours_worked)
print("Your wage is: ", output_salary)