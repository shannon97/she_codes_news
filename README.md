# Shannon Oliver - She Codes News Project

## About This Project
 Our class had to create a news website using Django with some starter code (https://github.com/SheCodesAus/plus-django-news-project-template) that allows users to read news stories, and authors to create them.

## How To Run This Code
   First clone the repo from to your local machine, then create and activate a virtualenvironment (venv) to be able to run your server through the manage.py file to see my website.

## Database Schema
![ERD](<DB Schema2-1.png>)

## Project Features
- [X] Order stories by date
    ![Latest Stories date ordered](<latest stories order by date-1.png>)![Other Stories date ordered](<other stories order by date-1.png>)

- [X] Styled "new story" form
    ![Create New Story Form](<create story form-1.png>)

- [X] Log-in/log-out
    ![Login Page](<login page-2.png>)![Logout Button](<logout btn -1.png>)
    
- [X] "Account view" page
    ![Own Profile View](<userAcc view-1.png>)
    
- [X] "Create Account" page
    ![Create Account Form](<createAcc form-1.png>)![Create Account Button](createAcc-btn-1.png)
    
- [X] View stories by author
    ![Other Account View](<other author acc-story view-1.png>)
    
- [X] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user logged in
    !{{ As seen is screenshots above }}

- [X] "Create Story" functionality only available when user is logged in
    ![No button - not logged in](<no login-no create-1.png>)![Create button - logged in](<login-create btn-1.png>)

## Additional Features:
    
- [X] Add the ability to update and delete stories.
    ![Edit/Delete story buttons](<edit-delete story btn-1.png>)
    
- [X] Add the ability to comment on stories and see a list of other comments(if there are any).
    ![View if no comments](<no comment view-1.png>)![View if comments](<comments view-1.png>)
    
- [X] Add the ability to upload an image from your local files OR paste in your own img URL when creating a story.
    ![Upload image Button](<upload img btn-1.png>)
    
- [X] All stories now show in a line with a scroll bar to look through.
    ![Scroll other stories](<Scroll stories-1.png>)
    

## Test accounts - guest/1/2/3@guest.com & admin@admin.com
username: admin - password: admin
    
username: guestuser - password: testaccount

username: guestuser2 - password: testaccount2

username: guestuser3 - password: testaccount3