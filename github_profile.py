import requests

url = "https://api.github.com/users/shloka09"
response = requests.get(url)
profile = response.json()

print("Name:", profile["name"])
print("Bio:", profile["bio"])
print("Public repos:", profile["public_repos"])
print("Followers:", profile["followers"])
print("Location:", profile["location"])
print("Account created:", profile["created_at"][:10])