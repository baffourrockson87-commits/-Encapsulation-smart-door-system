class Staff:
    def __init__(self, s_name, access_code):
        self.s_name = s_name          # Public attribute
        self.__access_code = access_code   # Private attribute

    # Property to view the access code
    @property
    def access_code(self):
        print("Access code viewed by an authorized user.")
        return self.__access_code

    # access code updating (using setter)
    @access_code.setter
    def access_code(self, new_code):
        if len(new_code) >= 6:
            self.__access_code = new_code
            print("Access code updated successfully.")
        else:
            print("Error: Access code must be at least 6 characters long.")

    #staff information display
    def display_info(self):
        print("Staff Information ")
        print(f"Name: {self.s_name}")
        print(f"Access Code: {self.__access_code}")


# Creating a Staff object
staff1 = Staff("Rockson Baffour", "UMAT123")

# Display staff information
staff1.display_info()

print()

# View the access code
print("Current Access Code:", staff1.access_code)

print()

# Update the access code with a valid code
staff1.access_code = "FOE.41.006"

print()

# Display updated information
staff1.display_info()

print()

# updating an invalid code
staff1.access_code = "123"