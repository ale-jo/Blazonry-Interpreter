import os
from textx import language, metamodel_from_file
from os.path import dirname
from textx import generator
from pathlib import Path

from blazonry.blazonry import Blazonry 
# from blazonry import Blazonry 


__version__ = "0.1.0.dev"


@language('blazonry', '*.txt')
def blazonry_language():
    "blazonry language"
    current_dir = os.path.dirname(__file__)
    mm = metamodel_from_file(os.path.join(current_dir, 'blazonry.tx'))
    my_model = mm.model_from_file('p.txt')
    # Here if necessary register object processors or scope providers
    # http://textx.github.io/textX/stable/metamodel/#object-processors
    # http://textx.github.io/textX/stable/scoping/

    return mm

@generator('blazonry', 'txt')
def blazonry_generate_files(metamodel, model, output_path, overwrite, debug): 
    "A generator function that produce txt report from model."
    output_file = Path(model._tx_filename).stem +'_result.txt' #get input file name and create output filename
    print(output_file)
    blazonry = Blazonry()
    blazonry.interpret(model,output_file)
   
