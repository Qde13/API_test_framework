import random
from faker import Faker
from data.data import Repository


faker_en = Faker('en')
Faker.seed()


def generated_repository():
    yield Repository(
        repository_name=faker_en.sentence(nb_words=1),
        repository_description=faker_en.sentence(nb_words=random.randint(1, 10)),
    )


def generated_file():
    filepath = rf"C:\PythonProjects\APIAutomationFramework\testfile{random.randint(0, 999)}.txt"
    with open(filepath, "w+") as file:
        file.write("some text")
    return filepath
