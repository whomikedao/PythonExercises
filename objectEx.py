class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print(f'Hello {other_person}, I am {self.name}')
        self.greeting_count += 1

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email} \n{self.name}'s phone number: {self.phone}")

    def add_friend(self, other_friend):
        self.friends.append(other_friend)

    def num_friends(self):
        print(len(self.friends))

    def __str___(self):
        return f'Person: {self.name}, {self.email}, {self.phone}'


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
# print(jordan.__str__(jordan))
jordan.add_friend('sonny')
print(jordan.friends)
print(jordan.num_friends())
jordan.greet('sonny')
print(jordan.greeting_count)

print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f'Make: {self.make} \nModel: {self.model} \nYear: {self.year}')



car1 = Vehicle('Nissan', 'Leaf', '2018')
car1.print_info()