import lxml.etree as et

root_tag = et.Element("knights")

with open('DATA/knights.txt') as knights_in:
    for  raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(":")
        knight_tag = et.SubElement(root_tag, "knight", title=title)
        et.SubElement(knight_tag, "name").text = name
        color_tag = et.SubElement(knight_tag, "color")
        color_tag.text = color
        et.SubElement(knight_tag, "quest").text = quest
        et.SubElement(knight_tag, "comment").text = comment


xml_doc = et.tostring(root_tag, xml_declaration=True, pretty_print=True).decode()
print(xml_doc)

doc = et.ElementTree(root_tag)
doc.write("knight_info.xml", xml_declaration=True, pretty_print=True)
