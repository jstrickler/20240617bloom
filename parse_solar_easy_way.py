import lxml.etree as et

doc = et.parse('DATA/solar.xml')

for planet_tag in doc.findall('.//planet'):    
    print(planet_tag.get('planetname'))
    for moon_tag in planet_tag.findall('moon'):
        print(f"  {moon_tag.text}")