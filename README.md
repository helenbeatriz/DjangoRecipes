# Recipe Sharing Blog
Welcome to the Recipe Sharing Blog, a platform for food enthusiasts to share and discover delicious recipes from around the world.

## Features

### Footer 
A footer has been added to the bottom of the site, containing links to social media profiles and contact information. The links have aria-labels to assist users with assistive screen reading technology, and open in new tabs to prevent users from leaving the site.
### Create Recipe Page
A page has been implemented to allow registered users to create and publish their own recipes. The page has a user-friendly form with fields for ingredients, cooking instructions, and images.
### View Recipes Page
A page has been implemented to allow users to browse through all published recipes. Users can search for recipes by keyword, cuisine, or category, and sort the results by popularity, date, or rating.
### Edit Recipe Page
Registered users can edit their own recipes from the View Recipes page. The page has a form similar to the Create Recipe page, with pre-filled fields and the ability to upload new images.
### Favicon and Error Pages:
A site-wide favicon has been added to provide an image in the browser's tab header for easy identification of the website when multiple tabs are open. A 404 error page has been implemented to redirect users to the main website if they access a broken link. A 403 error page has been created to provide feedback to users when attempting to access unauthorized content, covering pages such as Create Menu, Edit Menu, Delete Menu, Edit Booking, and Delete Booking. A 500 error page has also been implemented to alert users when an internal server error occurs.
- Base Setup, User Stories:
The following user stories were completed to set up a base structure for all HTML pages and the core installations and configurations needed to run the application, including creating the base.html page and structure for page layout reuse, creating static resources for images, CSS, and JavaScript, and setting up the project for implementing core features.
Future Feature Implementation:
In future releases, a chat and conversations with bloggers would be available. 
### Technologies Used
- HTML- CSS- JavaScript- React- Node.js- Express- Django- Python- Extensions
### InstallationTo install and run this project on your local machine, follow these steps:
- Clone the repository to your local machine.- Open a terminal window and navigate to the project directory.- Install the dependencies by running npm install.- Start the server by running npm start.- Open a web browser and navigate to http://localhost:3000.- ContributingIf you would like to contribute to this project, please follow these guidelines:
Fork the repository to your own GitHub account.- Create a new branch for your changes.- Make your changes and commit them with descriptive commit messages.- Push your changes to your forked repository.- Create a pull request to merge your changes into the main repository.Credits: This project was created by Helen Beatriz Cantu de Avila. If you have any questions or comments, please contact me at [helen_beatriz02@outlook.com]. 
LicenseThis project is licensed under the MIT License.
### Base Setup
The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first epic to be delivered as all other features depend on the completion of the base setup.
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
User StoriesThe following user stories (by epic) were completed over the 3 sprints:
### Base Setup
As a developer, I need to create the base.html page and structure so that other pages can reuse the layout
As a developer, I need to create static resources so that images, css and javascript work on the website
As a developer, I need to set up the project so that it is ready for implementing the core features
As a developer, I need to create the footer with social media links and contact information
As a developer, I need to create the navbar so that users can navigate the website from any device
### - Stand alone Pages
As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist
As a developer, I need to implement a 500 error page to alert users when an internal server error occurs
As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views
As a user, I would like to see a homepage where I can browse through the latest recipes and view featured recipes.
### Authentication 
As a user, I want to create an account so that I can save my favorite recipes and create shopping lists.
As a site owner, I want users to verify their email when registering an account so that I can ensure that a valid email address is being used.
As a site owner, I would like the login and registration pages customized to that they fit in with the sites styling.
### Recipe Management
As a user, I want to be able to search and browse through a variety of recipes so that I can discover new dishes to try.
### DeploymentVersion Control
This recipe sharing blog was developed using Visual Studio Code and version controlled using Git. The code was pushed to a remote repository named 'Gars-Steakhouse' on GitHub. The following Git commands were used to push code to the remote repo:
git add <file> - Adds the file(s) to the staging area before committing.
git commit -m “commit message” - Commits changes to the local repository queue.
git push - Pushes all committed code to the remote repository on GitHub.
### Heroku Deployment
The site was deployed to Heroku. The steps to deploy are as follows:
- Navigate to heroku and create an account- Click the new button in the top right corner- Select create new app- Enter app name- Select region and click create app- Click the resources tab and search for Heroku Postgres- Select hobby dev and continue- Go to the settings tab and then click reveal config vars- Add the following config vars: - SECRET_KEY: (Your secret key) - DATABASE_URL: (This should already exist with add on of postgres) - EMAIL_HOST_USER: (e-mail address) - EMAIL_HOST_PASS: (e-mail app password) - CLOUNDINARY_URL: (cloudinary api url)- Click the deploy tab- Scroll down to Connect to GitHub and sign in / authorize when prompted- In the search box, find the repositoy you want to deploy and click connect- Scroll down to Manual deploy and choose the main branch- Click deploy
The app should now be deployed.
# The following Python modules were used in the development of this application:
Django's class-based views (such as ListView, UpdateView, DeleteView) were used to create, read, update, and delete objects.Mixins such as LoginRequiredMixin and UserPassesTestMixin were used to enforce login requirements and ensure that only authorized users could perform certain actions.The messages module was used to display feedback messages to the user, typically in the form of toasts.The date and timedelta modules were used to search for objects based on date and date ranges.
