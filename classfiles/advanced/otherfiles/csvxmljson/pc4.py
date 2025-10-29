import xml.etree.ElementTree as ET


#root = ET.Element("employees")
#emp1 =ET.SubElement(root,"employee")
#ET.SubElement(emp1,"name").text ="Jhon"
#ET.SubElement(emp1,"age").text ="25"
#tree = ET.ElementTree(root)
#tree.write("output.xml")



tree = ET.parse('output.xml')
root = tree.getroot()

for emp in root.findall('employee'):
    print(emp.find('name').text)





