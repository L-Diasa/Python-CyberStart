import xml.etree.cElementTree as ET

root = ET.Element("root")
ET.SubElement(root, "country", name="Narnia")
ET.SubElement(root, "country", name="Wakanda")
ET.SubElement(root, "country", name="Panama")
tree = ET.ElementTree(root)
tree.write("/tmp/vulnerable-countries.xml")
