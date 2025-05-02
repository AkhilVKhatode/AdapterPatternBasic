# Smart Home System - Adapter Design Pattern

This repository implements a Smart Home System using the Adapter Design Pattern to control multiple devices through a unified interface. The system controls various smart devices like an Air Conditioner, Smart Light, and Coffee Machine, each communicating over different protocols (Bluetooth, Wi-Fi, Zigbee). By using adapter classes, the system provides a common interface to interact with different devices.

## Project Overview

This project demonstrates how to use the Adapter Design Pattern to integrate devices that use different communication protocols (Bluetooth, Wi-Fi, Zigbee) into a unified smart home control system. The code uses Python's abstract base class (ABC) to create a `SmartDevice` interface that all device-specific adapters implement.

### Devices Included:
- **Air Conditioner**: Communicates via Bluetooth.
- **Smart Light**: Communicates via Wi-Fi.
- **Coffee Machine**: Communicates via Zigbee.

Each device has its own communication and control logic, but through adapters, we can control them using the same methods.

## Files

- `SmartDevice.py`: Defines the `SmartDevice` interface, which all device-specific adapters implement.
- `AirConditioner.py`: Contains the logic for controlling an Air Conditioner using Bluetooth.
- `SmartLight.py`: Contains the logic for controlling a Smart Light using Wi-Fi.
- `CoffeeMachine.py`: Contains the logic for controlling a Coffee Machine using Zigbee.
- `AirConditionerAdapter.py`: Adapter for the Air Conditioner to conform to the `SmartDevice` interface.
- `SmartLightAdapter.py`: Adapter for the Smart Light to conform to the `SmartDevice` interface.
- `CoffeeMachineAdapter.py`: Adapter for the Coffee Machine to conform to the `SmartDevice` interface.
- `SmartHomeController.py`: Main script to control all devices via their adapters.

## How It Works

1. **Air Conditioner**: The `AirConditioner` class connects to the device via Bluetooth, starts cooling, and provides methods to stop cooling and disconnect Bluetooth.
   
2. **Smart Light**: The `SmartLight` class connects to the device via Wi-Fi, switches the light on or off, and disconnects the Wi-Fi when finished.

3. **Coffee Machine**: The `CoffeeMachine` class initializes a Zigbee connection, starts brewing coffee, and provides methods to stop brewing and disconnect the Zigbee connection.

4. **Adapters**: Each device has a corresponding adapter that implements the `SmartDevice` interface. The adapter allows the device to be controlled through the same `turn_on()` and `turn_off()` methods, despite each device using different communication protocols.

## Example Usage

```python
from AirConditionerAdapter import AirConditionerAdapter
from SmartLightAdapter import SmartLightAdapter
from CoffeeMachineAdapter import CoffeeMachineAdapter
from AirConditioner import AirConditioner
from SmartLight import SmartLight
from CoffeeMachine import CoffeeMachine

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
```
