from pathlib import Path
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup as Soup
from collections import defaultdict

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"


class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """

    levels = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,
              'VIII':8,'IX':9,'X':10}
    
    def __init__(self, id_name, name, max_level, description):
        self.id_name = id_name
        self.name = name
        self.max_level = self.levels.get(max_level) if max_level in self.levels else max_level
        self.description = description
        self.items = []

    def __str__(self):
        return f'{self.name} ({self.max_level}): {self.description}'



class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """

    def __init__(self, name):
        self.name = name
        self.enchantments = []
        
    def __str__(self):
        new_name = ''
        if '_' in self.name:
            new_name = self.name.replace('_',' ')
            new_name = new_name.title()
        else:
            new_name = self.name.title()
        out = [f'{new_name}: ']
        e_list =[]
        for e in self.enchantments:
            e_list.append((e.id_name, e.max_level))
        e_list = sorted(e_list, key=lambda x:x[0])
        for e in e_list:
            out.append(f'  [{e[1]}] {e[0]}')
        return '\n'.join(out)


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    items_regex = re.compile(r'\/([a-zA-Z_]+?)(sm)*\.png',re.I)
    name_regex = re.compile(r'^(.*)\((.*)\)')
    table = soup.find_all('table')[0]
    new_dict = {}
    for row in table.find_all('tr'):
        if row:
            columns = row.find_all('td')
            id_name = ''
            name = ''
            max_level = 1
            description = ''
            items_list = []
            for i, column in enumerate(columns):
                if column.find('img'):
                    items = items_regex.search(column.find('img')['data-src']).group(1)
                    items_list = items.split('_')
                    if 'enchanted' in items_list:
                        items_list.remove('enchanted')
                    if 'iron' in items_list:
                        items_list.remove('iron')
                    if 'fishing' in items_list and 'rod' in items_list:
                        idx = items_list.index('fishing')
                        items_list.remove('fishing')
                        items_list.remove('rod')
                        items_list.insert(idx,'fishing_rod')
                elif column.text:
                    if i == 0:
                        # name and id_name
                        if name_regex.search(column.text):
                            names_match = name_regex.search(column.text)
                            name = names_match.group(1).strip()
                            id_name = names_match.group(2).strip()
                    elif i == 1:
                        # max_level
                        max_level = column.text.strip()
                    elif i == 2:
                        # description
                        description = column.text.strip()
            if id_name:
                new_dict[id_name] = Enchantment(id_name=id_name, name=name, max_level=max_level, description=description)
                for item in items_list:
                    new_dict[id_name].items.append(item)
    return new_dict


def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    n_dict = defaultdict(list)
    for ename, enchantment in data.items():
        for item in enchantment.items:
            n_dict[item].append(enchantment)
    item_dict = {}
    for k, v in n_dict.items():
        item_dict[k] = Item(name=k)
        item_dict[k].enchantments.extend(v)
    return item_dict


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""