# ytdownload
Terminal Youtube Downloader using YT-DLP
# IMPORTANT
1. This Script is Disigned for linux use, I Have no idea if it will work on windows or not. If you would like to make a pull request to add windows support I will accept  
2. If you Dont set your variables inside of config.yml It <ins>WILL NOT WORK</ins>
## Setup
    git clone https://github.com/KalebSchmidlkofer/ytdownload.git
#### Its best practice to create a virtual enviorment
    python -m venv .venv
    
For Linux: 
    
    source venv/bin/activate

for Windows: 
    
    .venv\scripts\activate.bat

Then You need to install the requirements from the requirements.txt file.
    
    pip install -r requirements.txt
    
### Usage
### WIP
In order to use the links you must do :

    python main.py audio -l "https://www.youtube.com/watch?v=dQw4w9WgXcQ&" or -yt 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&'

For Video it's the same thing just 

    python main.py video

if you dont and instead run this:

    python main.py audio -l https://www.youtube.com/watch?v=dQw4w9WgXcQ&

you will get an error like this:

    no matches found: https://www.youtube.com/watch?v=dQw4w9WgXcQ

