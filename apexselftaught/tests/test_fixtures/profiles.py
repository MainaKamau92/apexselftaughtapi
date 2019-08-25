create_profile_mutation = '''
mutation {
  createProfile(
    avatar: "avatar.rr",
    country: "Kenya"
    county: "Kisumu"
    firstName: "John"
    github: "github/johndoe"
    industry: "Software"
    lastName: "Doe"
    secondaryEmail: ""
    userBio: "I love to code"
    website: "johndoe.me"
  ){
    profile{
      id
      firstName
    }
  }
}
'''
get_single_profile = """
{
  profile(id: 2) {
    id
    firstName
    lastName
  }
}
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

update_profile = """
mutation {
  updateProfile(
    avatar: "avatar.rr",
    country: "Kenya"
    county: "Thika"
    firstName: "Lewis"
    github: "github/mainakamau92"
    industry: "Software"
    lastName: "Maina"
    secondaryEmail: "lewismaina@jack.com"
    userBio: "I love thinking"
    website: "lewismaina.me"
  ){
    message
    profile{
      id
      lastName
    }
  }
}
"""
foreign_update_profile = """
mutation {
  updateProfile(
    avatar: "avatar.rr",
    country: "Kenya"
    county: "Thika"
    firstName: "Lewis"
    github: "github/mainakamau92"
    industry: "Software"
    lastName: "Maina"
    secondaryEmail: "lewismaina@jack.com"
    userBio: "I love thinking"
    website: "lewismaina.me"
  ){
    message
    profile{
      id
      lastName
    }
  }
}
"""
