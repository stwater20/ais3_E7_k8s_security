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




def test__Ingress_outside_cluster():
    if 'ingress' in diff_a['spec']:
        if diff_a['spec']['ingress']: 
            if 'ports' in diff_a["spec"]["ingress"][0]:
                if 'podSelector' in diff_a["spec"]["ingress"][0]["from"][0]:
                    assert 'app' in diff_a["spec"]["ingress"][0]["from"][0]["podSelector"]["matchLabels"], "\r\nUse specific pod selectors to achieve least-privilege security or allow all ingress traffic within namespace to get started with simpler policy."
                else:
                    assert diff_a["spec"]["ingress"][0]["from"][0]["ipBlock"]["cidr"] == "0.0.0.0/0" , "\r\n- allow ingress from any endpoint only to specific pods \r\n- allow ingress from any endpoint only to any pods but only specific port(s) (e.g to port 80)\r\n- allow ingress from any endpoint only to any pod in the namespace"
            else:
                assert 'ingress' in diff_a["spec"] ,"\r\n After applying a deny-all policy which blocks all non-whitelisted traffic to the application, now you have to allow access to an application from all pods in the current namespace.\r\nApplying this policy makes any other policies restricting the traffic to the pod void, and allow all traffic to it from its namespace and other namespaces."
                assert 'egress' in diff_a["spec"] ,"\r\nTo achieve least-privilege security, consider one of the following options instead:\r\n- allow egress to specific CIDRs\r\n- allow egress to specific FQDNs\r\n- allow egress to any endpoint outside of the cluster"
    else:
        assert 'ingress' in diff_a["spec"] ,"\r\n After applying a deny-all policy which blocks all non-whitelisted traffic to the application, now you have to allow access to an application from all pods in the current namespace.\r\nApplying this policy makes any other policies restricting the traffic to the pod void, and allow all traffic to it from its namespace and other namespaces."
        assert 'egress' in diff_a["spec"] ,"\r\nTo achieve least-privilege security, consider one of the following options instead:\r\n- allow egress to specific CIDRs\r\n- allow egress to specific FQDNs\r\n- allow egress to any endpoint outside of the cluster"

def test_Ingress_in_namespace():
    if 'ingress' in diff_a['spec']:
        if diff_a['spec']['ingress']: 
            if 'podSelector' in diff_a["spec"]["ingress"][0]["from"][0]:
                assert 'app' in diff_a["spec"]["ingress"][0]["from"][0]["podSelector"]["matchLabels"], "\r\nUse specific pod selectors to achieve least-privilege security or allow all ingress traffic within namespace to get started with simpler policy."
                assert 'port' in diff_a["spec"]["ingress"][0]["ports"][0],"\r\nUse specific pod selectors to achieve least-privilege security or allow all ingress traffic within namespace to get started with simpler policy."
    else:
        assert 'ingress' in diff_a["spec"] ,"\r\n After applying a deny-all policy which blocks all non-whitelisted traffic to the application, now you have to allow access to an application from all pods in the current namespace.\r\nApplying this policy makes any other policies restricting the traffic to the pod void, and allow all traffic to it from its namespace and other namespaces."
        assert 'egress' in diff_a["spec"] ,"\r\nTo achieve least-privilege security, consider one of the following options instead:\r\n- allow egress to specific CIDRs\r\n- allow egress to specific FQDNs\r\n- allow egress to any endpoint outside of the cluster"


def test_Ingress_in_cluster():
    if 'ingress' in diff_a['spec']:
        if diff_a['spec']['ingress']: 
            if 'from' in diff_a["spec"]["ingress"][0]:
                if 'namespaceSelector' in diff_a["spec"]["ingress"][0]["from"][0]:
                    assert 'port' in diff_a["spec"]["ingress"][0]["ports"][0], "\r\nIf pods in the namespace need to receive ingress traffic from other pods in the cluster, consider one of the following options:\r\n- allow ingress only from selected namespaces\r\n- allow ingress only from pods that match selected labels\r\n- allow all ingress traffic from any pod in the cluster"
    else:
        assert 'ingress' in diff_a["spec"] ,"\r\n After applying a deny-all policy which blocks all non-whitelisted traffic to the application, now you have to allow access to an application from all pods in the current namespace.\r\nApplying this policy makes any other policies restricting the traffic to the pod void, and allow all traffic to it from its namespace and other namespaces."
        assert 'egress' in diff_a["spec"] ,"\r\nTo achieve least-privilege security, consider one of the following options instead:\r\n- allow egress to specific CIDRs\r\n- allow egress to specific FQDNs\r\n- allow egress to any endpoint outside of the cluster"

