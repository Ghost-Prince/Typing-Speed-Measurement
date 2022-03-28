import time
now=time.time()
string=input("Enter a string: ")
duration=time.time()-now
print("Time taken: ",duration)
print("Length of string: ", len(string))
print("Keystrokes per second: ", len(string)/duration)