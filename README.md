# product: ROADMAP

**Version 1.0.0**

Final Project for CS50x 2020

| Title            | Author                |    Year   |    City     |      State      |        Country      |
| ---------------- | :-------------------: | :-------: | :---------: | :-------------: | :-----------------: |
| product: ROADMAP | Wesley  |    2020   |   |    |       |


The application allows users to keep track of projects and project entities that are in the development pipeline. Each project entity's development time can be to estimated and kept track of, while providing a granular look through into each To Do item depending on what level of detail is required by the user at that time:


* Selected Product ------------------ provides a place to view and switch between distinct products
* Product > 'Categories' ------------ provides a view of all Categories associated with the selected Product
* Selected Category > 'Projects' ---- provides a view of Projects associated with a particular Category
* Selected Project > 'Stories' ------ provides a view of Stories associated with a particular Project


Future Iteration TO DOs:

* Selected Story > 'Tasks' ----------------------------- will provide a view of Tasks associated with a particular Story  
* Selected Task > 'Sub-Tasks' -------------------------- and finally, this will show any Sub-Tasks associated with a particular Task

* Organize Project Lists with Ranking


The inspiration behind this project was to build a project/product management utility that will allow me to manage projects that help expand my CS knowledge, manage ongoing projects I have, and really use this product to enhance this particular application itself. My personal use case is that I utilize this application to manage this project's own development requirements and evolve it over time.

[Youtube Link](https://youtu.be/4PTz1-XBs6c)

---

Usage Instructions
==================
### You will need the following technologies installed (links provided within 'Other Information')
* Python
* Flask
* Flask-SQLAlchemy

### Within your Terminal
- Navigate to the Parent folder where the application was downloaded to
- Set your FLASK_APP environment to the application.py file.
$ export FLASK_APP=application.py

### Using Flask to run the live server via your Terminal
- $ flask run
- visit the URL
- You will be brought to the Home Page

### Application Navigation:
- Clicking on 'Home' in the main Navigation Bar will  bring you to a page view of All active Categories for your given Product
- Clicking on 'About' in the main Navigation Bar will bring you to the About page
- Clicking on the 'Categories' within the Sidebar will bring you to a 'Project Page' displaying all Projects associated with that particular Category
- Clicking into any of the Project Links will bring you to a 'Stories page' displaying all Stories associated with that particular Project

### Functionality
#### Add To Do list items by clicking on the 'Add' buttons
Within each table screen you will find a Form to 'Add' new entities to a particular list which. Data is stored in a SQL database file.

Home tab: You will find a 'Add Category' button and a field to 'enter a new category'.
- This will add new Categories to the Sidebar

Category Tabs: You will find a 'Add Project' button which takes inputs for the 'Project Name' and 'T-Shirt Size'
- This will add new Projects to the particular Category you are currently in

Project Links: You will find 'Add Story' buttons which take input for 'Story Name' and 'T-Shirt Size'
- This will add new Stories to the particular Project you are currently in

#### Update list items
Within each Project Table you will find an 'Action' column.
- Click on 'Edit' and you will be redirected to the Update page
- Here you can change a project's
- - 'Name'
- - 'T-Shirt Sizing' to estimate the time it will take to complete
- - 'Status' to mark if the project is 'To Do', 'In Progress', or 'Complete'
- - 'Parent ID' to change the parent entity for which the item is associated with

>Updates are currently only available for 'projects'

#### Delete list items
Click on 'Delete' within the 'Action' column to Delete an item
>Currently only available for 'Projects' and 'Stories'

---

Other Information
================
### Initial Commit to GitHub as of 12/31/2020
- Navigation controls
- Sidebar controls
- SQL Database integrated - read, update, delete records
- Item linking
- Category Look through
- Project Look through
- Story Look through

### Technologies used
- [Python 3.8.5](https://pypi.org)
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/#user-s-guide)
- [Jinja2](https://jinja2docs.readthedocs.io/en/stable/intro.html#installation)
- [Werkzeug 1.0.1](https://werkzeug.palletsprojects.com/en/1.0.x/)
- [HTML5](https://html.com/html5/)
- [CSS](https://www.w3.org/TR/CSS/#css)
- [Bootstrap v4.5.0](https://getbootstrap.com/)
- [SQLite v3.33.0](https://sqlite.org/index.html)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [Markdown](https://www.markdownguide.org)

### Sources
- [W3Schools](https://www.w3schools.com) for help with HTML, CSS and SQL
- Jinja & Flask-SQLAlchemy Documentation, and additional Code adapted from:
-- <iframe width="560" height="315" src="https://www.youtube.com/embed/hbDRTZarMUw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
- Sidebar CSS adapted from:  
-- <iframe width="560" height="315" src="https://www.youtube.com/embed/M-pil5oHw0w" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
