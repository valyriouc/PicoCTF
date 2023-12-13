import hashlib

username_trial = b"GOUGH"
testing = hashlib.sha256(username_trial).hexdigest()

result = f"{testing[4]}{testing[5]}{testing[3]}{testing[6]}{testing[2]}{testing[7]}{testing[1]}{testing[8]}"

print(result)