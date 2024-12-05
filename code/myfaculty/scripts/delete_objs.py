from theses.models import Thesis

def run():
    for l in Thesis.objects.all():
        l.delete()