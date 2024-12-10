def build_person(firts_name, last_name, age=None):
    person = {'first': firts_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('diana', 'castro', age=20)
print(musician)
