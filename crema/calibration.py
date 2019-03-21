import cv2 as cv
import numpy as np

# Calibrate camera systems through different implemented methods.
class Calibration:
    def __init__(self, model_points, eye_vectors, gaze_vectors, new_points, static_eye=False):
        self.static_eye = static_eye
        self.model_points = model_points
        self.eye_vectors = eye_vectors
        self.gaze_vectors = gaze_vectors
        self.new_points = new_points
        self.find_image_points()

    def find_image_points(self):
        self.image_points = np.empty((0, 2), dtype = "double")
        for i in range(0, self.model_points.shape[0]):
            depth = np.linalg.norm(self.model_points[i, 0:3], ord = 2)
            if self.static_eye:
                true_point = self.gaze_vectors[i, 0:3]
            else:
                true_point = self.eye_vectors[i, 0:3] + self.normalize(self.gaze_vectors[i, 0:3]) * depth
            self.image_points = np.append(self.image_points, [self.find_projection_point(true_point)], axis=0)

    # Calibrate cameras through PnP.
    def solve_PnP(self):
        (success, rotation_vector, translation_vector) = cv.solvePnP(np.ascontiguousarray(self.model_points[:, 0:3].reshape((8, 1, 3)), dtype= "double"), np.ascontiguousarray(self.image_points[:, 0:2].reshape((8, 1, 2)), dtype="double"), np.eye(3), np.zeros((4,1)), flags=cv.SOLVEPNP_ITERATIVE)
        rotation_matrix = np.empty((3, 3), dtype = "double")
        rotation_matrix, _ = cv.Rodrigues(rotation_vector)
        if self.static_eye:
            translation_vector = translation_vector.T + np.mean(self.eye_vectors, axis=0)[:3]
        return [success, rotation_matrix, translation_vector]

    def find_projection_point(self, true_point):
        return (true_point / true_point[2])[:2]

    def normalize(self, v):
        norm = np.linalg.norm(v, ord = 2)
        if norm == 0:
            norm = np.finfo(v.dtype).eps
        return v / norm