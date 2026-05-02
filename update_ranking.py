import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "stambul65": {"points": 968, "booster": 2.0},
    "Conrad_Gagnon": {"points": 210, "booster": 1.6},
    "nopainogain": {"points": 102, "booster": None},
    "kubak5": {"points": 95, "booster": None},
    "DarkOnCrack": {"points": 88, "booster": None},
    "ComeToBaba1": {"points": 74, "booster": 1.2},
    "Konariq7": {"points": 46, "booster": None},
    "mang0sunr1s3": {"points": 41, "booster": None},
    "DarkOnWeakBot": {"points": 35, "booster": 1.4},
    "Capi48": {"points": 30, "booster": 1.9},
    "okoh11122233": {"points": 29, "booster": 1.1},
    "tadeasek532": {"points": 28, "booster": None},
    "DAW8718": {"points": 28, "booster": 1.5},
    "Evgeny86": {"points": 27, "booster": 1.8},
    "schwarzerrabe": {"points": 23, "booster": None},
    "Ozgur3838": {"points": 23, "booster": 1.3},
    "xdxdboxjaja": {"points": 22, "booster": 1.7},
    "Satranc599": {"points": 19, "booster": None},
    "TheRuleBreaker122": {"points": 19, "booster": None},
    "matewasfate": {"points": 19, "booster": None},
    "thedecentchescuber": {"points": 18, "booster": None},
    "TvojaLaska": {"points": 16, "booster": None},
    "yongzhengwang": {"points": 13, "booster": None},
    "Pejton_bt": {"points": 13, "booster": None},
    "Justinsenpai": {"points": 9, "booster": None},
    "shailesh777": {"points": 8, "booster": None},
    "ZoTsihoarana": {"points": 7, "booster": None},
    "german11": {"points": 7, "booster": None},
    "LAFLAUTADORADA": {"points": 6, "booster": None},
    "emiliocba": {"points": 6, "booster": None},
    "healLan": {"points": 6, "booster": None},
    "MysteryPhantom7": {"points": 5, "booster": None},
    "longsonicc": {"points": 5, "booster": None},
    "timothyemmanuel": {"points": 5, "booster": None},
    "Atharv_2008": {"points": 4, "booster": None},
    "Gloria1959": {"points": 4, "booster": None},
    "Sotapana_ass": {"points": 4, "booster": None},
    "nikoforgione": {"points": 4, "booster": None},
    "Entrenador3talentos": {"points": 4, "booster": None},
    "yonis1111": {"points": 4, "booster": None},
    "Dede321": {"points": 4, "booster": None},
    "OneOfTheWorldsBest": {"points": 3, "booster": None},
    "GeekingKing": {"points": 3, "booster": None},
    "kenedyKimutai": {"points": 2, "booster": None},
    "mrsst": {"points": 2, "booster": None},
    "SparkToBlack": {"points": 2, "booster": None},
    "sheun": {"points": 2, "booster": None},
    "Omabc": {"points": 2, "booster": None},
    "sxantiago_chess": {"points": 2, "booster": None},
}

new_table_json = """
{"rank":1,"score":41,"rating":2398,"username":"stambul65","performance":2233}
{"rank":2,"score":27,"rating":2266,"username":"Capi48","performance":2164}
{"rank":3,"score":27,"rating":2204,"username":"Evgeny86","performance":1994}
{"rank":4,"score":22,"rating":2286,"username":"xdxdboxjaja","performance":2414}
{"rank":5,"score":16,"rating":1819,"username":"Conrad_Gagnon","performance":1928}
{"rank":6,"score":16,"rating":1888,"username":"DAW8718","performance":1907}
{"rank":7,"score":15,"rating":1639,"username":"DarkOnWeakBot","title":"BOT","performance":1691}
{"rank":8,"score":12,"rating":1548,"username":"Ozgur3838","performance":1767}
{"rank":9,"score":9,"rating":2101,"username":"ComeToBaba1","flair":"objects.crown","performance":1919}
{"rank":10,"score":6,"rating":1617,"username":"okoh11122233","flair":"smileys.winking-face-with-tongue","performance":1769}
{"rank":11,"score":5,"rating":1426,"username":"timothyemmanuel","performance":1602}
{"rank":12,"score":4,"rating":1909,"username":"Dede321","flair":"objects.chart-increasing","performance":1973}
{"rank":13,"score":4,"rating":2101,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":6,"performance":1837}
{"rank":14,"score":3,"rating":1961,"username":"kubak5","performance":1956}
{"rank":15,"score":3,"rating":1750,"username":"GeekingKing","performance":1914}
{"rank":16,"score":2,"rating":2071,"username":"Konariq7","flair":"nature.glowing-star","patronColor":6,"performance":1555}
{"rank":17,"score":1,"rating":1340,"username":"german11","patronColor":10,"performance":1409}
"""

# =========================
# APPLY SCORES (OLD BOOSTERS APPLY ONCE)
# =========================

new_table = []

for line in new_table_json.strip().splitlines():
    line = line.strip()
    if not line:
        continue
    new_table.append(json.loads(line))


for entry in new_table:
    username = entry["username"]
    score = entry["score"]

    if username not in current_ranking:
        current_ranking[username] = {"points": 0, "booster": None}

    booster = current_ranking[username]["booster"]
    if booster:
        score = int(score * booster)

    current_ranking[username]["points"] += score

# =========================
# RESET ALL BOOSTERS
# =========================

for user in current_ranking:
    current_ranking[user]["booster"] = None

# =========================
# ASSIGN NEW BOOSTERS TO TOP 10
# =========================

booster_levels = [2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1]

new_table_sorted = sorted(new_table, key=lambda x: x["score"], reverse=True)

for i in range(min(10, len(new_table_sorted))):
    current_ranking[new_table_sorted[i]["username"]]["booster"] = booster_levels[i]

# =========================
# SORT FINAL RANKING
# =========================

sorted_ranking = sorted(
    current_ranking.items(),
    key=lambda x: x[1]["points"],
    reverse=True
)

# =========================
# OUTPUT
# =========================

for rank, (username, data) in enumerate(sorted_ranking, start=1):
    booster_str = f" ({data['booster']}x boost next arena)" if data["booster"] else ""
    print(f"{rank}. @{username}: {data['points']}{booster_str}")

print("\n# ===== COPY FOR NEXT ARENA =====\n")
print("current_ranking = {")
for username, data in sorted_ranking:
    booster = data["booster"]
    booster_str = booster if booster else "None"
    print(f'    "{username}": {{"points": {data["points"]}, "booster": {booster_str}}},')
print("}")
