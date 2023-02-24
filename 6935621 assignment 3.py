# list of available cars and their prices
cars = {
'Audi' : 60000,
'Aston Martin' : 100000,
'Bentley' : 500000,
'BMW' : 56000,
'Bugatti' : 350000,
'Cadillac' : 800000,
'Chevrolet' : 70000,
'Ferrari' : 300000,
'Ford' : 90000,
'Honda' : 23000,
'Hyundai' : 14000,
'Jaguar' : 89000,
'Jeep' : 60000,
'Lamborghini' : 250000,
'Lexus' : 23000,
'Maserati' : 400000,
'Mazda' : 19000,
'Rolls-Royce ghost' : 200000,
'Tesla' : 100000,
'Toyota' : 30000,
'Volvo' : 21000,
}





  
car_name = input("Enter a car name: ")
if car_name in cars:
    print("Yes your car is available")
    car_price = cars[car_name]
    print(f"The price of {car_name} is ${car_price}.")
else:   
    print(f"Sorry,{car_name} is not available") 
    
    
# Github Repository Link https://github.com/derrickyebs/