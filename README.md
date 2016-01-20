# Mediasite-Closed-Caption-Recorder
Python script to capture the closed captions used on a Mediasite lecture into a text file

## But... why?
Many online classes at UF use Mediasite for lectures. Taking detailed notes during the lecture is difficult as quiz questions generally 
pertain to a specific piece of information offered during the lecture that you may have missed. With this script, you will have a text
file for the entire lecture and will never need to rewatch the lecture trying to find one small piece of information! :D

## Requirements
  - python 2.7+  (*Not yet tested in python 3+*)
  - [Selenium for python] (http://selenium-python.readthedocs.org/)
    - I recommend using [Python PIP] (https://pip.pypa.io/en/stable/installing/) for installing of the selenium package
  - Firefox web browser 
  - Text file named `urls.txt` with the list of video urls (*See included `urls.txt` file for example*)
  - Empty file named `closed_captions.txt` (**Included**)
  
## How to use
  - Clone and cd into Mediasite-Closed-Caption-Recorder
  - Run `python closed_caption_recorder.py` in terminal
  - Go grab some coffee while videos play
  - The script will print the lecture notes to the terminal during the video. This is so that you know the script is accurately capturing
    the closed captions.

## How it works
Using the Selenium package, python opens each link one by one from the urls.txt file into a new browser. Selenium then clicks the CC button
and the speed button 3x to push the video to the fastest speed. The closed captions that apear on screen are recorded and after the video
finishes (current video time = duration of video), the text is appended to the closed_captions.txt file
