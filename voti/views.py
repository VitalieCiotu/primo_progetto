from django.shortcuts import render

def index(request):
    return render(request, "indexVoti.html")

materie = ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]
def views_a(request):
    return render(request, "view_a.html", {"materie": materie})
#py manage.py startapp prima_app
voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
def views_b(request):
    return render(request, "view_b.html", {"voti":voti})

def views_c(request):
    a=()
    n=0
    medie={}
    for k, situazione in voti:
        for materia, voto in situazione:
            a.append(voto)
            n+=1
        media=sum(a)/n
        medie[k].append(media)
    
    return render(request, "view_c.html" ,{"medie":medie})