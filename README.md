# Shannon Oliver - She Codes News Project

## About This Project
 Our class had to create a news website using Django with some starter code (https://github.com/SheCodesAus/plus-django-news-project-template) that allows users to read news stories, and authors to create them.

## How To Run This Code
   First clone the repo from to your local machine, then create and activate a virtualenvironment (venv) to be able to run your server through the manage.py file to see my website.

## Database Schema
![ERD](<Screenshots/DB Schema2.png>)

## Project Features
- [X] Order stories by date
    ![Latest Stories date ordered](<Screenshots/latest stories order by date.png>)![Other Stories date ordered](<Screenshots/other stories order by date.png>)

- [X] Styled "new story" form
    ![Create New Story Form](<Screenshots/create story form.png>)

- [X] Log-in/log-out
    ![Login Page](<Screenshots/login page.png>)![Logout Button](<Screenshots/logout btn .png>)
    
- [X] "Account view" page
    ![Own Profile View](<Screenshots/userAcc view.png>)
    
- [X] "Create Account" page
    ![Create Account Form](<Screenshots/createAcc form.png>)![Create Account Button](Screenshots/createAcc-btn.png)
    
- [X] View stories by author
    ![Other Account View](<Screenshots/other author acc-story view.png>)
    
- [X] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user logged in
    !{{ As seen is screenshots above }}

- [X] "Create Story" functionality only available when user is logged in
    ![No button - not logged in](<Screenshots/no login-no create.png>)![Create button - logged in](<Screenshots/login-create btn.png>)

## Additional Features:
    
- [X] Add the ability to update and delete stories.
    ![Edit/Delete story buttons](<Screenshots/edit-delete story btn.png>)
    
- [X] Add the ability to comment on stories and see a list of other comments(if there are any).
    ![View if no comments](<Screenshots/no comment view.png>)![View if comments](<Screenshots/comments view.png>)
    
- [X] Add the ability to upload an image from your local files OR paste in your own img URL when creating a story.
    ![Upload image Button](<Screenshots/upload img btn.png>)
    
- [X] All stories now show in a line with a scroll bar to look through.
    ![Scroll other stories](<Screenshots/Scroll stories.png>)
    

## Test accounts - guest/1/2/3@guest.com & admin@admin.com
username: admin - password: admin
    
username: guestuser - password: testaccount

username: guestuser2 - password: testaccount2

username: guestuser3 - password: testaccount3