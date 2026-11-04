#!/home/<ut_kasutajanimi>/.venv/bin/python3
# TODO: Enne veebilehe ülesseadmist panna õige kasutajanimi.

import os         

method = os.environ.get("REQUEST_METHOD", "")

if method != "GET":
    print("Status: 405 Method Not Allowed")
    print("Allow: GET")
    print("Content-Type: text/html; charset=utf-8")
    print()
    print("<h1>405 Method Not Allowed</h1>")
else:
    print("Status: 200 OK")
    print("Content-Type: text/html; charset=utf-8")
    print()
    print("<h1>Backend is running!</h1>")
