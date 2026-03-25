import time

text = "python is powerful"

input("Press enter")

start = time.time()

t = input("Type: " + text + "\n")

end = time.time()

print("Time:", end - start)