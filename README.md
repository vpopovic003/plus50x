# Plus50x
#### Video Demo: https://www.youtube.com/watch?v=tWOz693ZLHE
#### Description:

Plus50x is a redesign page for CS50's Introduction to Computer Science by Harvard. The main idea behind the project was to have an intuitive learning experinece. Our goal was to get more attention to the shorts, notes and other features of the lecture, which are very imporant for the complete experience. 

This page was done in response to the official CS50x web page (https://cs50.harvard.edu/x/2022/), and similarities in design were intentional.

#### URL: https://plus50x.herokuapp.com/

## Technologies used

The main application is written in Flask. Database is sqlite3. All other web elements are written in standard HTML, CSS and JavaScript.

## Current Features

- Access all lessons, shorts, notes, transcripts, source files and problem sets.
- Register/Login to track your course progress on the Progress page
- Access your grades via external link
- Switch between light/dark theme

#### Lessons:
Access each week by clicking on the left side menu, or on the landing page. Use drop down menus to access different parts of the week's lesson.

#### Register/Login:
Use username/password to create account to be able to track your progrees on the Progress page. All videos (both lecture and shorts) will be automatically detected and checked if played. For labs and problem sets you will have to check them manually.

#### Grades:
If you click grades it will take you to an external link cs50.me/cs50x.

#### Settings:
Choose between light and dark theme. This will be stored in a cookie, and the page will remember your choice.
  
#### Cookies:
The page asks for your permission to save cookies. If activated the Darkmode will be activated each time you open the page, if not you will have to do it manually.

## Developer Notes:

layout.html: This html page loads the main layout for every page. It contains the dropdown menu, the side menu and the burger menu on smaller screens. The code for the burger menu is written in JavaScript, and all other components are completely in CSS, without any JavaScript.

main.html: The main landing page, with relatively simple design.

start.css: The main css file for the overall design of this page. Switches layout to handle different screen sizes and triggers burger menu that will appear in the top left corner of the screen.

lecture.html: The main page for each week. On bigger devices shows video of the selected lecture directly. On smaller screens you need to click on the video link.

admin.html: The Admins can see the traffic of the Website and how many users visited it on that day and in the past.

progress.html: The progress of each short and video are checked if the video has been played. You need to be logged in for that function. If you click an checkbox on the page it will update the db and it will be saved automatically.


## Authors
- [@keen003](https://github.com/keen003)
- [@CJason14](https://github.com/CJason14)
