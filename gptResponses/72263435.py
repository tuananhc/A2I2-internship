# To delete all but the coordinates returned by the face-recognition function, you can modify the code as follows:

# ```python
import face_recognition

image1 = face_recognition.load_image_file("image extract/image.jpg")
face_locations = face_recognition.face_locations(image1)
print(face_locations)

# Store the coordinates returned by the face-recognition function
coordinates = face_locations

# Create a new list to contain only the coordinates
filtered_coordinates = []

# Iterate through the original coordinates list and add any non-empty coordinates to the filtered list
for location in coordinates:
    if location:
        filtered_coordinates.append(location)

# Print the filtered coordinates list
print(filtered_coordinates)
# ```

# In this code, after obtaining the face coordinates using the `face_recognition.face_locations()` function, the coordinates are stored in the `coordinates` variable. Then, a new list called `filtered_coordinates` is created to hold the filtered coordinates. Finally, a loop iterates through the original coordinates and adds any non-empty coordinates to the filtered list. The resulting filtered coordinates are then printed.