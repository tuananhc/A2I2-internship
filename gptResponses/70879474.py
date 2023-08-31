# To run the commands automatically every 15 minutes, you can create a Python script and use a scheduler like cron to execute it at regular intervals. Here's how you can do it:

# 1. Create a new Python script file. You can name it something like `inky_script.py`.

# 2. Open the file in a text editor and paste the code you provided inside it.

# 3. Save the file and exit the text editor.

# 4. Open a terminal on your Raspberry Pi.

# 5. Type the following command to open the crontab file for editing:
#    ```bash
#    crontab -e
#    ```

# 6. If prompted, choose an editor to use (e.g., nano).

# 7. Add the following line to the crontab file to schedule the script to run every 15 minutes:
#    ```bash
#    */15 * * * * python3 /path/to/inky_script.py
#    ```
#    Replace `/path/to/inky_script.py` with the actual path to your Python script file.

# 8. Save the crontab file and exit the editor.

# 9. The script will now run automatically every 15 minutes with no interaction required from you.

# Make sure you have the necessary Python modules installed by running:
# ```bash
# pip3 install Pillow inky
# ```

# Note: Make sure the Python script file has the executable permission set. You can use the following command to give it execute permissions:
# ```bash
# chmod +x /path/to/inky_script.py
# ```

# That's it! Your script will now run on schedule, displaying the specified image on your InkyWHAT display.