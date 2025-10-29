import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root =tree.getroot()

print("roottag:",root.tag)
for emp in root.findall('employee'):
    emp_id =emp.get('id')
    name =emp.find('name').text
    position= emp.find('position').text
    print(f"ID:{emp_id},name:{name},Position:{position}")