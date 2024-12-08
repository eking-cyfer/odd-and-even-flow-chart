# Odd and Even Numbers Chart

# Define the range
start = 1
end = 20

print("Odd and Even Numbers Chart:")
print("Odd Numbers     Even Numbers")
print("-" * 30)

# Loop through the range
for i in range(start, end + 1):
    if i % 2 != 0:  # Check if the number is odd
        print(f"{i:<14}", end="")  # Print odd number
    else:
        print(f"{i:<14}")  # Print even number on the same line
