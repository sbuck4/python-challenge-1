# Dictionary full of info
my_info = { 'name' : 'Spencer',
           'age' : 25 ,
           'hobbies' : [ 'soccer', 'sleeping', 'video games', 'night sweats'] ,
           'wake-up' : {
               "Monday" : "6:30" , 
               "Tuesday" : "6:30" , 
               "Wednesday" : "6:30" ,
               "Thursday" : "6:30" ,
               "Friday" : "6:30" ,
               "Saturday" : "6:30" , 
               "Sunday" : "6:30" ,

           }


}

# Print out results stored in the dictionary
print(f"My name is {my_info['name']} and I am {my_info['age']} years old.")
print("-" * 50)
# Use a loop to print out the key-value pairs in the dictionary
for key, value in my_info.items() : 
    print(f"My{key} is {value}")

for key, value in my_info.items() :
    print(f"My{key} is {value}")

# Use a loop to print out the keys of the wake-up dictionary
for key in my_info['wake-up'] :
    print(key)

# Use a loop to print out the values of the wake-up dictionary
