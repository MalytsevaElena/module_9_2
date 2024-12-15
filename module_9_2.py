first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(str_) for str_ in first_strings if len(str_) >= 5]
second_result = [(f_str, s_str) for f_str in first_strings for s_str in second_strings if len(f_str) == len(s_str)]
third_result = {str_: len(str_) for str_ in first_strings + second_strings if len(str_) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)

