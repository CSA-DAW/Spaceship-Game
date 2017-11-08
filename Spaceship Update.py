#Denver Wydermyer
#Computer Prgramming
#10/18/17

Planet = ' '
Name = ' '

def game_intro():
    global Name 
    print(" Welcome to Spaceship Game 1! The object of the game is to be on a planet in the galaxy, figure out your ship weight, and how fast you want to go(km/s). If your weight and speed are correct for that planet you are fine, but if you speed and/or weight is incorrect you will blow up. continue on to your planet Astronaut!")
    Name =input("What is your name: ")



def menu():
    global Name
    global Planet
    print('Hi ' + Name)
    print("1. Start Game\n2. Enter Planet ")
    choice = input("Choice: ")
    if choice=="1":
        takeoff()
    elif choice =='2':
        location()

def location():
    global Planet
    Planet = input("What planet do you want to zoom to: \n1. Mercury\n2. Venus\n3. Earth\n4. Mars\n5. Jupiter\n6. Saturn\n7. Uranus\n8. Neptune")
    choice = input("Choice: ")

def takeoff():
    global Planet
    global speed
    speed = float(input("How fast do you want to go (in km/s): " ))
    weight = float(input("What is your ship weight: "))
    print('you are going %f' %speed) 


def escape_planet():
    if Planet == "Earth":
        esc=11.86
        check(esc,spped,destination)
    else:
        print("You did something wrong.Do it again!")
        
def check(esc,speed,destination):
    global planet
    if speed <=(esc * 1.1):
        print("You lived!your next destination is coming up!")
    else:
        print("You have gone boom boom!Try again!")
        menu()
        
    
game_intro()
menu()
location()
escape_planet()
check(esc,speed,destination)
