import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "stambul65": {"points": 594, "booster": 2.0},
    "Conrad_Gagnon": {"points": 114, "booster": 1.6},
    "nopainogain": {"points": 102, "booster": None},
    "kubak5": {"points": 75, "booster": 1.9},
    "DarkOnCrack": {"points": 71, "booster": None},
    "ComeToBaba1": {"points": 65, "booster": 1.1},
    "mang0sunr1s3": {"points": 41, "booster": None},
    "Konariq7": {"points": 38, "booster": 1.8},
    "tadeasek532": {"points": 28, "booster": 1.7},
    "Satranc599": {"points": 19, "booster": None},
    "TheRuleBreaker122": {"points": 19, "booster": None},
    "matewasfate": {"points": 19, "booster": 1.4},
    "thedecentchescuber": {"points": 18, "booster": None},
    "TvojaLaska": {"points": 16, "booster": None},
    "yongzhengwang": {"points": 13, "booster": None},
    "Ozgur3838": {"points": 11, "booster": None},
    "schwarzerrabe": {"points": 10, "booster": None},
    "Justinsenpai": {"points": 9, "booster": None},
    "shailesh777": {"points": 8, "booster": None},
    "ZoTsihoarana": {"points": 7, "booster": None},
    "german11": {"points": 6, "booster": None},
    "LAFLAUTADORADA": {"points": 6, "booster": 1.5},
    "MysteryPhantom7": {"points": 5, "booster": None},
    "Atharv_2008": {"points": 4, "booster": None},
    "Gloria1959": {"points": 4, "booster": None},
    "Sotapana_ass": {"points": 4, "booster": None},
    "nikoforgione": {"points": 4, "booster": 1.3},
    "Entrenador3talentos": {"points": 4, "booster": 1.2},
    "Capi48": {"points": 3, "booster": None},
    "emiliocba": {"points": 3, "booster": None},
    "Pejton_bt": {"points": 3, "booster": None},
    "OneOfTheWorldsBest": {"points": 3, "booster": None},
    "healLan": {"points": 3, "booster": None},
    "kenedyKimutai": {"points": 2, "booster": None},
    "mrsst": {"points": 2, "booster": None},
    "SparkToBlack": {"points": 2, "booster": None},
    "sheun": {"points": 2, "booster": None},
    "Omabc": {"points": 2, "booster": None},
}


new_table_json = """
{"rank":1,"score":60,"rating":2425,"username":"stambul65","performance":2221}
{"rank":2,"score":15,"rating":1817,"username":"Conrad_Gagnon","performance":1982}
{"rank":3,"score":13,"rating":2083,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":1958}
{"rank":4,"score":10,"rating":1932,"username":"Pejton_bt","performance":2271}
{"rank":5,"score":9,"rating":1968,"username":"kubak5","performance":1997}
{"rank":6,"score":8,"rating":1452,"username":"schwarzerrabe","performance":1649}
{"rank":7,"score":7,"rating":1620,"username":"DarkOnWeakBot","title":"BOT","performance":1700}
{"rank":8,"score":4,"rating":1891,"username":"yonis1111","performance":1850}
{"rank":9,"score":3,"rating":1513,"username":"healLan","patronColor":7,"performance":1719}
{"rank":10,"score":3,"rating":2126,"username":"emiliocba","flair":"nature.pig-face","performance":1667}
{"rank":11,"score":1,"rating":2097,"username":"Konariq7","flair":"nature.glowing-star","patronColor":6,"performance":1615}
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
