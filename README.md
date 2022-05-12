# Pitch Blog

## Built By Sandra

## Description
This Application allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application


You can view the site at:[]()

## User Stories
As a user I would like to:
* See various pitches according to category
* Allowed to Register an account
* Allowed to Log in
* Create and post a pitch
* Comment on various pitches
* Vote on various pitches


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display  pitches | **On page load** | List of various pitches from users is displayed in a list |
| Display tabs with pitch by category | **On Tab link click** | Clickable links to open pitch based on category |
| Display tabs for login page  | **On page load** | Registered users can log into their accounts and post a pitch |
| Display tabs for Register  | **On page load** | Registered users are redirected to Log in |
| To post a pitch | **On log in** |  users can create and post pitches|


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pipenv


### Cloning
* In your terminal:

        $ git clone git@github.com:Dindihub/Pitch-blog.git
        $ cd pitch-blog

## Running the Application
* Creating the virtual environment

        $ pip install pipenv
        $ pipenv install requests
        $ pipenv shell
       


* To run the application, in your terminal:

        $ python3 app.py
        $ flask run

## Testing the Application
* To run the tests for the class files:

        $ python3  app.py tests 

## Technologies Used
* Python3.8
* Flask

## Known Bugs
No known bugs

### License
MIT (c) 2022 **[Sandra Dindi](https://github.com/Dindihub/Pitch-blog.git)**
