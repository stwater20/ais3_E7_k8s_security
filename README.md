# k8s pod network policy tools



By default, pods are non-isolated; they accept traffic from any source.

Pods become isolated by having a NetworkPolicy that selects them. Once there is any NetworkPolicy in a namespace selecting a particular pod, that pod will reject any connections that are not allowed by any NetworkPolicy. (Other pods in the namespace that are not selected by any NetworkPolicy will continue to accept all traffic.)

Network policies do not conflict; they are additive. If any policy or policies select a pod, the pod is restricted to what is allowed by the union of those policies' ingress/egress rules. Thus, order of evaluation does not affect the policy result.

For a network flow between two pods to be allowed, both the egress policy on the source pod and the ingress policy on the destination pod need to allow the traffic. If either the egress policy on the source, or the ingress policy on the destination denies the traffic, the traffic will be denied.


```

 _   ___                    _            _                  _               _ _           _            _    
| |_( _ )___  _ __  ___  __| |  _ _  ___| |___ __ _____ _ _| |__  _ __  ___| (_)__ _  _  | |_ ___  ___| |___
| / / _ (_-< | '_ \/ _ \/ _` | | ' \/ -_)  _\ V  V / _ \ '_| / / | '_ \/ _ \ | / _| || | |  _/ _ \/ _ \ (_-<
|_\_\___/__/ | .__/\___/\__,_| |_||_\___|\__|\_/\_/\___/_| |_\_\ | .__/\___/_|_\__|\_, |  \__\___/\___/_/__/
             |_|                                                 |_|               |__/                     
usage: k8spod.py [-h] [-i REQFILE]

optional arguments:
  -h, --help  show this help message and exit
  -i REQFILE  Pod Network Policy Request file

Examples:
    python k8spod.py -i test.yaml
    

```