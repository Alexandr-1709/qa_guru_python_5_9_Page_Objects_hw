from dataclasses import dataclass
from enum import Enum
from datetime import date
from typing import List


class Gender(Enum):
    Female = 'Female'
    Male = 'Male'
    Other = 'Other'


class Subject(Enum):
    english = 'English'
    maths = 'Maths'
    physics = 'Physics'
    chemistry = 'Chemistry'
    computer_science = 'Computer Science'
    economics = 'Economics'
    arts = 'Arts'
    biology = 'Biology'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: List[Subject]
    hobbies: List[Hobby]
    picture_file: str
    address: str
    state: str
    city: str
