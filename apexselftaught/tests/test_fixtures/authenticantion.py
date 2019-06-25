login_user_query = '''
mutation {{
  loginUser(email:"{email}", password:"{password}"){{
    token
  }}
}}
'''

register_user_query = '''
mutation {
  registerUser(username:"johnydoe" email: "johnydoe@test.com", mobileNumber:"0713116974", password: "johnydoe123"){
    user {
      id
      email
    }
  }
}

'''
# users_query = '''
# {
#   users {
#     id
#     username
#   }
# }
# '''
# user_query = '''
# {
#   user(id: 1) {
#     id
#     username
#   }
# }
# '''
# user_ghost_query = '''
# {
#   user(id: 10) {
#     id
#     username
#   }
# }
# '''
