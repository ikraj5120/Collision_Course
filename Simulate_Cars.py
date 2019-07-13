import math


class Car:
    def __init__(self,x,y, speed):
        self.x = x # x cordinate
        self.y = y # y cordinate
        self.speed = speed 

        # time to reach the origin
        # sqrt(x^2 + y^2)/speed

        self.time = math.sqrt(self.x**2 + self.y **2)/self.speed

# Cars will collide if their they reach at the origin at the exact same time.

def collide(car1, car2):
    if car1.time == car2.time:
        return True

if __name__=='__main__':
    cars = {}
    count = 0
    
    # Input number of Cars
    c = int(input())
    
    # input three space deliminited values. Firts two are cordinates of location. Third one is speed.
    for i in range(c):
        x, y, speed = [int(i) for i in input().split(' ')]
        cars[i] = Car(x,y,speed)

    # iterate over cars and check for two cars at a tme.
    # increase count by one if they collide
    for i in range(len(cars)):
        for j in range(i+1,len(cars)):
            if collide(cars[i],cars[j]):
                count += 1

    # print Output
    print(count)