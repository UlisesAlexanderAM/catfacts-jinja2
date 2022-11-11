#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader, select_autoescape, Template
import requests


def main():
    list_catfacts_url: str = "https://catfact.ninja/facts?limit=10"
    catfacts = get_facts(list_catfacts_url)
    template = generate_template("templates", "catfacts.html")
    print(render_template(catfacts, template))


def render_template(catfacts: list, template: Template) -> str:
    return template.render(list=catfacts)


def generate_template(file_system: str, template: str) -> Template:
    env = Environment(loader=FileSystemLoader(file_system), autoescape=select_autoescape())
    template = env.get_template(template)
    return template


def get_facts(url: str) -> list:
    list_catfacts_url: str = url
    request_catfacts = requests.get(url=list_catfacts_url)
    catfacts_json = request_catfacts.json()
    data_catfacts = catfacts_json["data"]
    catfacts = []
    for facts in data_catfacts:
        catfacts.append(facts["fact"])

    return catfacts


if __name__ == '__main__':
    main()
