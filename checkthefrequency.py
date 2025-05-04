student_data = {'id1':
    {'name': ['Sarah'],
     'class': ['V'], # type: ignore
     'subject_integration': ['english, math, science']
   },
'id2':
 {'name': ['Max'],
  'class': ['V'],
  'subject_integration': ['english, math, science']
 },
'id3':
 {'name': ['Sam'],
 'class': ['V'],
 'subject_integration': ['english, math, science']
 },
'id4': 
{'name': ['Tyler'],
  'class': ['V'],
  'subject_integration': ['english, math, science']
 },
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)