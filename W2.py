points = [(5,6),(8,10),(7,7),(3,10),(10,10)]
holder = []
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (((y2-y1)**2) + ((x2-x1)**2))**(1/2)

for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance = euclideanDistance(points[i],points[j])
        holder.append(distance)
print("Mesafeler")
for dist in holder:
    print(dist)