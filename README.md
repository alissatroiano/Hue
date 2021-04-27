# Hue

This full-stack application was developed for Hue, an online art gallery and store where users can view and purchase artwork. The main goal of Hue's website is to display and sell their artwork to shoppers digitally. Hue is a fictional company that was created for the purpose of this project.

As the Milestone 4 Project for [Code Institute's](https://codeinstitute.net) [Full Stack Software Development Diploma Program](https://codeinstitute.net/full-stack-software-development-diploma/), Hue was built with HTML, CSS, Bootstrap 5, JavaScript, Python 3, and Django.

## UX

### Summary

Hue, a fictional art gallery & store, needs to move their business online and sell their work to customers digitally. The business needs software that gives them the ability to:

- Add, edit and remove products from the shop

- Receive payments upon purchases

- Sell and send products to customers

Hue's niche target market is comprised of male & female luxury art enthusiasts, ages 24 - 39, that want to preview and purchase art online. In order to meet the needs of these shoppers, Hue's website should allow them to:

- View art products

- Add selected products to a shopping cart

- Purchase items (via online Stripe payment)

- Sign up and become a member

- Login to persist shopping cart between visits


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
- Home - A

- Gallery:

**Shopper**

- Allows *shoppers* to view, search, sort and filter products, by having them visit the gallery and utilized the built-in tools.

**Site Owner**
- Gives *site owner* the opportunity to view the gallery page as a regular shopper/user would.

- Sign Up - Allows **all users** to create an account, by having them fill out a form that sends ``POST`` requests and add "Users" table in the database.

- Login: 

**Shoppers**

- Provides an opportunity for **shoppers** to persist their cart between visits, by logging in.

**Site Owner**
- Allows the *site owner* to access special product management tools hidden from other users, by filling out secure form that sends data and logging in.

- About: Allows **all users** to view information and images related to the business, by having them visit the about page.


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

- I copied components from [Bootstrap's documentation](https://getbootstrap.com/docs/5.0/components/navs-tabs/) to make Hue's navigation intuitive and responsive.

- I copied the sticky bottom navigation (with tabs) from [this Codepen pen](https://codepen.io/alissatroiano/pen/JjEBLvK).


### Media
- I used this article from [CSS Tricks](https://css-tricks.com/perfect-full-page-background-image/) to style the background image on Hue's homepage.

- Hue's images were copied from the following sources:

    - **Hero** background image: Pexels](https://www.pexels.com/photo/abstract-painting-2156881/)

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
