brown = 0
black = 0
grey = 0
unknown = 0

def countMoonRocks(s):

  if("brown" in s):
    print("found a brown\n")
    global brown 
    brown += 1

  if("black" in s):
    print("found a black\n")
    global black
    black += 1

  if("grey" in s):
    print("found a grey\n")
    global grey
    grey += 1

  if("unknown" in s):
    print("found an unknown rock\n")
    global unknown
    unknown +=1
    
  return 

print("Artemis Rover Starting\n")


strPath = "test.txt"
f = open(strPath)
line = f.readline()

while line:
    countMoonRocks(line)
    line = f.readline()
f.close()

print("Number of brown:")
print(brown)

print("Number of black:")
print(black)

print("Number of grey:")
print(grey)

print("Number of unknown:")
print(unknown)

print("the max number of one rock type is: ",max(brown, black, grey, unknown))
print("the minimum number of one rock type is: ", min(brown, black, grey, unknown))



