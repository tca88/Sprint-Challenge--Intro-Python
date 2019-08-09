# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#VEHICLE IS A BASE/PARENT CLASS
class Vehicle:
    def __init__(self):
        pass
#############

#FLIGHTVEHICLE IS A SUBCLASS/CHILD CLASS of VEHICLE
class FlightVehicle(Vehicle): # "is-a" relationship
    def __init__(self):
        pass
#############

#GROUNDVEHICLE IS A SUBCLASS/CHILD CLASS of VEHICLE
class GroundVehicle(Vehicle): # "is-a" relationship
    def __init__(self):
        pass
#############

#STARSHIP IS A SUBCLASS/CHILD CLASS of FLIGHTVEHICLE
class Starship(FlightVehicle): # "is-a" relationship
    def __init__(self):
        pass
#############

#AIRPLANE IS A SUBCLASS/CHILD CLASS of FLIGHTVEHICLE
class Airplane(FlightVehicle): # "is-a" relationship
    def __init__(self):
        pass
#############

#CAR IS A SUBCLASS/CHILD CLASS of GROUNDVEHICLE
class Car(GroundVehicle): # "is-a" relationship
    def __init__(self):
        pass
#############

#MOTORCYCLE IS A SUBCLASS/CHILD CLASS of GROUNDVEHICLE
class Motorcycle(GroundVehicle): # "is-a" relationship
    def __init__(self):
        pass
#############