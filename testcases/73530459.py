Here are some sample unit test cases for testing the `myFunc` function:

```python
import unittest
import numpy as np
from PIL import Image

def myFunc(images, x, y):
    pil_images = []
    for i in range(images.shape[0]):
        pil_images.append(Image.fromarray(np.uint8(images[i])).convert('RGB'))
    
    fig, ax = plt.subplots()
    for i in range(len(pil_images)):
        ab = AnnotationBbox(OffsetImage(pil_images[i]), x[i], y[i], frameon=False)
        ax.add_artist(ab)
    fig.savefig(image_path + 'funny_markers.png')
    plt.close('all')
    
    return 'success'

class MyFuncTestCase(unittest.TestCase):
    def test_images_as_markers(self):
        images = np.random.uniform(0, 1, (5, 10, 10))
        x = np.array([0, 2, -3, 6, 6.5])
        y = np.array([10, 3, -2, -1, 0.2])
        
        result = myFunc(images, x, y)
        self.assertEqual(result, 'success')

    def test_empty_images(self):
        images = np.zeros((0,))
        x = np.array([0, 2, -3])
        y = np.array([10, 3, -2])
        
        result = myFunc(images, x, y)
        self.assertEqual(result, 'success')

    def test_empty_coordinates(self):
        images = np.random.uniform(0, 1, (5, 10, 10))
        x = np.array([])
        y = np.array([])
        
        result = myFunc(images, x, y)
        self.assertEqual(result, 'success')

    def test_different_image_shape(self):
        images = np.random.uniform(0, 1, (5, 8, 8))
        x = np.array([0, 2, -3, 6, 6.5])
        y = np.array([10, 3, -2, -1, 0.2])
        
        result = myFunc(images, x, y)
        self.assertEqual(result, 'success')

if __name__ == '__main__':
    unittest.main()
```

These test cases cover scenarios such as when the images and coordinates are empty, when the image shape is different, and the general case. Running the test cases will assert that the `myFunc` function should return 'success' for each of these cases.