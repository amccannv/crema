from crema.generator import Generator
from crema.calibration import Calibration

generator = Generator(static_eye=True)
calibration = Calibration(generator.box, generator.eye_vectors, generator.gaze_vectors, generator.new_points, static_eye=True)
(success, rotation_matrix, translation_vector) = calibration.solve_PnP()

print("\n calc rotationMatrix")
print(rotation_matrix)
print("\n true rotationMatrix")
print(generator.rotationMatrix)
print("\n calc translationVector")
print(translation_vector)
print("\n true translationVector")
print(generator.translationVector)