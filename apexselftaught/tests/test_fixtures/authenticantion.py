login_user_query = '''
mutation {{
  loginUser(email:"{email}", password:"{password}"){{
    token
    errors
    verificationPrompt
  }}
}}
'''

register_user_query = '''
mutation {
  registerUser(username:"johnydoe" email: "johnydoe@test.com",
  mobileNumber:"0713116974", password: "johnydoe123"){
    user {
      email
    }
    errors
  }
}

'''
register_user_query2 = '''
mutation {
  registerUser(username:"marydoe" email: "marydoe@test.com",
  mobileNumber:"0713516974", password: "marydoe123"){
    user {
      id
      email
    }
    errors
  }
}

'''
register_user_query3 = '''
mutation {
  registerUser(username:"philipdoe" email: "philipdoe@test.com",
  mobileNumber:"0712116974", password: "philipdoe123"){
    user {
      id
      email
    }
    errors
  }
}

'''
register_user_query2 = '''
mutation {
  registerUser(username:"marydoe" email: "marydoe@test.com",
  mobileNumber:"0713516974", password: "marydoe123"){
    user {
      id
      email
    }
    errors
  }
}

'''
register_user_query3 = '''
mutation {
  registerUser(username:"philipdoe" email: "philipdoe@test.com",
  mobileNumber:"0712116974", password: "philipdoe123"){
    user {
      id
      email
    }
    errors
  }
}

'''
invalid_register_query = '''
mutation {
  registerUser(username:"" email: "johnydoe@test.com",
  mobileNumber:"0713116974", password: "johnydoe123"){
    user {
      id
      email
    }
  }
}
'''
login_query = '''
mutation {
  loginUser(email:"johnydoe@test.com", password:"johnydoe123"){
    token
    errors
    verificationPrompt
  }
}
'''
get_all_users_query = '''
{
  users{
    id
    username
  }
}
'''
get_single_user_query = '''
{
  user(id:8){
    id
    username
  }
}
'''
get_inexistent_user_query = '''
{
  user(id:400){
    id
    username
  }
}
'''
