
tarjeta = Element("tarjetas")
monitor = Element("monitores")
memoria = Element("memorias")
case = Element("cases")
teclado = Element("teclados")
mouse = Element("mouses")
audifono = Element("audifonos")

output1 = Element("output1")

def calcular(*args, **kwargs):
    totalsuma = float(tarjeta.value)+ float(monitor.value)+ float(memoria.value)+ float(case.value)+ float(teclado.value)+ float(mouse.value)+ float(audifono.value)
    output1.write("{0:.2f}".format(totalsuma))
    