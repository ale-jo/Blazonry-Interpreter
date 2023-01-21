import os
from textx import language, metamodel_from_file
from os.path import dirname
from textx import generator 


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
    # input_file = model._tx_filename
    # output_dir = output_path if output_path else dirname(input_file)
    # print(output_dir, ' output dir')
    print("    = = = == = = success")
    current_dir = os.path.dirname(__file__)
    mm = metamodel_from_file(os.path.join(current_dir, 'blazonry.tx'), debug= True)
    my_model = mm.model_from_file('p.txt')
    # print(my_model.fileds[0].field.__str__)
