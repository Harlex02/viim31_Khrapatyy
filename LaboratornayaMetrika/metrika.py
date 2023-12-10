import math

class Metric:
    def __init__(self):
        self.x = [5, 6, 3, 1, 0]
        self.y = [4, 2, 9, 5, 4]
        self.z = 0
        self.p = 2

    def euclid(self):
        for i in range(5):
            self.z += (self.x[i] - self.y[i]) ** 2
        return math.sqrt(self.z)

    def manhattan(self):
        for i in range(5):
            self.z += abs(self.x[i] - self.y[i])
        return self.z

    def ravnomer(self):
        for i in range(5):
            self.z = max(self.z, abs(self.x[i] - self.y[i]))
        return self.z

    def minkowski(self):
        for i in range(5):
            self.z += abs(self.x[i] - self.y[i]) ** self.p
        return self.z

if __name__ == "__main__":
    metric_instance = Metric()

    print("Euclidean =", metric_instance.euclid())
    print("Manhattan =", metric_instance.manhattan())
    print("Uniform =", metric_instance.ravnomer())
    print("Minkowski =", metric_instance.minkowski() ** (1/2))