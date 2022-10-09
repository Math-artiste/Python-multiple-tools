email = input("Enter your email : ")

#remove unecessary spaces
email=email.strip()

#ge index of @
slicer_index=email.index("@")

#fetch the user name by string slicing
username = email[:slicer_index]

#fetch the domain nzame by string slicing
domain_name = email[slicer_index + 1:]

print("Your user name is ", username, " and your domain is ",domain_name)
