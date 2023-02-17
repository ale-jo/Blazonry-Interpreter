import os
from textx import language, metamodel_from_file
from os.path import dirname
from textx import generator
from pathlib import Path
import sys
from field import *
from ordinaries import *
import turtle

from blazonry import Blazonry 

colors = {
            "Azure":"blue",
            "Vert":"green",
            "Gules":"red",
            "Sable":"black",
            "Purpure":"violet",
            "Ermine":"gray",
            "Vair":"gray",
            "Or":"gold",
            "Argent":"silver"
        }

def main(turtle_field_color, turtle_party, turtle_chief,turtle_bordure, turtle_ordinary, turtle_ordinary_color):
    draw_field(turtle_field_color)
    if turtle_party is not None:
        draw_party(turtle_party, turtle_field_color)
    if turtle_ordinary is not None:
        ordinary = get_ordinary_function(turtle_ordinary)
        if turtle_ordinary_color is not None:
            ordinary(colors[turtle_ordinary_color])
        else:
            print("Neispravan blazon! Niste prosledili ispravan broj boja. Bice primenjena podrzaumevana boja: dark olive green")
            ordinary()
    if turtle_chief is not None:
        chief(colors[turtle_chief])
    if turtle_bordure is not None:
        bordure(colors[turtle_bordure])




        
def draw_field(turtle_field_color):
    if type(turtle_field_color) == str:
        field(colors[turtle_field_color])
    elif len(turtle_field_color) == 2 or len(turtle_field_color) == 3 : #ukoliko je turtle_field_color lista boja
        field(colors[turtle_field_color[1]])
    elif len(turtle_field_color) == 1:
        field(colors[turtle_field_color[0]])
    else: #ukoliko nije prosledio boje
        print("Neispravan blazon! Niste prosledili ispravan broj boja. Bice primenjena podrzaumevana boja: dark olive green")
        field()
def draw_ordinary():
    pass

def get_ordinary_function(ordinary):
    if ordinary == "Pale": return pale
    elif ordinary == "Fess": return fess
    elif ordinary == "Bend": return bend
    elif ordinary == "Saltire": return saltire
    elif ordinary == "Chevron": return chevron
    elif ordinary == "Pall": return pall


def draw_party(turtle_party, turtle_field_color):
    if turtle_party == "Per Pall":
            if len(turtle_field_color) == 3:
                per_pall(colors[turtle_field_color[0]],colors[turtle_field_color[2]])
            else:
                print("Neispravan blazon! Niste prosledili dovoljan broj boja. Bice primenjene podrzaumevane boje: dark olive green, dark sea green")
                per_pall()
    else:
        part = get_party_function(turtle_party)
        if len(turtle_field_color) == 2:
            part(colors[turtle_field_color[0]])
        else:
            print("Neispravan blazon! Niste prosledili ispravan broj boja. Bice primenjene podrzaumevana boja: dark olive green")
            part()
    
def get_party_function(party_name):
    if party_name == "Per Pale": return per_pale
    elif party_name == "Per Fess": return per_fess
    elif party_name == "Per Bend": return per_bend
    elif party_name == "Per Saltire": return per_saltire
    elif party_name =="Per Chevron": return per_chervon


if __name__ == "__main__":
    print("main")
    print("    = = = == = = main")
    # print(sys.argv[1])
    # current_dir = os.path.dirname(__file__)
    mm = metamodel_from_file("blazonry.tx")
    # m = mm.model
    command = ''
    while command.lower() != 'x':
        blz = input("\n>> Unesite blazon(X za prekid rada programa): ")
        command = blz
        if blz.lower() != 'x':
            my_model = mm.model_from_str(blz+'.')          
            blazonry = Blazonry()
            turtle_field_color, turtle_party, turtle_chief,turtle_bordure, turtle_ordinary, turtle_ordinary_color = blazonry.interpret(my_model) 
            # print("turtle_field_color",turtle_field_color )
            # print("turtle_party", turtle_party)
            # print("turtle_chief",turtle_chief)
            # print("turtle_bordure",turtle_bordure)
            # print("turtle_ordinary",turtle_ordinary)
            # print("turtle_ordinary_color",turtle_ordinary_color)
            turtle.reset()
            turtle.shape(name='turtle')
            main(turtle_field_color, turtle_party, turtle_chief,turtle_bordure, turtle_ordinary, turtle_ordinary_color)

    
    
    

