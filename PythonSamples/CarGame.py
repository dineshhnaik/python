#Simple Car game

car_started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("Car is already started")
        else:
            car_started = True
            print("Starting the car!")
    elif command == "stop":
        if car_started:
            car_started = False
            print("Stopping the car!")
        else:
            print("Car is already stopped")
    elif command == "quit":
        print("Quitting the application")
        break
    elif command == "help":
        print('''List of valid commands are:
Start - Start the car
Stop - Stop the car
Quit - Quit the application
Help''')
    else:
        print("Please enter a valid command!")

