import requests

for _ in range(4):
    print("hello")

name = input("Enter your name: ")
first_letter = name[0]
print("First letter of your name:", first_letter)
print("お前の名前は" + name[0] + "だ")



# Define the switchbot API endpoint
api_endpoint = "https://api.switch-bot.com/v1.0/devices/{device_id}/commands"

# Define the device ID of the switchbot light
device_id = "your_device_id"

# Define the command to turn on the light
command = {
    "command": "turnOn"
}

# Send the command to the switchbot API
response = requests.post(api_endpoint.format(device_id=device_id), json=command)

# Check if the command was successful
if response.status_code == 200:
    print("Light turned on successfully")
else:
    print("Failed to turn on the light")
