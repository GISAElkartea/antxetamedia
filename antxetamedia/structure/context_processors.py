from antxetamedia.structure.models import Node

def nodes_on_menu(request):
    return {'nodes_on_menu': Node.objects.filter(on_menu=True)}

def root_nodes(request):
    return {'root_nodes': Node.objects.roots() }
