import pytest
import yaml 

def yaml2json(file):
    with open(file,'r') as yaml_in:
        json_data = yaml.load(yaml_in,Loader=yaml.FullLoader)
        return json_data

diff_a  = yaml2json("./test/test.yaml")
diff_b  = yaml2json("./Manifest/03.yaml")


def test_label_exisit():
    assert 'kind' in diff_a
    assert 'apiVersion' in diff_a
    assert 'metadata' in diff_a
    assert 'spec' in diff_a
    
