# hro_burned_imx
Script to query imx API and return results in JSON of burned assets.  Can modify line 36 to filter mint#

To run the Python code from the command line on a Windows machine, follow these steps:

Install Python: If you haven't already, download and install the latest version of Python from the official website: https://www.python.org/downloads/

Add Python to PATH: During the installation process, make sure to check the box that says "Add Python to PATH" or "Add Python to environment variables". This allows you to run Python directly from the command prompt.
Install the requests library: Open the Command Prompt (press Win + R, type cmd, and hit Enter). Type the following command and hit Enter to install the requests library:

Copy code
pip install requests
Save the code: Open your preferred text editor, paste the Python code provided in the previous response, and save the file with a .py extension, such as fetch_assets.py.

Run the code: Open the Command Prompt and navigate to the folder where you saved the Python script using the cd command. For example, if you saved the file in the C:\Users\YourUsername\Documents folder, type:

bash
Copy code
cd C:\Users\YourUsername\Documents
Replace "YourUsername" with your actual username.

Execute the script: Finally, run the script by typing the following command and hitting Enter:
Copy code
python fetch_assets.py
The script will execute, and you should see the filtered results in the Command Prompt.

If you encounter any issues or errors, make sure you have installed Python correctly and have the necessary libraries installed.


You can paste the JSON results into a viewer:
https://data.page/json/csv


You can modify line 49 handle filtering of min #.  Currently its set to search for all mints under 100. "if mint_number < 100:"
