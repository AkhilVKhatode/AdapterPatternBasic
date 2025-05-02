from abc import ABC, abstractmethod

class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# AirConditioner.py - Device using Bluetooth for communication
class AirConditioner:
    def connect_via_bluetooth(self):
        print("Air Conditioner connected via Bluetooth.")
    
    def start_cooling(self):
        print("Air Conditioner is now cooling.")
    
    def stop_cooling(self):
        print("Air Conditioner stopped cooling.")
    
    def disconnect_bluetooth(self):
        print("Air Conditioner disconnected from Bluetooth.")

# SmartLight.py - Device using Wi-Fi for communication
class SmartLight:
    def connect_to_wifi(self):
        print("Smart Light connected to Wi-Fi.")
    
    def switch_on(self):
        print("Smart Light is now ON.")
    
    def switch_off(self):
        print("Smart Light is now OFF.")
    
    def disconnect_wifi(self):
        print("Smart Light disconnected from Wi-Fi.")

# CoffeeMachine.py - Device using Zigbee for communication
class CoffeeMachine:
    def initialize_zigbee_connection(self):
        print("Coffee Machine connected via Zigbee.")
    
    def start_brewing(self):
        print("Coffee Machine is now brewing coffee.")
    
    def stop_brewing(self):
        print("Coffee Machine stopped brewing coffee.")
    
    def terminate_zigbee_connection(self):
        print("Coffee Machine disconnected from Zigbee.")

# Adapter for Air Conditioner
class AirConditionerAdapter(SmartDevice):
    def __init__(self, air_conditioner):
        self.air_conditioner = air_conditioner
    
    def turn_on(self):
        self.air_conditioner.connect_via_bluetooth()
        self.air_conditioner.start_cooling()
    
    def turn_off(self):
        self.air_conditioner.stop_cooling()
        self.air_conditioner.disconnect_bluetooth()

# Adapter for Smart Light
class SmartLightAdapter(SmartDevice):
    def __init__(self, smart_light):
        self.smart_light = smart_light
    
    def turn_on(self):
        self.smart_light.connect_to_wifi()
        self.smart_light.switch_on()
    
    def turn_off(self):
        self.smart_light.switch_off()
        self.smart_light.disconnect_wifi()

# Adapter for Coffee Machine
class CoffeeMachineAdapter(SmartDevice):
    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine
    
    def turn_on(self):
        self.coffee_machine.initialize_zigbee_connection()
        self.coffee_machine.start_brewing()
    
    def turn_off(self):
        self.coffee_machine.stop_brewing()
        self.coffee_machine.terminate_zigbee_connection()

# SmartHomeController.py - Main driver class to control all devices
def main():
    # Create adapters for each device
    air_conditioner = AirConditionerAdapter(AirConditioner())
    smart_light = SmartLightAdapter(SmartLight())
    coffee_machine = CoffeeMachineAdapter(CoffeeMachine())
    
    # Control devices through the unified interface
    air_conditioner.turn_on()
    smart_light.turn_on()
    coffee_machine.turn_on()
    
    air_conditioner.turn_off()
    smart_light.turn_off()
    coffee_machine.turn_off()

if __name__ == "__main__":
    main()
