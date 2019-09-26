"""
File contains the properties of available Telugu Fonts as a dictionary.
Fields:
    Font Name
    Required Letter Spacing (Single/Double)
    Abbreviation
    Has Bold
"""

SIZE, SPACING, BOLD, ABBR, = range(4)
font_properties = {
'ARIALUNI':               [48, 1, 1, 1, 'Vemana',  ],
}

font_properties_list = list(font_properties.items())

import random


def random_font():
    font, properties = random.choice(font_properties_list)
    style = random.randrange(4 if properties[BOLD] else 2)

    return font, properties[SIZE], style


if __name__ == '__main__':
    from gi.repository import PangoCairo

    font_map = PangoCairo.font_map_get_default()
    families = font_map.list_families()
    font_names = [f.get_name() for f in families]

    for f in sorted(font_names):
        if f in font_properties:
            print('\n{}{}'.format(f, font_properties[f]))
        else:
            print("[X]{}".format(f), end='\t')

    print()
    for f in sorted(font_properties.keys()):
        if f in font_names:
            print("[✓]{}".format(font_properties[f][ABBR]), end=' ')
        else:
            print("\n[!]{} NOT INSTALLED".format(f))
