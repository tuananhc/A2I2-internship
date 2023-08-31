Here are some unit test cases for the 'myFunc' function:

1. Test case for an image with no faces:
```
def test_myFunc_no_faces(self):
    # Create an image with no faces
    image = load_image_file("path/to/no_faces.jpg")

    # Call the function
    result = myFunc(image)

    # Verify the result is an empty list
    self.assertListEqual(result, [])
```

2. Test case for an image with one face:
```
def test_myFunc_one_face(self):
    # Create an image with one face
    image = load_image_file("path/to/one_face.jpg")

    # Call the function
    result = myFunc(image)

    # Verify the result contains one set of coordinates
    self.assertEqual(len(result), 1)
    self.assertIsInstance(result[0], tuple)
    self.assertEqual(len(result[0]), 4)  # Assuming the coordinates are (top, right, bottom, left)
```

3. Test case for an image with multiple faces:
```
def test_myFunc_multiple_faces(self):
    # Create an image with multiple faces
    image = load_image_file("path/to/multiple_faces.jpg")

    # Call the function
    result = myFunc(image)

    # Verify the result contains the same number of coordinates as the detected faces
    face_locations = face_recognition.face_locations(image)
    self.assertEqual(len(result), len(face_locations))

    # Verify each set of coordinates in the result is valid
    for coordinates in result:
        self.assertIsInstance(coordinates, tuple)
        self.assertEqual(len(coordinates), 4)  # Assuming the coordinates are (top, right, bottom, left)
```

4. Test case for invalid input (not an image):
```
def test_myFunc_invalid_input(self):
    # Create an invalid input (not an image)
    invalid_input = "not an image"

    # Call the function
    with self.assertRaises(InvalidImageError):
        myFunc(invalid_input)
```

Feel free to adjust the test cases according to your specific requirements and assumptions.