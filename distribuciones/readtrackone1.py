#! /usr/bin/env python
# Para usar este programa debe escribir en una consola ./readtrackone1.py numeroparticulas particulaseleccionada numerovueltas vueltaseleccionada nombrebpm
#ejemplo:  ./readtrackone1.py 100 1 10 1 BPM.29R1.B1

import sys
#funcion para asignarle un numero a cada bpm
def asignarnumero (nombrebpm):
    for m in bpmlist:
        nombrelinea = 'place="'+ str(nombrebpm)+ '";'
        if(nombrelinea in m):
            numerobpm = m[2]
            return numerobpm
        # else:
        #print "no se hallo el bpm"

#funcion que da z pz, s y mas
def pxpy (ipart,ivuelta,ibpm):
    cipart = int(ipart)
    civuelta = int(ivuelta)
    cibpm = int(ibpm)
    for line in allreadings:
        #print line[0], line[1], line[11]
        if((cipart == int(line[0])) and (civuelta == int(line[1])) and (cibpm == int(line[11]))):
            #  print line[0], line[1], line[11]
            x =line[2]
            px =line[3]
            bpmnom = line[10]
            s = line[8]
            return [bpmnom,s,cipart,civuelta,cibpm,x,px]
    

        #Inicio del programa
inputfile="trackone" # Archivo de entrada del programa y salida de madx
bpmfile="../bpmlist.madx" #Archivo de bpms
felipse = "elipse.dat"
fdistrib = "distribout.dat"
forbita = "orbita.dat"


npart = int(sys.argv[1]) #numero de particulas en la simulacion
npartsel =  int(sys.argv[2])
nturns = int(sys.argv[3]) #numero de vueltas simuladas
nturnsel=int(sys.argv[4])  #vuelta seleccionada para dibujar la distribucion              
bpmname= sys.argv[5]      #nombre del bpm

                          
bpmf = open(bpmfile,'r') #Se abre el archivo de Bpms del acelerador
pfe = open(felipse,'w')
pfd = open(fdistrib,'w')
pfo = open(forbita,'w')
tracks = open(inputfile,'r')
nb = 0 #Contador de bpms arranca en cero

#Llena bpmlist con nombre de bpm y su correspondiente indice de acuerdo a bpmlist.madx
bpmlist = []
for line in bpmf:
    sline = line.split(None)
    nb = nb +1
    bpmline = sline
    bpmline.append(nb)
    #print bpmline
    bpmlist.append(bpmline)
    bpmnumber = asignarnumero(bpmname)
    #print bpmnumber


       #Se avanza en la lectura de trackone hasta el primer segment

line = tracks.readline()
sline = line.split(None)
while (not('#segment' in sline)):
 line = tracks.readline()
 sline = line.split(None)
 #Se ignoran las lecturas del punto start
for jp in range(1,npart+1):
 line = tracks.readline()
 sline = line.split(None)

 #La informacion de trackone es guardada en allreadings anadiendo nombre y numero de bpm
allreadings = []
for line in tracks:
 sline = line.split(None)
 #print sline
 if('#segment' in sline):
     bpmname =sline[5]
 else:
     singleline = sline
     singleline.append(bpmname)
     singleline.append(str(asignarnumero(bpmname)))
     allreadings.append(singleline)
     #print singleline
     #lineabpms = 'PTC_OBSERVE, place="'+singleline[10]+'";'
     #print lineabpms
     #print allreadings     
#La informacion en allreadings es leida y seleccionada por la funcion pxpy
#pxpy (particula,vuelta,bpm)
#./readtrack.py numeroparticulas numerovueltas     


#Se escoge una particula, se escoge un bpm y se deja variar el numero de vueltas
#Esto sirve para hacer las elipses de fase que describe una particula vuelta tras vuelta
#Ejemplo de ejecucion ./readtrackone1.py 1 1 100 1  BPM.29R1.B1 Para este caso el archivo madx debe simular una particula por 100 vueltas y observarlo en BPM.29R1.B1

#for vueltas in range(1,nturns+1):
#    [bpmnom,s,ppart,vvuelta,bbpm,x,px] =  pxpy(npartsel,vueltas,bpmnumber)
#    print >>pfe, x,px,s



#Se escoge una vuelta, un bpm y se hace para npart particulas
#Esto sirve para dibujar la posicion que todas las particulas ocupan en el espacio de fase en una vuelta.
#Ejemplo de ejecucion ./readtrackone1.py 500 1 5 1 BPM.29R1.B1    Para este caso el archivo madx debe simular 500 particulas por 5 vueltas  observarlo en un bpm. La vuelta de
#observacion escogida por readtrackone1.py es en este caso la vuelta 1    

for nnpart in range(1,npart+1):
     [bpmnom,s,ppart,vvuelta,bbpm,x,px] =  pxpy(nnpart,nturnsel,bpmnumber)
     print >>pfd, x,px



#Se escoge una vuelta, una particula y se usan todos los bpms del acelerador
#Sirve para dibujar la orbita de la particula en el acelerador.
#Ejemplo de ejecucion  ./readtrackone1.py 500 3 1 1 BPM.29R1.B1   Para este caso el archivo madx debe simular 500 particulas por 1 vuelta y observarla en todos los bpms. 
#La particula escogiada por readtrackone1.py en este caso es la 3

    
#for nbpm in range(1,nb):
#     [bpmnom,s,ppart,vvuelta,bbpm,x,px] =  pxpy(npartsel,nturnsel,nbpm) 
#     print >>pfo, s, x
  

