import json
import os
from unidecode import unidecode
import re

local_path = os.path.dirname(os.path.abspath(__file__))
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
json_str = json.dumps(json_data)
json_data = (unidecode(json_str))
json_dict = json.loads(json_data)

def generate_class_hierarchy(json_dict :dict, superclass_name:str=None,superclass_args:list=[]):
    class_defs = ""

    for class_name, class_attrs in json_dict.items():

        class_def = generate_class_def(class_name, class_attrs, superclass_name,superclass_args)
        class_defs += class_def

        if "subclasses" in class_attrs:
            super_attr = (list(class_attrs.keys())+superclass_args)
            super_attr.remove("subclasses")
            subclass_defs = generate_class_hierarchy(class_attrs["subclasses"], class_name, super_attr)
            class_defs += subclass_defs

    return class_defs

def write_content(content,filename):
        with open(filename, "w", encoding='utf-8') as f:
            f.write(content)
