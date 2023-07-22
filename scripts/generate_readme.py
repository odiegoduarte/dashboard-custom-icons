#!/usr/bin/python3
#
# Autor:      Diego Duarte 2023
# Projeto:    https://github.com/odiegoduarte/dashboard-custom-icons
#

from dataclasses import dataclass
from pathlib import Path

DASHBOARDS = [
    {"name": "Heimdall", "url": "https://github.com/linuxserver/Heimdall"},
    {"name": "Dashy", "url": "https://github.com/Lissy93/dashy"},
    {"name": "Homer", "url": "https://github.com/bastienwirtz/homer"},
    {"name": "Flame", "url": "https://github.com/pawelmalak/flame"},
    {"name": "Organizr", "url": "https://github.com/causefx/Organizr"},
    {"name": "Homarr", "url": "https://github.com/ajnart/homarr"},
    {"name": "Homepage", "url": "https://github.com/benphelps/homepage"}
]

def generate_img_tag(file):
    return f'<img src="png/{file.name}" alt="{file.stem}" width="50">'

def main():
    try:
        imgs = sorted(Path("../png").glob("*.png"))
        img_tags = [generate_img_tag(x) for x in imgs]

        with open("README.md", "wt", encoding="UTF-8") as f:
            f.write("<br><br>\n\n")
            f.write("![Logo](/assets/dashboardcustomicons.png)")
            f.write("\n\n")
            f.write("<br><br> \n\n")
            f.write("### Dashboards self-hosted:\n\n")
            for dashboard in DASHBOARDS:
                f.write(f"- [{dashboard['name']}]({dashboard['url']})\n")
            f.write("\n\n")
            f.write("<br><br> \n\n")
            f.write(" ".join(img_tags))
            f.write("\n\n")
            f.write("<br><br> \n\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()