# Yes, you can achieve this by using the `app.context_processor` decorator provided by Flask. This decorator allows you to define a function that adds context variables to the template context for every request.

# Here's an example of how you can set a global variable using `app.context_processor`:

# ```python
@app.context_processor
def inject_global_variables():
    def get_value():
        return 'your_value'

    return dict(value=get_value)
# ```

# In this example, the `inject_global_variables` function is decorated with `app.context_processor`. Inside this function, you define a nested function `get_value` that returns the desired value. This nested function is then added to the template context as the `value` variable.

# Now, in your route functions, you can omit passing the `value` variable explicitly to `render_template()`:

# ```python
@app.route('/hello')
def hello(name=None):
    return render_template('hello.html')

@app.route('/bye')
def bye(name=None):
    return render_template('bye.html')
# ```

# Both the `hello.html` and `bye.html` templates will have access to the `value` variable via the global context.

# Note that the `app.context_processor` function runs for every request, so the value can be dynamic if needed.