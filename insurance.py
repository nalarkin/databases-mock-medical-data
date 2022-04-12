from string import ascii_uppercase
from faker import Faker

fake = Faker()

def member_id()-> str:
    return fake.unique.bothify('???#########', letters=ascii_uppercase)
    
def group()-> str:
    return fake.bothify('######')

def name()-> str:
    return fake.company()

def policy_number()-> str:
    return fake.bothify('#####')

def in_network()-> str:
    return fake.boolean(chance_of_getting_true=80)
