import math
import sys

class Car:
    def __init__(self,x,y, v):
        # check for constraints and initialize coordinate (x,y) and speed (v)
        if ((x >= -10**9 and x <= 10**9) and (y >= -10**9 or y <= 10**9) and (v >= 1 and v <= 10**9)):
            self.x = x
            self.y = y
            self.v = v 
        else:
            print("Inavlid inputs...Run again!")
            sys.exit()

        # time to reach the origin = distance(sqrt(x^2 + y^2)) / speed
        self.time = math.sqrt(self.x**2 + self.y **2)/self.v

# Cars will collide if their they reach at the origin at the exact same time.
def collide(car1, car2):
    if car1.time == car2.time:
        return True

if __name__=='__main__':
    cars = {}
    count = 0
    
    # Input number of Cars
    c = int(input())
    
    if (c < 1 or c > 10**5):
        print("Too many or Too few Cars....")
        sys.exit()

    # input three space deliminited values. Firts two are cordinates of location. Third one is speed.
    for i in range(c):
        x, y, speed = [ int(i) for i in input().split(' ') ]
        cars[i] = Car(x,y,speed)

    # iterate over cars and check for two cars at a time.
    # increase count by one if they collide
    for i in range(len(cars)):
        for j in range(i+1,len(cars)):
            if collide(cars[i],cars[j]):
                count += 1

    # print Output
    print(count)