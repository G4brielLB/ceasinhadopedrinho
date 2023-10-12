
# Ceasa Amanhã
#### Video Demo: https://www.youtube.com/watch?v=nS1VY6izh9w
#### Description
> This project was idealized and produced by Gabriel Lopes Bastos.

This website was developed using the framework Django (3.1.6), that is based in Python. So, the backend and all the features, functionalities, math, etc. were did using Python. To do the frontend it was used JavaScript, HTML and CSS, with some tools from Bootstrap.
The main goal of the website is to allow people (usually family members) to do their markets lists, and then in the backend of the website, every market list that are did on the same day are joined into only one. This unification consists in make life simpler in the day of doing shopping on the market, instead of having a lot of lists, it would be just one.
In folder “cadastros” you have the main files for doing the registering and attachment of those lists.
> In “models.py” you have the form to do the market list, and this form is saved on the database with all the products, name, and date. After the form, the other lines of code are basically getting the information from all the forms, attaching the lists into a single list, and organizing it to send the final list to “views.py”.
> In “views.py” you have all the configured webpages around the lists. To do a new list, edit, delete, show the lists of the users and showing the final list. And in this file is used a lot of imports from the Django library, helping to create, delete, update and viewing.
> “listing.py” is basically to organize the final list and list of other users.
> In “urls.py” it is basically to make the paths to the urls. In this case, it is about editing, creating, deleting, and viewing the lists.
> Inside “cadastros”, you have another folder called “templates”, which has all the HTML files that have something related to the markets lists.
	Another folder (outside of “cadastros”) is “paginas”. Inside you have the static folder, with the static images used in the site, the javascript files and the css ones. You have the index page, the “about” page, and the “404 error” page. All of them distributed in “views.py”, “urls.py”, templates folder, mainly.
> P.S.: Outside “paginas” you have another folder called “staticfiles” that was created to implement in Heroku App, but it has the same function.
 	The folder “usuarios” has all the information and lines of code around registering, logging-in, managing passwords, etc. “Usuarios” in English means “users”, so that is it, all the files were written to manage this extremely important part of the website.
> In “forms.py” you have two forms, the user creation one, and the other is to change the password.
> In “urls.py” it has all the paths about the users, like the url path to login, logout, register a new user or changing the password.
> “views.py” is a file that connects the forms (“forms.py”), with the HTML files (inside templates folder) and the urls paths (“urls.py”).
The folder called “Projetos” is the base folder, created in the beginning by Django framework, and you have in it the files “settings.py”, that are the settings to implement the website in Heroku app, and the file “base.py” you have all the settings of the project.

That’s it! If you have any trouble, any doubt or wants to communicate with the developer, my contact is:
gabriellopesbastos@hotmail.com
