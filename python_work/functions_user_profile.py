def build_profile(firts,last,**user_info):
    user_info['first_name'] = firts
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', 
                             location = 'princeton',
                            field = 'physics' )

user_profile1 = build_profile('diana','castro',
                              university = 'unam',
                              career = 'computing')

print(user_profile)
print(user_profile1)

