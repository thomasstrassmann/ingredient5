# Ingredient5
## The most delicious and simple dishes - with only 5 ingredients


![Overview of Ingredient5](./static/img/documentation/overview_readme.png  "Overview of Ingredient5")

[Click here for the full website access]()



## Table of contents
1. [Introduction](#introduction) 
2. [Preparation - UX and UXD](#preparation)
3. [Agile Development](#agile)
4. [Features](#features)
5. [Testing](#testing)
6. [Deployment](#deployment) 
7. [Credits / attributes](#credits) 



## Introduction 
Ingredient5 is a django web app that is all about cooking. 
In the app, users have the opportunity to choose and recreate delicious and simple dishes. 
The special thing about the recipes is that each dish consists of 5 ingredients, it is easy to cook and yet particularly delicious. 


So the goal of Ingredient5 is to make chefs of all kinds (whether beginners or professionals) with an empty fridge, look like star chefs.... And that with minimal effort!


The application has various features / functions, which are explained in more detail in strategy and features.

## Preparation - UX and UXD
As mentioned in the introduction, the app is aimed at a broad audience. Many people unfortunately suffer from lack of time and are not able to eat sensibly. Therefore, many people resort to supplements, unhealthy food (mostly fast food), or skip meals altogether. 

Often not only the time to cook is missing, but also the time to even go shopping in the supermarket. Ingredient5 tries to fill this gap. Simple and delicious meals with a limited fridge are thus possible and excuses regarding unhealthy food should be a thing of the past.


The **UXD - User Experience Design** was declared and described in advance and includes the 5 panels *strategy, scope, structure, skeleton and surface*. 

### Strategy 
What makes Ingredient5 special? 

The content:

The simplicity of the recipes, which make dishes look complex. This makes all the recipes easy to implement and meets exactly the nerve of the time, in which no one has the time and leisure to prepare a delicious meal. In addition, the dishes are universal, that is, whether they are cooked to eat alone, served to friends, or directly appeal to a large family celebration.


Associated functions in the app should also lead to a great and intuitive user experience. 
The principles of good UX apply: simple navigation, user feedback, custom settings and a quick sense of achievement. 

The app and its content is also culturally appropriate: it's aimed at cooking amateurs who don't yet know how to cook and need to cook, as well as experienced cooks looking for inspiration. No one is excluded. 

To structure the content and make the data retrievable, there are different models, explained in detail in the scope section.

---
### Scope 

To describe the scope of the Ingridient5 app, the key features will be discussed first. 

Users should be able to log in with a username and thereby create a personal account, which is necessary for the personalizing of the content. 
However, this also means that the other content is behind this authentication hurdle. Recipes cannot be viewed without an account, which should lead to a higher registration rate.

After authentication, further functions are available to the user. For example, they can actively search for new recipes (via django generic ListView) and view the recipes in detail. An own cookbook with favorite recipes can then be created via a bookmark function. 

Furthermore, users have the option of registering for a virtual cooking class. All that is required is to select an email address, date and time (date and time specified in each case). Afterwards, the user automatically receives a confirmation email with an access link and the admin receives an overview of the participants in the backend. 

What can not be implemented within the project, just because of lack of time? 
* Users will not have the possibility to reset the password at first.
* Excessive filtering options in the recipe overview will be reduced to a minimum for the time being.
* The number of recipes will probably be 20 - 25 maximum. 
* Users will not yet be able to pay online, but a fictitious invoice will be in the mail. 

The scope, in terms of content, will stretch over 9 HTML pages.
* index.html
* signup.html
* login.html
* logout.html
* recipes.html
* recipes_detail.html
* cookbook.html
* workshop.html 
* 404 page (default django 404 page)

Here, further pages are omitted too due to time constraints. 
How the individual pages are composed is outlined in the structure section below. 

--- 
### Structure 

The structure of the app is kept very simple and is illustrated here for the sake of completeness. This results in a simple, clear and intuitive navigation for the user. 

![Structure of Ingredient5](./static/img/documentation/structure_ingredient5.png "Structure of Ingredient5")

---
### Skeleton 

In order to implement the pages safer, faster and more efficiently, wireframe models were created in advance. Excluded from this are the pages login, signup, logout and the 404page, as these are simple pages with either a form element or a feedback display. Wireframe models are therefore only created for more complex pages. 

The models for the index, recipes, recipes_list, cookbook, workshop are listed down below. 

![Wireframe of index page](./static/img/documentation/wireframe_index.png "Wireframe of index page")

![Wireframe of recipes page](./static/img/documentation/wireframe_recipes.png "Wireframe of recipes page")

![Wireframe of recipes detail page](./static/img/documentation/wireframe_recipes_detail.png "Wireframe of recipes detail page")

![Wireframe of cookbook](./static/img/documentation/wireframe_cookbook.png "Wireframe of cookbook")

![Wireframe of workshops](./static/img/documentation/wireframe_workshop.png "Wireframe of workshops")

---
### Surface

In terms of visual language, the main points that remain are colors, logo and fonts.
The color palette consists of the main color #38FA46 and some according compound colors. Down below you can see an abstract of the Adobe Color Wheel.

![Color palette](./static/img/documentation/color_palette.png "Color palette")

The app logo was created with the Adobe Express. The corresponding green should reflect the targeted healthy diet. 

![Logo](./static/img/documentation/final-logo.png "Logo")

Google Fonts was used for the typography. The font "Bebas Neue" is used for headlines and titles, the font "Ubuntu" is used for everything else. The icons in the app are also from Google (Google Icons). All content from Google is not provided via a CDN, but has been downloaded. 

## Agile Development

The entire project was developed in an agile manner. Particularly noteworthy is the sprint board (git hub project), on which the user stories and their status were recorded. For better traceability, the project was set to public. 

To make it clearer, the user stories were divided into epics (unfortunately not visible in the sprint). For the sake of completeness, the epics with the corresponding stories are listed here once again. 

### Admin Epic:
**Introduction:**

In the following, we will first outline what the biggest problems and challenges for the admin are and how they are solved. In addition, we will consider how the starting position can also be improved sustainably for the admin and how the right foundation can be laid. 

The admin is author, control unit and contact person in one for the ingredients community and therefore has many requirements. All requirements must therefore be clearly manageable in the backend area and without major technical knowledge. 

Therefore, different panels for these areas are created in the admin area and filterable settings are created so that the search is faster and more efficient. Furthermore, it is important that there are not too many actions for comments, workshops or recipes to keep it simple. 

**Goals & Outcomes:**

Even relatively new employees find their way around the backend within a few days. Creating new recipes is very quick, as is checking and approving comments. 

Clear **user acceptance criteria** are generally: simplicity, structuredness, great design, workshops as an experience. This is the only way Ingredients can establish itself as a source of cooking ideas. 

In addition, all information on workshops can be called up in this control center in order to prepare optimally. 

The user stories developed for the admin were:

* As an admin (employee of ingredient5), I would like to create recipes so that the users can explore the recipes.
* As an admin (employee of ingredient5), i would like to approve comments so that no inappropiate comments are on the site.
* As an admin (employee of ingredient5), i would like to get an overview of the workshop participants so that everything can be prepared accordingly.

All user stories are must have stories!

The admin stories can be broken down even further into tasks: 

* Create a backend form that allows the admin to add new recipes quickly and easily.
* Implement the ability to approve comments that are initially locked. 
* Create a workshop area in the backend where users are assigned to booked workshops. 


### User Epic:
**Introduction:**

In this section, we will first outline what the biggest problems and challenges for the users are and how they are solved. The user is the linchpin of the app and is therefore always brought to the fore during development. User experience and design must therefore never be neglected and are continuously improved. 


**Goals & Outcomes:**

One of the most important measures and goals is to create an attractive index page that attracts users. To increase the registration rate, all content and functions are only accessible with an account. 

The menu navigation as well as the CRUD operations are self-explanatory and no problem even for inexperienced internet users. 

Great recipes make you want more, which should increase the registration rate of the workshops and thus also the turnover. 

The user stories developed for the user were:

* As a site user, I want the ability to create an account, so that I can comment on recipes and create my own personal cooking book.
* As a site user, I want to see the recipes with the according comments, so that I can get new cooking ideas.
* As a user, I want to be able to comment on a recipe so that I can give feedback to the author and discuss it with other members.
* As a site user, I want to have a cookbook of my favorite recipes, so that I do not have to search them every time again.
* As a user, I want the ability to like (and at the same time bookmark) my favorite recipes so that i can store them in my own virtual cooking book.
* As a user, I want the ability to book (and delete) a virtual cooking-workshop, so that I can enhance my cooking skills and interact with other people.

All user stories are must have stories!


The resulting tasks look like this: 

* Create an athorization option for any user who wants to sign up.
* Build an individual comment section for each dish. 
* Code a comment function
* Create a personal cookbook for every user
* Implement the bookmark function to save dishes to the cookbook
* Code a workshop section with an acoording model, view and template in a separate app 


Down below, you can see the sprint board in action during development.
![Agile development](./static/img/documentation/agile_development.png "Agile development")



## Features
The Ingredients app has many features, which will now be examined in more detail below. 


The app has only custom css code, which is around a thousand lines long. Highlights are of course the reponsiveness on all devices, a color effect in the hero image, many media queries. Compared to other websites / apps, responsiveness is even more important in the context of cooking, because peopl at the stove look on smartphones and tablets, not on desktop computers.  Bootstrap was not used, because I personally find the styling with flexbox and grid more pleasant and the html files do not have umpteen div nestings. Bootstrap tends to mix styling and structure. 

Another feature are the present and working CRUD operations that the user can perform in the frontend.
These include: 

* the creation of comments
* the creation of accounts 
* the creation of workshop registrations
* reading comments
* reading recipes
* updating the cookbook (by deleting dishes)
* updating the list of recipes by filtering them
* deleting recipes from the cookbook 
* deleting workshops from the personal reminder section  


Users also get feedback on almost all CRUD operations, such as when a comment was left, or a workshop was booked. For small CRUD operations (such as adding dishes to the cookbook), this was initially omitted, as it is more distracting than useful in the flow of action, at least in the current version. However, this may become a feature in the future. 

A special feature is also the automatic sending of emails, which was implemented with the help of the built-in send_email function of Django. For this purpose a new gmail account was created especially for ingredients. Down below you can see an example email, which can be improved in the future.

![Email example](./static/img/documentation/email_example.png "Email example")


### Features for the future 
The following features would be ideas for further development...
* The independent cancellation of workshops. This was not implemented, as this is also related to the fictitious accounting system. Therefore, this is still the task of the admins. 
* More filtering options of the recipes (for example, whether it is vegetarian or not), or a search bar.  However, since it is "only" 34 dishes for now, a filter option by region is perfectly sufficient. Anything else would be over-engineered.
* An account setting section. Here users could tell something about themselves and choose an avatar, which would be visible to other users. 


## Testing 

The page and its functionality was tested manually as well as automatically. For a better overview, these two areas are now treated separately from each other. 

**Manual testing**

Manual testing was done primarily using Chrome DevTools (Lighthouse) and validators for HTML, CSS, JavaScript and Python.

The layout was tested in portrait and landscape mode on the following devices: iPhone SE, iPhone XR, iPhone 12 Pro, Pixel 5, Samsung Galaxy S8+, Surface Pro 7, Surface Duo, Galaxy Fold, Samsung Galaxy A51/71, Nest Hub, Nest Hub Max and common monitors. No display errors were detected. If other devices show any, they would have to be improved afterwards. 

To test accessibility and SEO, Lighthouse was used. 

![Lighthouse report](./static/img/documentation/lighthouse.png  "Lighthouse report")

The test results of Best Practices are slightly worse than those of Accessibility and SEO, because images with somewhat low resolution were also used (especially in the Recipes section). Of course, this has to do with the fact that the images should fit the dishes and only these were available. If time had allowed, the search for high-resolution images would be something to look into. 




Furthermore, the W3C Validator was used to ensure that the HTML and CSS file are valid. Since the template engine of Django causes problems with validation, the Django logic was removed. That is: {% load static %} was removed and all src and href values were replaced with a "#". 


No fatal errors exist anymore at this moment. JShint was used to find errors in JavaScript code. In the corrected version there are currently only hints that some techniques can only be used with ES6, so the code is valid.

## Deployment 

[You can access the website right here](https://)


## Credits
