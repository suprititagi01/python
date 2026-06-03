#dictionaries it means key-value.

dict_creams = {'name':'suprit', 'age':22, 'fav ice cream': ['cone','cup']};
print(dict_creams)
print(type(dict_creams))
print(dict_creams.values())
print(dict_creams.keys())
print(dict_creams.items())

#changing the name

dict_creams['name'] = 'sunil'
print(dict_creams)

#updaing the values

dict_creams.update({'name':'suprit', 'age':22, 'wight':300})
print(dict_creams)

#deleting

del dict_creams['wight']
print(dict_creams)