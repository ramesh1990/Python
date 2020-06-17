import re

'''Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format'''
re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1', text)

''' Write a Python program to find all five characters long word in a string.  '''
re.search(r'\b\w{5}\b',text)

''' Write a Python program to extract values between quotation marks of a string. 
IO : text = '"Python", "PHP", "Java"'
OP : ['Python', 'PHP', 'Java']
'''
re.findall(r'"(.*?)"',text)

''' Write a Python program to remove multiple spaces in a string. '''
re.sub(r' +',' ',text)

