txt = "This is my string! I love it."

print("First 5 chars:")
print(txt[0:6])
print(txt[:6])

print("Chars after first 5")
print(txt[5:len(txt)-1])
print(txt[5:])

print("Second sentence:")
idx = txt.index('!')
print(txt[idx+1:].strip())

print("Last 5 chars")
print(txt[-8:])


#
# cursor = fromDb()
#
# page_size = 10
# current_page = 2

#for books in cursor[page_size*(current_page-1):page_size*(current_page)]








