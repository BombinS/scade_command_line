import xml.etree.ElementTree as et
import config

def modify_ept_file(path):
    tree = et.parse('tmp/MC21_FWA_CAS_ELEC_007.etp')
    root = tree.getroot()
    
    element = root.findall(".//*[@name='@QTE:SOURCE_MODEL']/value")[0]
    element.text = config.path_to_root_model
    
    element = root.findall(".//*[@name='Model']")[0]
    el = element.findall(".//*FileRef")[0]
    el.set('persistAs', config.path_to_root_model)

    tree.write('tmp/MC21_FWA_CAS_ELEC_007.etp')
    
    return