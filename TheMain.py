from InputParser import InputParser
from Deliver import DeliveryGuy

theParser = InputParser()
theParser.loadInput("test.in")

theDeliveryGuy = DeliveryGuy()
theDeliveryGuy.start(theParser.drones, theParser.orders, theParser.warehouses, theParser.deadline)

print (theDeliveryGuy.commands)