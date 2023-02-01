def details(name, dept="BSC"):  # ---->Default this value is booked
    '''Example of Default arguments'''
    print(f"Name : {name} | Department : {dept}")


print(details.__doc__)
details("Bristi")
details("Suvendu")

# Example of keyword arguments
details(name="Anuska Ghose", dept="BCA")
details(dept="BTECH", name="Supratim")
