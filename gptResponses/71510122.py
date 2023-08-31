To embed images with different formats in Sphinx docs, you can use the following code snippet:

```
.. rst-class:: sphx-glr-horizontal

.. figure:: _static/diagram.jpg
   :alt: alternate text
   :width: 620px
   :height: 540px

   .. figure:: _static/diagram.avif
      :alt: alternate text
      :target: _static/diagram.jpg
      :class: sphx-glr-single-img-embed
```

Here's what each part of the code does:

- The `rst-class` directive sets the CSS class to display the images in a horizontal layout.
- The `figure` directive is used to display the main image (in JPG format). You can adjust the `width` and `height` parameters to fit your needs, and set the `alt` attribute for alternate text.
- Inside the `figure` directive, another `figure` directive is nested, this time with the AVIF image. The `alt` attribute is set for alternate text, and the `target` attribute links it to the JPG image. The `class` attribute `sphx-glr-single-img-embed` is used to hide the AVIF image when the JPG image is supported, and show only the JPG image.

By using this code, the JPG image will be served to all modern browsers, while the AVIF image will be served to browsers that support it (modern browsers).