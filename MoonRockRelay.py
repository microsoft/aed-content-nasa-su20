class Camera:
  pass

rover_1 = Camera()


def countMoonRocks(s, brown, black, grey):

  if("brown" in s):
      print("found a brown\n")
      rover_1.brown += 1

  if("black" in s):
    print("found a black\n")
    rover_1.black += 1

  if("grey" in s):
    print("found a grey\n")
    rover_1.grey += 1

  if("unknown" in s):
    print("found an unknown rock\n")
    rover_1.unknown += 1
    
  return 

print("Artemis Rover Starting\n")

rover_1.brown = 0
rover_1.black = 0
rover_1.grey = 0
rover_1.unknown = 0

strPath = "test.txt"
f = open(strPath)
line = f.readline()

while line:
    countMoonRocks(line, rover_1.brown, rover_1.black, rover_1.grey)
    line = f.readline()
f.close()

print("Number of brown:")
print(rover_1.brown)

print("Number of black:")
print(rover_1.black)

print("Number of grey:")
print(rover_1.grey)

print("Number of unknown:")
print(rover_1.unknown)