def test_Egress_outside_cluster():
    if 'egress' in diff_a['spec']:
        if diff_a['spec']['egress']:
            if 'ports' in diff_a["spec"]["egress"][0]:
                if 'podSelector' in diff_a["spec"]["egress"][0]["to"][0]:
                    assert 'app' in diff_a["spec"]["egress"][0]["to"][0]["podSelector"]["matchLabels"], "\r\nUse specific pod selectors to achieve least-privilege security or allow all ingress traffic within namespace to get started with simpler policy."
                else:
                    assert 'cidr' in diff_a["spec"]["egress"][0]["to"][0]["ipBlock"] , "\r\n- allow ingress from any endpoint only to specific pods \r\n- allow ingress from any endpoint only to any pods but only specific port(s) (e.g to port 80)\r\n- allow ingress from any endpoint only to any pod in the namespace"
                    assert 'ports' in diff_a["spec"]["egress"][0] , "\r\n- allow ingress from any endpoint only to specific pods \r\n- allow ingress from any endpoint only to any pods but only specific port(s) (e.g to port 80)\r\n- allow ingress from any endpoint only to any pod in the namespace"
        else:
            assert 'ingress' in diff_a["spec"] ,"\r\n After applying a deny-all policy which blocks all non-whitelisted traffic to the application, now you have to allow access to an application from all pods in the current namespace.\r\nApplying this policy makes any other policies restricting the traffic to the pod void, and allow all traffic to it from its namespace and other namespaces."
            assert 'egress' in diff_a["spec"] ,"\r\nTo achieve least-privilege security, consider one of the following options instead:\r\n- allow egress to specific CIDRs\r\n- allow egress to specific FQDNs\r\n- allow egress to any endpoint outside of the cluster"
    else:
        assert 'ingress' in diff_a["spec"] ,"\r\n After applying a deny-all policy which blocks all non-whitelisted traffic to the application, now you have to allow access to an application from all pods in the current namespace.\r\nApplying this policy makes any other policies restricting the traffic to the pod void, and allow all traffic to it from its namespace and other namespaces."
        assert 'egress' in diff_a["spec"] ,"\r\nTo achieve least-privilege security, consider one of the following options instead:\r\n- allow egress to specific CIDRs\r\n- allow egress to specific FQDNs\r\n- allow egress to any endpoint outside of the cluster"

def test_Egress_in_namespace():
    if 'egress' in diff_a['spec']:
        if diff_a['spec']['egress']: 
            if 'podSelector' in diff_a["spec"]["egress"][0]["to"][0]:
                if not 'k8s-app' in diff_a["spec"]["egress"][0]["to"][0]["podSelector"]["matchLabels"]:
                    assert 'app' in diff_a["spec"]["egress"][0]["to"][0]["podSelector"]["matchLabels"], "\r\nUse specific pod selectors to achieve least-privilege security or allow all ingress traffic within namespace to get started with simpler policy."
                    assert 'port' in diff_a["spec"]["egress"][0]["ports"][0],"\r\nUse specific pod selectors to achieve least-privilege security or allow all ingress traffic within namespace to get started with simpler policy."
    else:
        assert 'ingress' in diff_a["spec"] ,"\r\n After applying a deny-all policy which blocks all non-whitelisted traffic to the application, now you have to allow access to an application from all pods in the current namespace.\r\nApplying this policy makes any other policies restricting the traffic to the pod void, and allow all traffic to it from its namespace and other namespaces."
        assert 'egress' in diff_a["spec"] ,"\r\nTo achieve least-privilege security, consider one of the following options instead:\r\n- allow egress to specific CIDRs\r\n- allow egress to specific FQDNs\r\n- allow egress to any endpoint outside of the cluster"

def test_Egress_in_cluster():
    if 'egress' in diff_a['spec']:
        if diff_a['spec']['egress']: 
            if 'to' in diff_a["spec"]["egress"][0]:
                if 'namespaceSelector' in diff_a["spec"]["egress"][0]["to"][0]:
                    assert 'port' in diff_a["spec"]["egress"][0]["ports"][0], "\r\nIf pods in the namespace need to send egress to other pods in other namespaces, consider one of the following options:\r\n- allow egress only to selected namespaces\r\n- allow egress only to pods that match selected labels"
            if 'podSelector' in diff_a["spec"]["egress"][0]["to"][0]:
                if 'k8s-app' in diff_a["spec"]["egress"][0]["to"][0]["podSelector"]["matchLabels"]:
                    assert 'port' in diff_a["spec"]["egress"][0]["ports"][0],"\r\nUse specific pod selectors to achieve least-privilege security or allow all ingress traffic within namespace to get started with simpler policy."
    else:
        assert 'ingress' in diff_a["spec"] ,"\r\n After applying a deny-all policy which blocks all non-whitelisted traffic to the application, now you have to allow access to an application from all pods in the current namespace.\r\nApplying this policy makes any other policies restricting the traffic to the pod void, and allow all traffic to it from its namespace and other namespaces."
        assert 'egress' in diff_a["spec"] ,"\r\nTo achieve least-privilege security, consider one of the following options instead:\r\n- allow egress to specific CIDRs\r\n- allow egress to specific FQDNs\r\n- allow egress to any endpoint outside of the cluster"
