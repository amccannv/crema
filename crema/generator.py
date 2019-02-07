import numpy as np
from math import radians, cos, sin

# Generate random points, rotation matrices, and translation vectors.
# To be used as test data to calibrate between two camera (coordinate) systems.
class Generator:
    def __init__(self):
        self.generateRandomBox()
        self.generateRotationMatrix()
        self.generateTranslationVector()
        self.gazeVectors = []
        self.eyeVectors = []

    # Generate a random box of points.
    def generateRandomBox(self):
        point = [3.0, 1.0, -10.0, 1.0]
        boxSize = 3.0
        self.box = np.array([[point[0], point[1], point[2], point[3]],
                             [point[0], point[1], point[2] + boxSize, point[3]],
                             [point[0], point[1] + boxSize, point[2], point[3]],
                             [point[0], point[1] + boxSize, point[2] + boxSize, point[3]],
                             [point[0] + boxSize, point[1], point[2], point[3]],
                             [point[0] + boxSize, point[1], point[2] + boxSize, point[3]],
                             [point[0] + boxSize, point[1] + boxSize, point[2], point[3]],
                             [point[0] + boxSize, point[1] + boxSize, point[2] + boxSize, point[3]]])

    # Generate a random rotation matrix.
    def generateRotationMatrix(self):
        rotationAngle = radians(30)
        self.rotationMatrix = np.array([[1.0, 0.0, 0.0],
                                        [0.0, cos(rotationAngle), -1 * sin(rotationAngle)],
                                        [0.0, sin(rotationAngle), cos(rotationAngle)],
                                        [0.0, 0.0, 0.0]])

    # Generate a random translation vector.
    def generateTranslationVector(self):
        self.translationVector = np.array([[-16.0, 0.0, 0.0, 1.0]])

    # Generate a random translation vector.
    def generateGazeVectors(self):
        return 1

    # Generate a random translation vector.
    def generateEyeVectors(self):
        return 1
