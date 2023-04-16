n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

# сортировка по правым концам
segments.sort(key=lambda x: x[1])

# список точек покрытия
points = []

# начинаем с самой правой точки
current_point = segments[0][1]
points.append(current_point)

for segment in segments:
    # если текущая точка не покрывает текущий отрезок, добавляем новую точку
    if current_point < segment[0] or current_point > segment[1]:
        current_point = segment[1]
        points.append(current_point)

print(len(points))
print(*points)