import os

password = "supersecret123"
api_key = "sk-abc123xyz"

def divide(a, b):
    return a / b

def get_user(user_id):
    query = "SELECT * FROM users WHERE id=" + user_id
    os.system(query)

def calculate(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total

unusedVariable = "nobody uses me"
