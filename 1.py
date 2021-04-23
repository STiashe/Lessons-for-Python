from time import sleep


class TrafficLight:
    __color = 0

    def running(self):
        TrafficLight.__color += 1


a = TrafficLight()
print(a)
