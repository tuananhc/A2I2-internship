import unittest

class TestSphinxDocs(unittest.TestCase):
    def test_image_format(self):
        # Mock input
        input_html = '<p>I have found the following question:\n<a href="https://stackoverflow.com/questions/25866102/how-do-we-embed-images-in-sphinx-docs">How do we embed images in sphinx docs?</a></p>\n<p>However this image tag assumes the file is in jpg or png:</p>\n<pre><code>.. image:: picture.jpg\n   :width: 200px\n   :height: 100px\n   :scale: 50 %\n   :alt: alternate text\n   :align: right\n</code></pre>\n<p>The issue with that is that jpg and png are not modern formats (also creates a bad speed index in Lighthouse/Google PageSpeed Insights: <a href="https://i.stack.imgur.com/Fe3dP.png" rel="nofollow noreferrer"><img src="https://i.stack.imgur.com/Fe3dP.png" alt="enter image description here" /></a>). I would like to use a html </p>\n<pre><code>&lt;picture&gt;\n   &lt;source srcset=&quot;diagram.avif&quot; type=&quot;image/avif&quot;&gt;\n   &lt;img src=&quot;diagram.jpg&quot; width=&quot;620&quot; height=&quot;540&quot;&gt;\n&lt;/picture&gt;\n</code></pre>\n<p>This will serve the way smaller image to all modern browsers, but will serve the png to browsers which don\'t support avif (e.g. IE). How can you do that in sphinx docs / RST?</p>'
        
        # Expected output
        expected_output = '<pre><code>&lt;picture&gt;\n   &lt;source srcset=&quot;diagram.avif&quot; type=&quot;image/avif&quot;&gt;\n   &lt;img src=&quot;diagram.jpg&quot; width=&quot;620&quot; height=&quot;540&quot;&gt;\n&lt;/picture&gt;\n</code></pre>'
        
        # Call the function to be tested
        result = myFunc(input_html)
        
        # Compare the result with expected output
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()