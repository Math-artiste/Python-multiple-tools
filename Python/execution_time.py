from time import time
start = time()

email = input("Enter your email : ")
email=email.strip()
slicer_index=email.index("@")
username = email[:slicer_index]
domain_name = email[slicer_index + 1:]
print("Your user name is ", username, " and your domain is ", domain_name)

#code end

end = time()
execution_time = end - start
print("Execution time (s) : ", execution_time)
