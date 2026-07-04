# Spam Detector using Linear Search

# Blacklist of spam sender IDs (unordered)
blacklist = [1023, 2045, 3098, 4567, 5890]

# Input sender ID
sender_id = int(input("Enter Sender ID: "))

# Linear Search
found = False

for id in blacklist:
    if id == sender_id:
        found = True
        break

# Output
if found:
    print("Spam Detected! Email Blocked.")
else:
    print("Safe Email. Sender is not in the blacklist.")