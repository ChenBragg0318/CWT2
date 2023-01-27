name=["Jules","Jone","Shah","Tom","Sue","Sameer"]
name.sort()
Greetings=("yall right?")
for x in range (len(name)):
 print(Greetings+name[x])

locations=["tokyo","shanghai","london","seoul","Busan","NewYork","Taipei"]
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

locations.append("Taichuang")
x=locations.pop(2)
print(x)

del locations[0]
locations.remove("Busan")

print(len(locations))

print(locations)
