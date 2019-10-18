import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# Works well!
dupes = set(names_1).intersection( names_2 )
duplicates.append( list(dupes) )
duplicates = duplicates[0]
# 0.00590205192565918 seconds

# -----------------------------------------------

# # 2nd
# for i in names_1:
#     if i in names_2:
#         duplicates.append( i )
# # 2.2562029361724854 seconds

# -----------------------------------------------

# # Original
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# # 9.02682900428772 seconds

print( '\n\n' , duplicates )

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

