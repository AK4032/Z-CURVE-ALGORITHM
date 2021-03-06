import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import time
start = time.time()
 
def RYArray(Genome):
    skew = {0:0}
    for i in range(len(Genome)):
        if Genome[i] == "A" or Genome[i] == "G":
            skew[i+1] = skew[i] + 1
        elif Genome[i] == "C" or Genome[i] == "T":
            skew[i+1] = skew[i] - 1
    return skew

def RYSkew(Genome):
    positions = []
    skew = RYArray(Genome)
    minvalue = (min(skew.values()))
    for i in skew:
        if skew[i] == minvalue:
            positions.append(i)
    return positions

def MKArray(Genome):
    skew = {0:0}
    for i in range(len(Genome)):
        if Genome[i] == "A" or Genome[i] == "C":
            skew[i+1] = skew[i] + 1
        elif Genome[i] == "G" or Genome[i] == "T":
            skew[i+1] = skew[i] - 1
    return skew

def MKSkew(Genome):
    positions = []
    skew = MKArray(Genome)
    minvalue = (max(skew.values()))
    for i in skew:
        if skew[i] == minvalue:
            positions.append(i)
    return positions

def GCSkew(Genome):
    positions = []
    skew = GCArray(Genome)
    minvalue = (min(skew.values()))
    for i in skew:
        if skew[i] == minvalue:
            positions.append(i)
    return positions

def GCArray(Genome):
    skew = {0:0}
    for i in range(len(Genome)):
        if Genome[i] == "G":
            skew[i+1] = skew[i] + 1
        elif Genome[i] == "C":
            skew[i+1] = skew[i] - 1
        elif Genome[i] == "A" or "T":
            skew[i+1] = skew[i]
    return skew

def ATSkew(Genome):
    positions = []
    skew = ATArray(Genome)
    minvalue = (max(skew.values()))
    for i in skew:
        if skew[i] == minvalue:
            positions.append(i)
    return positions

def ATArray(Genome):
    skew = {0:0}
    for i in range(len(Genome)):
        if Genome[i] == "A":
            skew[i+1] = skew[i] + 1
        elif Genome[i] == "T":
            skew[i+1] = skew[i] - 1
        elif Genome[i] == "G":
            skew[i+1] = skew[i]
        elif Genome[i] == "C":
            skew[i+1] = skew[i]
    return skew

f = open("Halobacterium sp. NRC-1.txt", "r")
contents = f.read()
whitelist = set('ACGT')
contents = ''.join([c for c in contents if c in whitelist])
print(RYSkew(contents))
print(MKSkew(contents))
print(GCSkew(contents))
print(ATSkew(contents))

end = time.time()
print(end-start)

plt.plot(RYArray(contents).values(), color = 'red')
plt.plot(MKArray(contents).values(), color = 'blue')
plt.plot(GCArray(contents).values(), color = 'green')
plt.plot(ATArray(contents).values(), color = 'yellow')

plt.title('Z curve for Halobacterium sp NRC-1')

plt.xlabel('position (bp)')
plt.ylabel('skew (bp)')

red_patch = mpatches.Patch(color='red', label='RY Skew')
blue_patch = mpatches.Patch(color='blue', label='MK Skew')
green_patch = mpatches.Patch(color='green', label='GC Skew')
yellow_patch = mpatches.Patch(color='yellow', label = 'AT Skew')
plt.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])

plt.show()

