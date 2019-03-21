import numpy as np
from math import radians, cos, sin

# Generate random points, rotation matrices, and translation vectors.
# To be used as test data to calibrate between two camera (coordinate) systems.
class Generator:
    def __init__(self, static_eye=False):
        self.static_eye = static_eye
        self.generate_random_box()
        self.generate_rotation_matrix()
        self.generate_translation_vector()
        self.transformation_matrix = np.append(self.rotationMatrix, np.transpose(self.translationVector), axis=1)
        self.generate_new_points()
        self.generate_eye_vectors()
        self.generate_gaze_vectors()
        

    # Generate a random box of points.
    def generate_random_box(self):
        point = [3.0, 1.0, -10.0, 1.0]
        box_size = 3.0
        self.box = np.array([[point[0], point[1], point[2], point[3]],
                             [point[0], point[1], point[2] + box_size, point[3]],
                             [point[0], point[1] + box_size, point[2], point[3]],
                             [point[0], point[1] + box_size, point[2] + box_size, point[3]],
                             [point[0] + box_size, point[1], point[2], point[3]],
                             [point[0] + box_size, point[1], point[2] + box_size, point[3]],
                             [point[0] + box_size, point[1] + box_size, point[2], point[3]],
                             [point[0] + box_size, point[1] + box_size, point[2] + box_size, point[3]]], dtype = "double")

    # Generate a random rotation matrix.
    def generate_rotation_matrix(self):
        rotationAngle = radians(30)
        self.rotationMatrix = np.array([[cos(rotationAngle), 0.0, sin(rotationAngle)],
                                        [0.0, 1.0, 0.0],
                                        [-1 * sin(rotationAngle), 0.0, cos(rotationAngle)],
                                        [0.0, 0.0, 0.0]], dtype = "double")

    # Generate a random translation vector.
    def generate_translation_vector(self):
        self.translationVector = np.array([[-16.0, 0.0, 0.0, 1.0]], dtype = "double")

    # Generate a new points from translation and rotation.
    def generate_new_points(self):
        self.new_points = np.empty((0, 4), dtype = "double")
        for i in range(0, self.box.shape[0]):
            new_point = self.transformation_matrix @ np.transpose(self.box[i])
            self.new_points = np.append(self.new_points, [new_point], axis=0)
        
    # Generate a random translation vector.
    def generate_eye_vectors(self):
        point = [0.0, 10.0, 10.0, 1.0]
        box_size = 0.005
        self.eye_vectors = np.array([[point[0], point[1], point[2], point[3]],
                                     [point[0], point[1], point[2] + box_size, point[3]],
                                     [point[0], point[1] + box_size, point[2], point[3]],
                                     [point[0], point[1] + box_size, point[2] + box_size, point[3]],
                                     [point[0] + box_size, point[1], point[2], point[3]],
                                     [point[0] + box_size, point[1], point[2] + box_size, point[3]],
                                     [point[0] + box_size, point[1] + box_size, point[2], point[3]],
                                     [point[0] + box_size, point[1] + box_size, point[2] + box_size, point[3]]], dtype = "double")

    # Generate a random translation vector.
    def generate_gaze_vectors(self):
        self.gaze_vectors = np.empty((0, 4), dtype = "double")
        for i in range(0, self.box.shape[0]):
            gaze_vector = self.new_points[i] - self.eye_vectors[i]
            self.gaze_vectors = np.append(self.gaze_vectors, [gaze_vector], axis=0)
