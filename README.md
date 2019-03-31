# AlexasLyrics

A Python game in which Alexas reads out lyrics of a song to you and you have to guess the song.

# Instructions
I figured out what was causing the problem! The intents in the JSON files were all okay, and so was the Python code.
The problem was that the code had a lot of imports like the AWS package and the lyric package.
To zip all our code with its packages, download this repository then do the following:
    
    1. On your system, navigate to the lambda folder in the AlexasLyrics repo and install the dependencies in a new folder called “skill_env” using the following command:
    
        ```
        pip install -r py/requirements.txt -t skill_env
        ```
        
    2. Copy the contents of the `lambda/py` folder into the `skill_env` folder. 
    
        ```
        cp -r py/* skill_env/
        ```
    
    3. Zip the contents of the `skill_env` folder. Remember to zip the **contents** of the folder and **NOT** the folder itself.
    4. On the AWS Lambda console, change the **code entry type** drop-down to **Upload a .ZIP file**, upload the zip created in the previous step and click on **Save**.
   
   
For further instructions check https://github.com/alexa/skill-sample-python-colorpicker/blob/master/instructions/2-lambda-function.md
Most popular songs from 2000 - 2019 https://chart2000.com/about.htm
