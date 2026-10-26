from faker import Faker


class TestFakeDataGeneration:
    def test_fake_data_generation(self):
        faker = Faker()   #local variable
        fullname = faker.name()
        firstname = faker.first_name()
        lastname = faker.last_name()
        email = faker.safe_email()
        password = faker.password(length=8)
        phoneno = faker.phone_number()

        print("Full Name:", fullname)
        print("First Name:", firstname)
        print("Last Name:", lastname)
        print("Email:", email)
        print("Password:", password)
        print("Phone No:", phoneno)