import xml.etree.ElementTree as et
import config

def modify_ept_file(path):
    print(path)
    tree = et.parse(path)
    root = tree.getroot()
    
    element = root.findall(".//*[@name='@QTE:SOURCE_MODEL']/value")[0]
    element.text = config.path_to_root_model
    
    element = root.findall(".//*[@name='Model']")[0]
    el = element.findall(".//*FileRef")[0]
    el.set('persistAs', config.path_to_root_model)

    tree.write(path)
    
    return