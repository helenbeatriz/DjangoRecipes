# Recipe Sharing Blog
Welcome to the Recipe Sharing Blog, a platform for food enthusiasts to share and discover delicious recipes from around the world.
<img src="https://res.cloudinary.com/dvnmyhfxx/image/upload/v1681915441/mockup_khyhpr.png">

💻 [Visit live website](https://djangorecipes.herokuapp.com/)

 ## Introduction

Thank you for joining our user testing phase for the Recipe Sharing Blog. Your objective is to explore the website, perform specific tasks, and provide feedback based on your experience. Your input will help us identify any issues, usability concerns, or suggestions for improvement.

Please follow the instructions below to participate in the user testing.

## How to Participate

1. **Access the Website:**
   - Go to the live website: [Recipe Sharing Blog](https://djangorecipes.herokuapp.com/)
   - Use a modern web browser for the best experience (e.g., Chrome, Firefox, Safari).

2. **Explore the Website:**
   - Spend some time navigating through the website.
   - Try different features and pages, such as browsing recipes, adding a recipe, editing a recipe, and using the search functionality.

3. **Perform Testing Scenarios:**
   - Refer to the [Testing Scenarios](#testing-scenarios) section below to find specific tasks to complete.
   - Follow the instructions for each scenario and provide feedback on your experience.

4. **Report Issues:**
   - If you encounter any bugs, usability issues, or have suggestions for improvement, please report them as described in the [Reporting Issues](#reporting-issues) section below.

5. **Share Your Overall Impressions:**
   - After completing the testing scenarios, feel free to share your overall impressions of the website. Is there anything you particularly liked or disliked?


### Main Page Wireframe 

The main page will have a header section containing the website logo and navigation bar with links to various sections of the website (Home, Categories, Recipes, Login/Register, Contact).
Below the header, there will be a welcome section with a brief description of the website's purpose and a call-to-action button to encourage users to explore recipes.
Featured recipes can be displayed in a grid format below the welcome section, with images and titles, possibly with a "View Recipe" button.
Sections for the most popular recipes, recent categories, and recent articles can be added further down the page, each with a title and a list of items (recipes, categories, articles) with links or buttons to view more.
At the bottom of the page, you can include a footer with links to social media profiles and tips posted by users.

<img src="media /wireframecomputer.png">
<img src="media /wireframephone.png ">

### Recipes Wireframe 

The recipes page will have a header similar to the main page with the logo and navigation bar.
Below the header, there can see the recipes and description.  
The main content of the page will display a list of recipes, each in a card format.
Each recipe card will include an image, title, short description.
Users can click on a recipe card to view the full recipe details on a separate page.
Pagination or infinite scroll can be used if there are many recipes to display.
At the bottom of the page,  footer with social media links and contact information as on the main page.

<img src="media /recipewireframe.png ">

### Contact Form Wireframe

 <img src="media /contactwireframe.png">

 The contact form will be a simple web form with fields for the user to input their name, email address, subject, and message.
It will have a "Submit" button at the bottom to send the message.

### Technologies Used
- HTML
- CSS
- JavaScript
- React
- Node.js
- Express
- Django
- Python
- Bootstrap 
- Extensions

### To install and run this project on your local machine, follow these steps:

- Clone the repository to your local machine.
- Open a terminal window and navigate to the project directory.
- Install the dependencies by running npm install.- Start the server by running npm start.
- Open a web browser and navigate to http://localhost:3000.
- ContributingIf you would like to contribute to this project, please follow these guidelines:
Fork the repository to your own GitHub account.- Create a new branch for your changes.
- Make your changes and commit them with descriptive commit messages.
-  Push your changes to your forked repository.- Create a pull request to merge your changes into the main repository.
Credits: This project was created by Helen Beatriz Cantu de Avila. If you have any questions or comments, please contact me at [helen_beatriz02@outlook.com]. 
LicenseThis project is licensed under the MIT License.

### Stand alone Pages
The stand alone pages epic is for small pages that did not have enough stories to warrant their own full epics. Instead of creating epics for tiny features, these small deliverables were all added under this epic.

### Authentication Epic
The authentication epic is for all stories related to the registration, login and authorization of views. This epic provides critical functionality and value as without it users would not be able to create, save and access their favorite recipes.

### Recipe Management
The recipe management epic is for all stories that relate to creating, deleting, editing and viewing of recipes. This allows users to view recipes and for staff to manage them with a simple UI interface.
- Deployment Epic
This epic is for all stories related to deploying the app to heroku so that the site is live for users.
- Documentation
This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

## User Stories:
The following user stories were completed to set up a base structure for all HTML pages and the core installations and configurations needed to run the application, including creating the base.html page and structure for page layout reuse, creating static resources for images, CSS, and JavaScript, and setting up the project for implementing core features.
Future Feature Implementation:
In future releases, a chat and conversations with bloggers would be available. 

### Base Setup 
* As a developer, I need to create the base.html page and structure so that other pages can reuse the layout
* As a developer, I need to create static resources so that images, css and javascript work on the website
* As a developer, I need to set up the project so that it is ready for implementing the core features
* As a developer, I need to create the footer with social media links and contact information
* As a developer, I need to create the navbar so that users can navigate the website from any device.

### Stand alone Pages
* As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist
* As a developer, I need to implement a 500 error page to alert users when an internal server error occurs
* As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views
* As a user, I would like to see a homepage where I can browse through the latest recipes and view featured recipes.

### Authentication 
* As a user, I want to create an account so that I can save my favorite recipes and create shopping lists.
* As a site owner, I want users to verify their email when registering an account so that I can ensure that a valid email address is being used.
* As a site owner, I would like the login and registration pages customized to that they fit in with the sites styling.

### Recipe Management
* As a user, I want to be able to search and browse through a variety of recipes so that I can discover new dishes to try.

## Schema
* User Authentication:
The User and Session tables provide authentication functionality for the website. Users can create an account, log in, and log out of the website. Sessions are used to keep users logged in between requests.
<img src="media /diagram.png">


* Recipe Data:
The Recipe, Category, Ingredient, and Instruction tables represent the data related to recipes on the website. Recipes have a title, description, image, servings, difficulty, author, category, creation and lists of ingredients and instructions.

* User Interaction:
Users can leave tip and also add their own recipes. 

* Authorization:
The tables in the schema have different levels of authorization. For example, only authenticated users add tips or recipes. 

# The following Python modules were used in the development of this application:
Django's class-based views (such as ListView, UpdateView, DeleteView) were used to create, read, update, and delete objects.Mixins such as LoginRequiredMixin and UserPassesTestMixin were used to enforce login requirements and ensure that only authorized users could perform certain actions.The messages module was used to display feedback messages to the user, typically in the form of toasts.The date and timedelta modules were used to search for objects based on date and date ranges.

# Design
Fonts
The website uses Google Fonts with a sans-serif fallback for clear and legible body content. The main page headings use Vast Shadow with a sans-serif fallback.

### Structure
The website's structure focuses on simplicity, clarity, and easy navigation. The top of the page has a recognizable navigation bar with the website name and links to the right. It also includes a search bar, login/register buttons, and a friendly welcome message for authenticated users. On smaller screens, the menu collapses to a hamburger icon. The bottom of the page contains a footer with links to social media pages.

### The website has the following sections:

- Home page: overview of the content and aim of the website.
- Categories page: list of all published recipe categories.
- recipe detail page: related recipes listed below the category description.
- Add recipe page: for admin users to create a category.
- Edit recipe page: for admin users to edit an existing category.
- Delete recipe: for admin users to delete a selected category.
- Recipes page: list of all published recipes.
- Recipe detail page: authenticated users can like or comment on recipes.
- Add recipe page: for admin users to create a recipe.
- Edit recipe page: for admin users to edit an existing recipe.
- Delete recipe: for admin users to delete a selected recipe.
- Articles page: list of all published articles.
- Article detail page: authenticated users can like or comment on articles.
- Add article page: for admin users to create an article.
- Edit article page: for admin users to edit an existing article.
- Delete article: for admin users to delete a selected article.
- Login page: for returning users to log in by email or social provider.
- Register page: for new users to sign up by email or social provider.
- Logout page: for users to log out of the website.
- Contact page: with a contact form for users to provide feedback.
- 404 error page.

## Database
The backend is built with Python using the Django framework, and the deployed version uses a Postgres database. Two database models mimic the structure of the Postgres database and contain all the stored fields.

The following models represent the database model structure for the website:

#### User Model
- Contains information about the user and is part of the Django allauth library.
- recipe Model
- Contains fields for title, description, featured image, and recipes.
- Has a many-to-many relationship with recipes.
- Recipe Model
- Represents a specific recipe and contains general information.
- Contains fields for title, description, featured image, categories, difficulty, author, status, created date, ingredients, and instructions.
- Has a many-to-many relationship with categories.
- Contains Ingredient and Instruction as foreign keys.
- Ingredient Model
- Represents an ingredient for a specific recipe's ingredients.
- Contains fields for name, and recipe.
- Contains Recipe as a foreign key.
- Instruction Model
- Represents an instruction for a specific recipe's instructions.
- Contains fields for body and recipe.
- Contains Recipe as a foreign key.
- Comment Model (Recipe)
- Represents a comment on a specific recipe.
- Contains fields for name, email, body, created date, approved, and recipe.
- Contains Recipe as a foreign key.
- Article Model
- Represents a specific article and contains general information.
- Contains fields for title, description, featured image, author, status, created date, and last modified date.

# Features

### Logo and Navigation Bar

- The website has a logo and navigation bar that is featured on all pages.
- The navigation bar contains links to the Home page, Planner page, Exercise page, and Profile page.
- When logged in, the user's name is displayed in the navigation bar, and they have the option to view their profile or log out.
- When not logged in, the user has the option to either register or log in.
- The navigation bar is fully responsive and changes to a toggler (hamburger menu) on smaller screens.
- The navigation bar allows users to easily jump to a specific section on the website.

### Home page
- The Home page consists of a navigation bar, main body, and a footer.
- The Home page's main body includes the featured recipes section, a description of the website and what users can expect to find, the most popular recipes section, most recent categories section, most recent articles section, and a sign-up form.
- Sign up / Register
-  New users can create an account.
- Users must provide a valid username, password, and password confirmation.
- Users cannot register the same details twice for an account.
- Once registered, users are immediately logged in and taken to the Home page.

<img src="https://res.cloudinary.com/dvnmyhfxx/image/upload/v1681906921/8xNRAKWyXzbSdvi_smajdt.png">

### Login
- Returning users can log in to their account.
- The user must have an account in the system and enter the correct username and password.
- Users can log in to their account with Google and Facebook social sign-on.
- Both fields are mandatory.
- Once logged in, the user will be navigated to the Planner page.
- Users who are logged in as admins can see the option to add recipes and also tips.
- Users who are logged in as admins can see the option to edit or delete a recipe under the general category information.
- Logged-in users and unauthenticated users will not have the ability to edit or delete categories and will not see this section of the page.
- Visitors to this page will see the featured image, a recipe description where applicable, and the related recipes listed below in card format.
- Logged-in admin users have the ability to add recipe categories.
- Admin users will add a name, description, featured image.
- For easier use on small screen devices, the form increases to full screen width.
- Users are provided with a feedback message that their recipe has been added.

<img src="https://res.cloudinary.com/dvnmyhfxx/image/upload/v1681907918/login_sibmnj.png">

### Logout
- Confirmation screen for logged-in users to log out from their account.
- There are two views depending on whether a user is logged in or not.

<img src="https://res.cloudinary.com/dvnmyhfxx/image/upload/v1681908712/signout_qwfyy9.png">


### Edit recipe page
- Admin users can edit the information of any recipe.
- The Edit recipe page is based on the Add Category page.
- Fields are prepopulated with the information from the selected recipe.
<img src="https://res.cloudinary.com/dvnmyhfxx/image/upload/v1681911974/recipe_tpq9qw.png">



### Footer 
A footer has been added to the bottom of the site, containing links to social media profiles and contact information. The links have aria-labels to assist users with assistive screen reading technology, and open in new tabs to prevent users from leaving the site.

### Create Recipe Page
A page has been implemented to allow registered users to create and publish their own recipes. The page has a user-friendly form with fields for ingredients, cooking instructions, and images.

### View Recipes Page
A page has been implemented to allow users to browse through all published recipes. Users can search for recipes by keyword, cuisine, or category, and sort the results by popularity, date, or rating.

### Favicon and Error Pages:
A site-wide favicon has been added to provide an image in the browser's tab header for easy identification of the website when multiple tabs are open. A 404 error page has been implemented to redirect users to the main website if they access a broken link. A 403 error page has been created to provide feedback to users when attempting to access unauthorized content, covering pages such as Create Menu, Edit Menu, Delete Menu, Edit Booking, and Delete Booking. A 500 error page has also been implemented to alert users when an internal server error occurs.

### Contact Form
- User are able to get in touch with the admin of the page and the message in sent to a database. 

<img src="https://res.cloudinary.com/dvnmyhfxx/image/upload/v1681908107/contactus_hrrpfc.png">

### Base Setup
The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the completion of the base setup.

## Testing Scenarios

**Log in to Admin Panel**:

    - Access the admin panel by going to [http://localhost:8000/admin](http://localhost:8000/admin).
    - Log in using the superuser credentials you created earlier.
    - You should be able to access the Django admin panel and manage recipes and other data.

### Scenario 1: User Registration

1. Click on the "Register" button in the navigation bar.
2. Complete the registration form by providing a valid username, password, and email address.
3. Confirm your registration and log in.
4. A message saying that you are logged in is going to show up.

### Scenario 2: Browsing Recipes

1. Navigate to the "Recipes" page.
2. Use the search functionality to find a recipe by keyword.
3. Browse through the list of recipes and click on one to view its details.
4. When you click on view you will be able to see recipe, ingredients, image. 


### Scenario 3: Adding a Recipe

1. Log in to your account (if not already logged in).
2. Navigate to the "Add Recipe" page.
3. Fill out the recipe details, including title, ingredients, instructions, and an image.
4. Submit the new recipe.
5. A message saying that you submitted the recipe is going to show up.


### Scenario 4: Editing a Recipe

1. Log in to your account (if not already logged in).
2. Navigate to the "Recipes" page.
3. Find a recipe you added previously and click on it.
4. Click the "Edit" button.
5. Make changes to the recipe details and save.
6. A message saying that you edited the recipe is going to show up.


### Scenario 5: Contacting Support

1. Navigate to the "Contact" page.
2. Use the contact form to send a message to the site admin.
3. Provide feedback on the contact form's usability and clarity.
4. A page saying that the message was sent is going to show up.

## Reporting Issues

To report any issues, usability concerns, or suggestions for improvement, please follow these steps:

1. Contact us, fill the form and click on "Submit" button. 
2. Get in touch with us. 

We appreciate your contributions to improving our website!

## Contact Information

If you have any urgent questions or need assistance during the user testing phase, please feel free to contact Helen Beatriz Cantu de Avila at [helen_beatriz02@outlook.com].

Thank you for participating in the Recipe Sharing Blog user testing!

## Deployment

### Deployment Version Control
This recipe sharing blog was developed using Visual Studio Code and version controlled using Git. The code was pushed to a remote repository named 'Gars-Steakhouse' on GitHub. The following Git commands were used to push code to the remote repo:
git add <file> - Adds the file(s) to the staging area before committing.
git commit -m “commit message” - Commits changes to the local repository queue.
git push - Pushes all committed code to the remote repository on GitHub.

### Heroku Deployment
The site was deployed to Heroku. The steps to deploy are as follows:
- Navigate to heroku and create an account- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars: 
- SECRET_KEY: (Your secret key) 
- DATABASE_URL: (This should already exist with add on of postgres) 
- EMAIL_HOST_USER: (e-mail address) 
- EMAIL_HOST_PASS: (e-mail app password) 
- CLOUNDINARY_URL: (cloudinary api url)- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch- Click deploy
The app should now be deployed.

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open commandline interface on your computer
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard 
  ```
  $ git clone <website link > 
  ```
7. Press Enter to create your local clone

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python 3.8.11
- Django 3.2.16


**External Python Modules**

- asgiref==3.6.0
- cloudinary==1.32.0
- dj-database-url==1.2.0
- dj3-cloudinary-storage==0.0.6
- Django==3.2.18
- django-allauth==0.52.0
- django-cloudinary-storage==0.3.0
- django-crispy-forms==1.14.0
- django-resized==1.0.2
- django-richtextfield==1.6.1
- django-summernote==0.8.20.0
- gunicorn==20.1.0
- migrate==0.3.8
- numpy==1.24.2
- oauthlib==3.2.2
- Pillow==9.4.0
- psycopg2==2.9.5
- PyJWT==2.6.0
- python3-openid==3.2.0
- pytz==2022.7.1
- requests-oauthlib==1.3.1
- sqlparse==0.4.3

### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/) was used to create the multi-device mock-up at the top of this README.md file
- [Balsamiq](https://balsamiq.com/) to create the projects wireframes
- [Bootstrap v5.2.3](https://getbootstrap.com/). This project uses the Bootstrap library for UI components (Buttons, Card, Footer, Modal, Pagination, Navbar)
- [Cloudinary](https://cloudinary.com/) to store static files
- [Dbdiagram.io](https://dbdiagram.io/home) used for the database schema diagram
- [Favicon.io](https://favicon.io) for making the site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Font Awesome](https://fontawesome.com/) - Icons from Font Awesome were used throughout the site
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Fonts](https://fonts.google.com/)
- [Heroku](https://heroku.com) was used to deploy the project into live environment
- [jQuery](https://jquery.com) was used for drop-down exercises filters on smaller screens
- [Elephant SQL](https://www.elephantsql.com/) – deployed project on Heroku uses an Elephant SQL database
- [Summernote](https://summernote.org/) - editor used for exercise description field in Admin page
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/) - code editor used to write this project
- Validation:
- [WC3 Validator](https://validator.w3.org/) was used to validate the html in the project
- [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/) to validate the css in the project
- [JShint](https://jshint.com/) for JavaScript quality
- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) for performance, accessibility, progressive web apps, SEO analysis of the project code
- [Wave Validator](https://wave.webaim.org/) to evaluate accessibility


## Credits

### Images

**Images used in this app were found on Pexels and other websites. I'm not able to list all but I'm not the author of any of the pics.**

### Code
I developed my website based on plenty of tutorials and also on the blog included in the course. 
- Youtube Tutorial [tutorial] (https://www.youtube.com/playlist?list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)
- Django all-auth [documentation](https://django-allauth.readthedocs.io/en/latest/index.html)
- Django inline formsets [tutorial](https://www.letscodemore.com/blog/django-inline-formset-factory-with-examples/)

### Acknowledgements
I want to express my gratitude towards all those who helped me in the creation of this project. Specifically, I would like to thank my mentor Daisy, for providing me with valuable feedback and professional guidance throughout the development process.


