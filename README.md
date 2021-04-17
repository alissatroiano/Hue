# Hue

This full-stack application was developed for Hue, a digital design agency. The main purpose of Hue's website is to display and sell digital art & services to shoppers. Hue is a fictional company that was created for the purpose of this project.

As the Milestone 4 Project for [Code Institute's](https://codeinstitute.net) [Full Stack Software Development Diploma Program](https://codeinstitute.net/full-stack-software-development-diploma/), Hue was built with HTML, CSS, Bootstrap 5, JavaScript, Python 3, and Django.

## UX

### Summary

The main goal of Hue is to boost revenue by selling products online. Hue also wishes to provide their target market, comprised of male & female shoppers (ages 25-39), with an intuitive, responsive platform where they can preview & purchase digital design products.

### Research & Planning

#### Users

##### Database Design
During the research & planning phase of this milestone project the developer completed the below flowchart activity, titled "Django Multiple User Types". This activity was conducted to determine how to properly build and implement the django user model.

![Django Multiple User Types](wireframes/djangomultipleusertypes.png)
[djangomultipleusertypes](wireframes/djangomultipleusertypes.pdf)

As can be seen in the image above, the activty led the developer to make the following conclusions:

- Hue's user authentication model should define a one-to-one relationship, using the [``OneToOneField``](https://docs.djangoproject.com/en/3.1/topics/db/examples/one_to_one/).

- Hue should be built for **two** different types of users:

  1) The Site Owner
    - Hue, the company, that wants to:
        - Sell digital artwork.

    2) The Shopper
    - Digital art buyers that want to:
        - Purchase digital artwork from Hue online.   

### User Stories

User stories were created by the [developer](https://www.github.com/alissatroiano) during the planning phase of this project. As practiced in agile development, each user story coincides with a feature of the Hue application and will be accomplished in one sprint.

#### The following user stories were created for the **shopper**:

![Shopper](wireframes/userstories-shopper.png)

![Site Owner](wireframes/siteownerstories.png)

## Features

To meets all of Hue's goals and needs, this application will be built with the following features:

### Existing Features
- Gallery - Allows *shoppers* to view, search, sort and filter products, by having them visit the gallery and utilized the built-in tools.

- Sign Up - Allows **all users** to create an account, by having them fill out a form that sends ``POST`` requests and add "Users" table in the database.

- Login: Allows **all users** to access the software, by having them fill out a form built with the HTTP ``POST`` request method to send data and ``{% csrf_token %}`` tags for security reasons.

- About: Alllows **all users** to view information and images related to the business, by having them visit the about page.


### Features Left to Implement
- Another feature idea

## Technologies Used

- [Django](https://www.djangoproject.com/)
 - The project uses **Django** to simplify development and scalability.

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
 - This project will use  uses **Allauth** to simplify authentication, registration, account management and 3rd party (social media) login.

 - [Pillow]() 
    - This project will use **the Python Imaging Library, Pillow** to add image processing capabilities to the Python interpreter.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
 1. Go to the "Contact Us" page
 2. Try to submit the empty form and verify that an error message about the required fields appears
 3. Try to submit the form with an invalid email address and verify that a relevant error message appears
 4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content

- The artwork categories in the database and application were copied from [Architecure Lab article "15 Types of Digital Art to Consider"](https://www.architecturelab.net/types-of-digital-art/)

- I copied Font Awesome's CDN from [cdnjs.com](https://cdnjs.com/libraries/font-awesome).

## UX Design

- 

- I copied components from [Bootstrap's documentation](https://getbootstrap.com/docs/5.0/components/navs-tabs/) to make Hue's navigation intuitive and responsive.


### Media
- I used this article from [CSS Tricks](https://css-tricks.com/perfect-full-page-background-image/) to style the background image on Hue's homepage.

### Backend Functionality
- The code used to manage user permissions was copied from [Real Python article "What You Need to Know to Manage Users in Django Admin"](https://realpython.com/manage-users-in-django-admin/#implement-custom-business-roles-in-django-admin).

### Acknowledgements


### Research & Planning

- I learned about writing user stories for multiple end users by reading the following articles:

 - "User Stories with Examples and Template" from [Atlassian article "User Stories with Examples and Template"](https://www.atlassian.com/agile/project-management/user-stories)

 - "User Stories and User Stories Examples", [Knowledge Hut article "User Stories and User Stories Examples](https://www.knowledgehut.com/blog/agile/user-stories-examples)

- I learned how to make user stories that capture feature requirements from:

 - [Code Insitute]()

 - [Knowledge Hut article "User Stories and User Stories Examples"](https://www.knowledgehut.com/blog/agile/user-stories-examples)

- I learned about different target markets by reading:

    - [Marketing Artfully article "Customer Demographics - Age Demographics for Advertising"][https://marketingartfully.com/customer-demographics-age-demographics-for-advertising/]
