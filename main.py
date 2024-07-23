# imports
import json
from lib import find_path_to_key, get_value_from_path


# read json string from file
with open("test.json") as F:
    json_str = F.read()

# convert json string to Python dict
page = json.loads(json_str)

# retrieve the 'boxes' from the file
boxes = page.get('boxes')

# initial variables
sections = []  # final result
section = str()  # section name for each 'box'
texts = [] # list of texts in each section

def get_texts(boxes):
    global section, texts

    if not boxes:
        return
    
    for box in boxes:
        # get the box level
        level = box.get('level')

        # in case of new section, reinitialize the section and append it to 'sections'
        if level == 'section':
            if section:
                sections.append({"section": section, "texts": texts})
            section = box.get('name')
            texts = []
            
        # if the 'box' level is 'widget' search for "text" keys and get the corresponding value
        # then get the "type" from the widget box
        if level == 'widget':
            path = find_path_to_key(box, "text")
            if path:
                text_value = get_value_from_path(box, path)
                path = path[:-3]
                path.append('type')
                text_type = get_value_from_path(box, path)
                text_dict = {"type": text_type, "text": text_value}
                texts.append(text_dict)
        else:
            get_texts(box.get('boxes'))
        
    return

# main program
get_texts(boxes)
j_result = json.dumps(sections, indent=4)
print(j_result)
