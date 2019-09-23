login_user_query = '''
mutation {{
  loginUser(email:"{email}", password:"{password}"){{
    token
    message
    verificationPrompt
  }}
}}
'''

register_user_query = '''
mutation {{
  registerUser(username:"{username}" email: "{email}", mobileNumber:"{mobileNumber}", password: "{password}"){{
    user {{
      email
    }}
    message
  }}
}}

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
{{
  user(id:{id}){{
    id
    username
  }}
}}
'''
