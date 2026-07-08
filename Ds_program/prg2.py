# Sorted list of laptop prices
prices = [25000, 32000, 40000, 50000, 55000, 62000, 70000]

# User enters the minimum price
target = int(input("Enter minimum price: "))

low = 0
high = len(prices) - 1
answer = -1

# Binary Search
while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        answer = mid          # Store the possible answer
        high = mid - 1        # Search on the left side
    else:
        low = mid + 1         # Search on the right side

# Display Result
if answer != -1:
    print("First laptop price >= ₹", target, "is ₹", prices[answer])
else:
    print("No laptop found in this price range.")
