#!/usr/bin/env python3

from jinja2 import Environment, PackageLoader, select_autoescape
import requests


def main():
    list_catfacts_url: str = "https://catfact.ninja/facts?limit=10"
    catfacts = get_facts(list_catfacts_url)
    print(catfacts)


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
