import datetime

eingabe = input("Wann willst du aufstehen? (HH:MM): ")

# 1. ":" prüfen
if ":" not in eingabe:
    print("Format muss HH:MM sein")
    exit()

# 2. split
teile = eingabe.split(":")

# 3. Länge prüfen (2 Teile)
if len(teile) != 2:
    print("Format muss HH:MM sein")
    exit()

stunde_str, minute_str = teile

# 4. Länge der einzelnen Teile prüfen (HH und MM)
if len(stunde_str) != 2 or len(minute_str) != 2:
    print("Format muss HH:MM sein")
    exit()

# 5. Zahlen prüfen
if not stunde_str.isdigit() or not minute_str.isdigit():
    print("Nur Zahlen erlaubt")
    exit()

# 6. Umwandeln
stunde = int(stunde_str)
minute = int(minute_str)

# 7. Bereich prüfen
if not (0 <= stunde <= 23 and 0 <= minute <= 59):
    print("Ungültige Uhrzeit")
    exit()

# 8. aktuelle Zeit
jetzt = datetime.datetime.now()

# 9. Aufstehzeit bauen
aufstehen = datetime.datetime(
    jetzt.year,
    jetzt.month,
    jetzt.day,
    stunde,
    minute
)

# 10. ggf. morgen
if aufstehen <= jetzt:
    aufstehen += datetime.timedelta(days=1)

# 11. Differenz berechnen
schlafdauer = aufstehen - jetzt

sekunden = int(schlafdauer.total_seconds())
stunden = sekunden // 3600
minuten = (sekunden % 3600) // 60

# 12. Ausgabe
print("Du kannst", stunden, "Stunden und", minuten, "Minuten schlafen")
