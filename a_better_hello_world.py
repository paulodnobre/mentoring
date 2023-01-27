import os
import sys

arguments = {
    "lang": None,
    "help": 1,
}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print("Invalid Option. Please run with --help=1 parameter to see more information")
        sys.exit()
    if key == "help":
        print("You must specify the --lang parameter and one of the following languages: en_US, pt_BR, it_IT, es_SP, fr_FR")
        sys.exit()
    arguments[key] = value

language = arguments["lang"]
if language is None:
    language = os.getenv("LANG", "en_US")

if language == "pt_BR":
    msg = "Olá, Mundo!"
elif language == "it_IT":
    msg = "Ciao, Mondo!"
elif language == "es_SP":
    msg = "Hola, Mundo!"
elif language == "ja_JP":
    msg = "こんにちは世界！"
else:
    msg = "Language not found. Please run with --help=1 parameter to see more information"

"""

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "ja_JP": "こんにちは世界！",

"""


print(msg)
# print(msg[current_language])

