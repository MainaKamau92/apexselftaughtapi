## What does this PR do?
It creates implementation to enable a user to reset their password using their registered email

## Description of the task to be completed
- Enable registered users to reset their passwords via their emails
- Send password reset link to users registered email
- Create an HTML template for the password reset link
- Write password reset mutation for sending password reset email
- Django view for updating the password

## How can this be manually tested
- Clone repository to a local machine
- Use .exampleenv to set up the environment variables
- create migrations by running `python manage.py makemigrations`
- migrate by running `python manage.py migrate`
- start the development server by running `python manage.py runserver`
- access the graphql endpoint by navigating to `http:127.0.0.1:8000/apexselftaught`
- Register a user by running 
```
mutation {
  registerUser(email: "johndoe@gmail.com", 
    mobileNumber: "0713123456", 
    password: "johndoe123", username: "johndoe") {
    user {
      id
    },
    errors
  }
}
```
- Request for a password reset by running 
```
mutation {
  requestPasswordReset(email:"johndoe@gmail.com"){
    success
    error
    link
  }
}
```
- Copy the link that is returned to your api consuming tool's url and set your new password as shown below
<img width="1133" alt="Screenshot 2019-07-16 at 23 11 31" src="https://user-images.githubusercontent.com/26567020/61326303-1ae24600-a81f-11e9-8305-0cdeeee8bf90.png">

## Relevant PT stories
https://www.pivotaltracker.com/story/show/166928085
