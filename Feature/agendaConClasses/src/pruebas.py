import xml.etree.cElementTree as ET
from xml.dom import minidom

root = ET.Element("Contactos")

doc = ET.SubElement(root, "Persona")
ET.SubElement(doc, "nombre").text = "nombre"
ET.SubElement(doc, "apellido").text = "apellido"
ET.SubElement(doc, "apodo").text = "apodo"
ET.SubElement(doc, "telefono").text = "#telefono"
ET.SubElement(doc, "Nombre").text = "Nombre"

archivo = ET.ElementTree(root)
archivo.write("xl.xml")
'''

xml=minidom.parse("xl.xml")
print(xml)
docs=xml.getElementsByTagName("doc")
print(docs)





        #docs=xml.getElementsByTagName("doc")
       # print(docs)
       # for doc in docs:
        #    nodo1=doc.getElementsByTagName("nodo1")[0]
        #    nodo2=doc.getElementsByTagName("nodo2")[0]
        #    print(f"nodo1={nodo1.firstChild.data}")

     #   input()
        #'''