# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

glossary ={
'algorithm':'value',
'array':'type',
'bug':'mistake',
'comment':'arbitrary text',
'class':'user defined Objects','dictionary':'associative arry','debug':'investigate and fix','invoke':'call'}
for terms,values in glossary.items():
  print(terms.title() + " = " + values.title())
