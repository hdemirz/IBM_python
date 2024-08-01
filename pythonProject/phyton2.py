# Noktaların Tanımlanması
points = [(1, 2), (3, 4), (6, 8), (2, 1)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) ** 0.5

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print(f"{points[i]} ve {points[j]} arasındaki Öklid mesafesi: {distance:.2f}")

# Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonuçların Yazdırılması
print("Noktalar arasındaki Öklid mesafeleri:", distances)
print("Minimum Öklid mesafesi:", min_distance)
