import lxml.etree as et

doc = et.parse('DATA/solar.xml')

root_tag = doc.getroot()

for section_tag in root_tag:
    if "planet" in section_tag.tag:
        for planet_tag in section_tag:
            print(planet_tag.get('planetname'))
            for moon_tag in planet_tag:
                print(f"  {moon_tag.text}")