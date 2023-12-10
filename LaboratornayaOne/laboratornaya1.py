import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

class EllipseWithPoints:
    def __init__(self, x, y, width, height, num_points):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.num_points = num_points
        self.ellipse = Ellipse((x, y), width=width*2, height=height*2, fill=False, color='b')
        self.points_x, self.points_y = self.generate_points()

    def generate_points(self):
        points_x = []
        points_y = []
        while len(points_x) < self.num_points:
            angle = np.random.uniform(0, 2 * np.pi)
            radius = np.random.uniform(0, 1)

            point_x = self.x + radius * self.width * np.cos(angle)
            point_y = self.y + radius * self.height * np.sin(angle)
            # Проверка, что точка внутри эллипса
            if ((point_x - self.x) / self.width) ** 2 + ((point_y - self.y) / self.height) ** 2 <= 1:
                points_x.append(point_x)
                points_y.append(point_y)
            else:
                continue
        return points_x, points_y

def read_input(filename):
    with open(filename, 'r') as file:
        Nk = int(file.readline().strip())  # Количество классов (эллипсов)
        counts = [int(line.strip()) for line in file]  # Количество точек внутри каждого эллипса
    return Nk, counts

def save_data_to_file(ellipses_data, filename):
    with open(filename, 'w') as file:
        for ellipse in ellipses_data:
            file.write(f"{ellipse.x}, {ellipse.y}, {ellipse.width}, {ellipse.height}\n")
            for i in range(len(ellipse.points_x)):
                file.write(f"{ellipse.points_x[i]}, {ellipse.points_y[i]}\n")

def generate_ellipses(Nk, counts):
    ellipses = []
    for num_points in counts:
        x = np.random.rand() * 10  # случайная координата X центра эллипса
        y = np.random.rand() * 10  # случайная координата Y центра эллипса
        width = np.random.rand() * 3  # случайная ширина эллипса
        height = np.random.rand() * 3  # случайная высота эллипса
        ellipse = EllipseWithPoints(x, y, width, height, num_points)
        ellipses.append(ellipse)
    return ellipses

def visualize_ellipses(ellipses):
    fig, ax = plt.subplots()
    for ellipse in ellipses:
        # Добавление эллипса на график
        ax.add_patch(ellipse.ellipse)
        # Добавление точек внутри эллипса
        ax.plot(ellipse.points_x, ellipse.points_y, 'o', markersize=1)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Генерированные эллипсы и точки внутри них')
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    Nk, counts = read_input("tochk.txt")
    ellipses_data = generate_ellipses(Nk, counts)
    
    # Визуализация
    visualize_ellipses(ellipses_data)

    # Сохранение сгенерированных данных в файл
    save_data_to_file(ellipses_data, "output.txt")