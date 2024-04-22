
# Company Information Storing

## Introduction

Welcome to Company Information Storing! This project helps you keep track of details about different companies, like their names, addresses, and contact information.

## Features

- **Company Management**: Add, edit, and remove company records.
- **Data Organization**: Sort companies by industry or location.
- **Search Functionality**: Easily find specific companies using search filters.
- **User Authentication**: Keep your data safe with login credentials.

## Technical Details

### What We Used

- **Frontend**: Basic web design using HTML, CSS, and Bootstrap for styling.
- **Backend**: Python with Django framework for handling data and requests.
- **Database**: SQLite3 to store company information.
- **Development Environment**: We used PyCharm IDE for coding.

  ### In summary, the MVC/MVT pattern in Django works as follows:


**Model (M)**: Defines the data structure and interacts with the database.

- **webapp/models.py** - in this python file we create django.db models like Company_Details.

**View (V)**: Processes requests, retrieves data from models, and passes it to templates for rendering.

- **webapp/views.py** - companyModelView, edit_Company and delete_Company.

**Template (T) /Controllers(C)**: **webapp/Urls.py** - Renders HTML pages, incorporating dynamic content provided by views.


### Installation

1. **Clone the Project**: Copy the project to your computer using `git clone`.
2. **Install Dependencies**: Use `pip install -r requirements.txt` to get what you need.
3. **Run Migrations**: Set up the database with `python manage.py migrate`.
4. **Start the Server**: Run `python manage.py runserver` to see the project in action.

### How to Use

- **Admin Panel**: You can manage company records here: http://localhost:8000/admin
  - Username: admin
  - Password: admin

- Use the website to add, edit, or view company information.



---

This version simplifies the explanation of the project, its features, technical details, and how to use it. Feel free to adjust it further to suit your needs.
