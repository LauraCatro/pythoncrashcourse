from functions_printing_functions import print_models,show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventig a Function from Modifying a List

# You can send a copy of a list to a function like this:
# function_name(list[:])

print_models(unprinted_designs[:], completed_models)

