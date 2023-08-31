# Yes, there is a way to run the deployed script through the Heroku server independently of the local machine. 

# To achieve this, you need to create a Heroku worker dyno instead of using the `heroku run` command. Here's how you can do it:

# 1. Create a `Procfile` in the root directory of your project.
# 2. Inside the `Procfile`, add the following line:

#     ```
#     worker: python script.py
#     ```

#     Replace `script.py` with the actual filename of your script.
  
# 3. Commit the `Procfile` to your version control system (e.g., git).

# 4. Push the changes to Heroku to deploy the worker dyno:

#     ```
#     git push heroku main
#     ```

# Heroku will now start a worker dyno running the specified script, and it will continue to run independently of your local machine or terminal. You can check the logs to verify that the script is running:

# ```
# heroku logs --tail
# ```

# Note: Make sure you have scaled your worker dyno accordingly. If you only have a web dyno running, you can scale it to zero using the following command:

# ```
# heroku ps:scale web=0
# ```

# This will free up resources for the worker dyno to run your script.