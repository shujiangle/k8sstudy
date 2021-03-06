from django.shortcuts import render
from kubernetes import config, dynamic
from kubernetes.client import api_client


# Create your views here.


def hostinfor(request):
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # fetching the node api
    api = client.resources.get(api_version="v1", kind="Node")

    # Listing cluster nodes

    # print("%s\t\t%s\t\t%s" % ("NAME", "STATUS", "VERSION"))
    # nodes = []
    node1 = []
    node2 = []
    node3 = []
    for item in api.get().items:
        node = api.get(name=item.metadata.name)
        node1.append(node.metadata.name)
        node2.append(node.status.conditions[3]["reason"])
        node3.append(node.status.nodeInfo.kubeProxyVersion)
        # nodes.append(node)
        # print(node)
        # print(
        #     "%s\t%s\t\t%s\n"
        #     % (
        #         node.metadata.name,
        #         node.status.conditions[3]["type"],
        #         node.status.nodeInfo.kubeProxyVersion,
        #     )
        # )
    nodes = zip(node1, node2, node3)
    return render(request, 'k8sshost/hostinfor.html', locals())


def pods(request):
    from kubernetes import client, config
    config.load_kube_config()

    v1 = client.CoreV1Api()
    # print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    rets = ret.items
    # for i in ret.items:
    #     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    return render(request, 'k8sshost/pods.html', locals())


def dashboard(request):
    return render(request, 'k8sshost/dashboard.html', locals())









