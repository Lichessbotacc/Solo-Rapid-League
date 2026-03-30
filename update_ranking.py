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
{"rank":1,"score":41,"rating":2409,"username":"stambul65","performance":2323}
{"rank":2,"score":16,"rating":1990,"username":"kubak5","performance":1979}
{"rank":3,"score":13,"rating":2111,"username":"Konariq7","flair":"nature.glowing-star","patronColor":6,"performance":2239}
{"rank":4,"score":11,"rating":2205,"username":"tadeasek532","performance":2164}
{"rank":5,"score":8,"rating":1862,"username":"Conrad_Gagnon","performance":1921}
{"rank":6,"score":6,"rating":2093,"username":"LAFLAUTADORADA","flair":"objects.crossed-swords","performance":2067}
{"rank":7,"score":6,"rating":1642,"username":"matewasfate","performance":1813}
{"rank":8,"score":4,"rating":1628,"username":"nikoforgione","performance":2142}
{"rank":9,"score":4,"rating":2131,"username":"Entrenador3talentos","flair":"activity.chess-pawn","performance":1779}
{"rank":10,"score":3,"rating":2129,"username":"ComeToBaba1","flair":"objects.crown","performance":2136}
{"rank":11,"score":3,"rating":2054,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":1982}
{"rank":12,"score":3,"rating":1905,"username":"Pejton_bt","performance":1929}
{"rank":13,"score":3,"rating":1979,"username":"OneOfTheWorldsBest","flair":"symbols.white-flag","performance":1765}
{"rank":14,"score":3,"rating":1640,"username":"TvojaLaska","flair":"activity.heart-suit","performance":1708}
{"rank":15,"score":3,"rating":1497,"username":"healLan","patronColor":7,"performance":1613}
{"rank":16,"score":2,"rating":1951,"username":"Omabc","performance":2026}
{"rank":17,"score":1,"rating":1712,"username":"Justinsenpai","performance":1788}
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
