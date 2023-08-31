# To upload both the files and the email address in the same request using Flask, you can modify your code as follows:

# On the client side, you can use the `data` parameter in the `post` method to include the email address as a separate field in the request:

# ```python
import requests

test_files = {
    ('dicom', open("Pre_1", "rb")),
    ('dicom', open("Pre_2", "rb")),
    ('dicom', open("Post_1", "rb")),
    ('dicom', open("Post_2", "rb"))
}

data = {
    "email": "RecipientEmail@gmail.com"
}

response = requests.post("MyWebsite.com", files=test_files, data=data)
# ```

# On the server side, you can access the email address in the same way you access the uploaded files using `request.form['email']`:

# ```python
@app.route("/upload", methods=["POST"])
def upload():
    email = flask.request.form["email"]
    uploaded_files = flask.request.files.getlist("dicom")
    print(uploaded_files, email, file=sys.stderr)
    for file in uploaded_files:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # Rest of your code to process the images
# ```

# This way, you can send the email address along with the files in the same POST request and access it on the server side.