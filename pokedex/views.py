from django.shortcuts import render

def index(request):
    pokemons = ["pikachu", "bulbasaur", "charmander", "squirtle", "jigglypuff", "meowth", "psyduck", "snorlax", "soteldo"]
    return render(request, "index.html", {"pokemons": pokemons})

def pokemon_details(request, pokemon):
    return render(request, "details.html", {
        "pokemon": pokemon
    })
    