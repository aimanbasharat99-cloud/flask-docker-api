import requests

# Test datetime route
response = requests.get("http://localhost:12000/datetime")
print("Datetime response:", response.json())

# Test image flip
files = {'image': open('test.jpg', 'rb')}
response = requests.post("http://localhost:12000/flip", files=files)

with open("flipped.jpg", "wb") as f:
    f.write(response.content)

print("Flipped image saved as flipped.jpg")