#!/usr/bin/env python3
"""Random Joke Generator CLI using icanhazdadjoke (primary) and Official Joke API (fallback).

Usage:
  python -m src.jokegen [-n N] [--source auto|ican|official]

"""

import argparse
import requests
import sys

ICAN_URL = "https://icanhazdadjoke.com/"
OFFICIAL_URL = "https://official-joke-api.appspot.com/random_joke"

HEADERS = {"Accept": "application/json", "User-Agent": "joke-generator/1.0 (+https://github.com/bhanuprakashyr)"}


def fetch_ican_joke():
    try:
        r = requests.get(ICAN_URL, headers=HEADERS, timeout=6)
        r.raise_for_status()
        data = r.json()
        return data.get("joke")
    except Exception:
        return None


def fetch_official_joke():
    try:
        r = requests.get(OFFICIAL_URL, timeout=6)
        r.raise_for_status()
        data = r.json()
        setup = data.get("setup")
        punch = data.get("punchline")
        if setup and punch:
            return f"{setup} — {punch}"
    except Exception:
        return None


def get_joke(prefer_source="auto"):
    if prefer_source == "ican":
        return fetch_ican_joke() or fetch_official_joke()
    if prefer_source == "official":
        return fetch_official_joke() or fetch_ican_joke()
    # auto
    return fetch_ican_joke() or fetch_official_joke()


def main():
    parser = argparse.ArgumentParser(description="Random joke generator (CLI)")
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of jokes to fetch")
    parser.add_argument("-s", "--source", choices=["auto", "ican", "official"], default="auto", help="Preferred joke source")
    args = parser.parse_args()

    for i in range(args.number):
        joke = get_joke(args.source)
        if joke:
            print(joke)
        else:
            print("Couldn't fetch a joke right now. Try again later.", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()