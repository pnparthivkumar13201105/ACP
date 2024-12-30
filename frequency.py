def count_value_frequency(dictionary, value_to_check):
    values = dictionary.values()
    frequency = sum(1 for value in values if value == value_to_check)
    return frequency

my_dict = { "a": 5, "b": 3,"c": 5,"d": 2,"e": 5}
value = 5
result = count_value_frequency(my_dict, value)
print(f"The frequency of {value} in the dictionary is: {result}")
