from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from dataclasses import dataclass
from typing import List

@dataclass
class Mystery:
    char: str
    description: str
    ability: str
# Create your views here.
def home(request):
    context = {
        "gang": ["Fred", "Daphne", "Velma", "Shaggy", "Scooby"]
    }
    return render(request, "home.html", context)

def items(request, name):
    context = {
        "name": name,
        "invest": {
            "Fred": Mystery("Fred Jones", "Fred Jones is the leader of Mystery Inc., and (more often than not) the driver of the van: The Mystery Machine. Fred is statuesque and brave; everything that the group's other male human member, Shaggy isn't.", "Ability: Traps"),
            "Daphne": Mystery("Daphne Blake", "Daphne Blake is the fashion-loving member of Mystery Inc.. Daphne's characteristic trait in the gang is her tendency to get into danger.", "Ability: Danger-prone"),
            "Velma": Mystery("Velma Dinkley", "Velma Dinkley is the bespectacled resident genius of the Mystery Inc., often being the one to decipher the clues and solve the crimes.", "Ability: Smarts"),
            "Shaggy": Mystery("Shaggy Rogers", "Shaggy Rogers is a member of Mystery Inc., and the owner and best friend of their teams's mascot: Scooby-Doo, a talking Great Dane.", "Ability: Clumsiness"),
            "Scooby": Mystery("Scooby-Doo", "Scooby-Doo is the Great Dane mascot of Mystery Inc., and pet and best friend of Shaggy Rogers.", "Ability: Clumsiness")
        }
    }
    return render(request, "info.html", context)
