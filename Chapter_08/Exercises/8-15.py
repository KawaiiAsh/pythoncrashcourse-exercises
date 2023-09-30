import sys
sys.path.append('../') # Add the parent directory to the path

from printing_models import print_models
from printing_models import show_models

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_models(completed_models)