get_single_profile = """
{{
  profile(id: {id}) {{
    id
    firstName
    lastName
  }}
}}
"""
get_all_profiles = """
{
  profiles{
    id
    firstName
    lastName
    secondaryEmail
    user {
    id
    username
    email
    }
  }
}
"""

update_profile_mutation = """
mutation {{
  updateProfile(
		firstName: "{firstName}"
		github: "{github}"
		industry: "{industry}"
		lastName: "{lastName}"
		userBio: "{userBio}"
  ){{
    message
    profile{{
      id
      lastName
    }}
  }}
}}
"""
