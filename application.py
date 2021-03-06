from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import or_, and_
from datetime import date

# Config your environment
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///roadmap.db'

# Initialize the Database
db = SQLAlchemy(app)

# Reflect your Database using automap base from sqlalchemy.ext.automap
Base = automap_base()
Base.prepare(db.engine, reflect=True)


Categories = Base.classes.categories
Projects = Base.classes.projects
Stories = Base.classes.stories


# removes caching so that you don't struggle with stubborn browsers
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# INDEX PATH
@app.route("/", methods=["GET", "POST"])
def load_categories():

    # Load Categories into main index HTML page
    # table_active = request.form["selected"]
    table = "categories"

    if request.method == "POST":

        product = "Product Roadmap"
        today = date.today()

        # request the category name from the HTML form
        category = request.form.get("category")

        # INSERT new categories to the category table
        # add the category to the category() database which, right now, is a class
        new_category = Categories(category=category, product=product, date=today)

        try:
            db.session.add(new_category)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an error adding your New Category"

            # used to be: db.execute("INSERT INTO :table (category, date, product) VALUES (:category, :date, :product)", table=table, category=category, date=today, product=product)

    else:
        # Query is the source of all SELECT statements generated by the ORM
        return render_template("index.html")


# PROJECT PAGE
@app.route("/project/<int:parent_id>", methods=["GET", "POST"])
def load_project(parent_id):
    # Source for Passing variables into applicaiton.py from HTML pages: https://stackoverflow.com/questions/49683892/pass-a-value-from-html-link-to-my-function-in-flask

    # Use active table for reading/writing

    table = "projects"

    # Set path for POST (not GET)
    if request.method == "POST":
        # INSERT into the table the entered value

        # Request items user entered within HTML Form
        project = request.form.get("project")
        tshirtsize = request.form.get("tshirtsize")

        new_project = Projects(project=project, tshirtsize=tshirtsize, categoryid=parent_id)

        try:
            db.session.add(new_project)
            db.session.commit()
            return redirect(f"/project/{parent_id}")
        except:
            return "There was an error adding the Project"

    # Set path for GET
    else:
        # Get Items from Parent Category selected
        projects_inprog = db.session.query(Projects.project, Projects.projectid, Projects.tshirtsize, Projects.categoryid, Projects.status).filter(and_(Projects.categoryid == parent_id, and_(Projects.status != 'Done', Projects.status != 'To Do')))

        projects_todo = db.session.query(Projects.project, Projects.projectid, Projects.tshirtsize, Projects.categoryid, Projects.status).filter(Projects.categoryid == parent_id, and_(Projects.status != 'Done', Projects.status != 'In Progress'))

        projects_done = db.session.query(Projects.project, Projects.projectid, Projects.tshirtsize, Projects.categoryid, Projects.status).filter(Projects.categoryid == parent_id, and_(Projects.status != 'In Progress', Projects.status != 'To Do'))


        # Get your Total T Shirt Sizing of your Project
        totalSize = 0
        for row in projects_todo:
            tshirtsize = int(row.tshirtsize)
            totalSize += tshirtsize

        category_name = db.session.query(Categories).get(parent_id)

        # Render the HTML page
        return render_template("projects.html", category_name=category_name.category, projects_todo=projects_todo, projects_done=projects_done, projects_inprog=projects_inprog, categoryid=parent_id, totalSize=totalSize)


@app.route("/stories/<int:project_id>", methods=["GET", "POST"])
def load_stories(project_id):

    # Add Stories to stories DB
    if request.method == "POST":

        story = request.form.get("story")
        tshirtsize = request.form.get("tshirtsize")
        today = date.today()

        add_story = Stories(story=story, tshirtsize=tshirtsize, date=today, projectid=project_id)

        try:
            db.session.add(add_story)
            db.session.commit()
            return redirect(f"/stories/{project_id}")
        except:
            return "There was an error creating the Story..."


    # GET path for Stories route
    else:
        stories_inprog = db.session.query(Stories.story, Stories.storyid, Stories.tshirtsize, Stories.date, Stories.projectid, Stories.status).filter(and_(Stories.projectid == project_id, and_(Stories.status != 'Done', Stories.status != 'To Do')))

        stories_todo = db.session.query(Stories.story, Stories.storyid, Stories.tshirtsize, Stories.date, Stories.projectid, Stories.status).filter(Stories.projectid == project_id, and_(Stories.status != 'Done', Stories.status != 'In Progress'))

        stories_done = db.session.query(Stories.story, Stories.storyid, Stories.tshirtsize, Stories.date, Stories.projectid, Stories.status).filter(Stories.projectid == project_id, and_(Stories.status != 'In Progress', Stories.status != 'To Do'))


        # Get your Total T Shirt Sizing of your Project
        totalSize = 0
        for row in stories_todo:
            tshirtsize = int(row.tshirtsize)
            totalSize += tshirtsize

        project_name = db.session.query(Projects).get(project_id)

        return render_template("stories.html", project_name=project_name.project, projectid=project_id, stories_inprog=stories_inprog, stories_todo=stories_todo, stories_done=stories_done, totalSize=totalSize)


@app.route('/update/<string:project_id>', methods=["GET", "POST"])
def update(project_id):

    # Use Project ID provided by FORM in HTML to query the value you want to update
    update_project = db.session.query(Projects).get(project_id)
    # db.execute("SELECT * FROM projects WHERE projectid=:project_id", project_id=project_id)


    if request.method == "POST":
        # Get values from HTML Form
        update_project.project = request.form.get("project")
        update_project.tshirtsize = request.form.get("tshirtsize")
        update_project.categoryid = request.form.get("categoryid")
        update_project.status = request.form.get("status")
        try:
            # UPDATE the record
            db.session.commit()
            return redirect(f"/project/{update_project.categoryid}")

            # db.execute("UPDATE projects SET project=:project, tshirtsize=:tshirtsize, categoryid=:categoryid, status=:status WHERE projectid=:project_id", project=project, tshirtsize=tshirtsize, categoryid=categoryid, status=status, project_id=project_id)

        except:
            return "There was a problem updating the record..."

    else:
        update_record = update_project
        return render_template("update.html", update_record=update_record)



# Delete path, redirects back to Project Path
@app.route('/delete/<int:project_id>', methods=["GET", "POST"])
def delete(project_id):
    delete_project = db.session.query(Projects).get(project_id)

    try:
        # DELETE FROM table WHERE search_condition
        db.session.delete(delete_project)
        db.session.commit()
        # db.execute("DELETE FROM projects WHERE projectid=:project_id", project_id=project_id)

        # TODO: Get the Parent ID corresponding to this Project ID so that you land on the proper Category page!
        print("delte's cat id: ", delete_project.categoryid)
        # categoryid = db.session.query(Projects).get(delete_project.categoryid)
        print("Cat ID is: ", delete_project.categoryid)

    except:
        return "There was a problem deleting the record..."

    return redirect(f"/project/{delete_project.categoryid}")


@app.route("/about")
def load_about():
    return render_template("about.html")


@app.context_processor
def context_processor():
    # All Categories
    categories = db.session.query(Categories.category, Categories.categoryid, Categories.product, Categories.date)

    # All Projects
    projects = db.session.query(Projects.project, Projects.projectid, Projects.tshirtsize, Projects.categoryid, Projects.status)

    # All Stories
    stories = db.session.query(Stories.story, Stories.storyid, Stories.tshirtsize, Stories.date, Stories.projectid, Stories.status)

    return dict(categories=categories, projects=projects)
