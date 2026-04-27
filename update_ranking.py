import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "stambul65": {"points": 798, "booster": 2.0},
    "Conrad_Gagnon": {"points": 160, "booster": 1.9},
    "nopainogain": {"points": 102, "booster": None},
    "kubak5": {"points": 92, "booster": None},
    "DarkOnCrack": {"points": 84, "booster": 1.6},
    "ComeToBaba1": {"points": 65, "booster": None},
    "mang0sunr1s3": {"points": 41, "booster": None},
    "Konariq7": {"points": 39, "booster": None},
    "tadeasek532": {"points": 28, "booster": None},
    "Satranc599": {"points": 19, "booster": None},
    "TheRuleBreaker122": {"points": 19, "booster": None},
    "matewasfate": {"points": 19, "booster": None},
    "thedecentchescuber": {"points": 18, "booster": None},
    "schwarzerrabe": {"points": 18, "booster": 1.3},
    "TvojaLaska": {"points": 16, "booster": None},
    "DarkOnWeakBot": {"points": 14, "booster": 1.7},
    "yongzhengwang": {"points": 13, "booster": None},
    "Pejton_bt": {"points": 13, "booster": None},
    "Ozgur3838": {"points": 11, "booster": None},
    "Justinsenpai": {"points": 9, "booster": None},
    "okoh11122233": {"points": 9, "booster": 1.8},
    "shailesh777": {"points": 8, "booster": None},
    "ZoTsihoarana": {"points": 7, "booster": None},
    "german11": {"points": 6, "booster": None},
    "LAFLAUTADORADA": {"points": 6, "booster": None},
    "emiliocba": {"points": 6, "booster": None},
    "healLan": {"points": 6, "booster": None},
    "MysteryPhantom7": {"points": 5, "booster": None},
    "Atharv_2008": {"points": 4, "booster": None},
    "Gloria1959": {"points": 4, "booster": None},
    "Sotapana_ass": {"points": 4, "booster": None},
    "nikoforgione": {"points": 4, "booster": None},
    "Entrenador3talentos": {"points": 4, "booster": None},
    "yonis1111": {"points": 4, "booster": None},
    "Capi48": {"points": 3, "booster": None},
    "OneOfTheWorldsBest": {"points": 3, "booster": None},
    "kenedyKimutai": {"points": 2, "booster": None},
    "mrsst": {"points": 2, "booster": None},
    "SparkToBlack": {"points": 2, "booster": None},
    "sheun": {"points": 2, "booster": None},
    "Omabc": {"points": 2, "booster": None},
    "jash_the_goat": {"points": 0, "booster": 1.5},
    "abdulJahangirov": {"points": 0, "booster": 1.4},
    "Shaurya1718": {"points": 0, "booster": 1.2},
}

new_table_json = """
{"rank":1,"score":44,"rating":2413,"username":"stambul65","performance":2299}
{"rank":2,"score":11,"rating":1816,"username":"Conrad_Gagnon","performance":1996}
{"rank":3,"score":6,"rating":1622,"username":"okoh11122233","flair":"smileys.winking-face-with-tongue","performance":1895}
{"rank":4,"score":5,"rating":2157,"username":"longsonicc","performance":1957}
{"rank":5,"score":4,"rating":2092,"username":"Konariq7","flair":"nature.glowing-star","patronColor":6,"performance":2233}
{"rank":6,"score":4,"rating":1901,"username":"DAW8718","performance":1735}
{"rank":7,"score":4,"rating":1448,"username":"schwarzerrabe","performance":1592}
{"rank":8,"score":2,"rating":1375,"username":"sxantiago_chess","performance":1952}
{"rank":9,"score":2,"rating":1650,"username":"DarkOnWeakBot","title":"BOT","performance":1464}
{"rank":10,"score":0,"rating":2116,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":6}
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
