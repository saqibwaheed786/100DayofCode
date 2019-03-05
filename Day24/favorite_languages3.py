# nest a list inside a dictionary
# ------------------------------------------------------------------------------
favorite_languages ={
'jen':['python','ruby'],
'sarag':['c'],
'edward':['ruby','go'],
'phil':['python', 'heskell'],
}

for name,languages in favorite_languages.items():
  print("\n"+ name.title() +"'s favorite languages are:")
  for language in languages:
    print("\t" + language.title())
