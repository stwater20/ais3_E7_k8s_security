import pytest
import yaml 

def yaml2json(file):
    with open(file,'r') as yaml_in:
        json_data = yaml.load(yaml_in,Loader=yaml.FullLoader)
        return json_data

diff_a  = yaml2json("./test/test.yaml")
diff_b  = yaml2json("./Manifest/00.yaml")


def test_label_exisit():
    assert 'kind' in diff_a
    assert 'apiVersion' in diff_a
    assert 'metadata' in diff_a
    assert 'spec' in diff_a

def test_kind_must_NetworkPolicy():
    assert diff_a["kind"] == "NetworkPolicy"

def test_spec_security():
    assert 'policyTypes' in diff_a["spec"]
    
