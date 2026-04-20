import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "stambul65": {"points": 714, "booster": 2.0},
    "Conrad_Gagnon": {"points": 138, "booster": 1.9},
    "nopainogain": {"points": 102, "booster": None},
    "kubak5": {"points": 92, "booster": 1.6},
    "DarkOnCrack": {"points": 84, "booster": 1.8},
    "ComeToBaba1": {"points": 65, "booster": None},
    "mang0sunr1s3": {"points": 41, "booster": None},
    "Konariq7": {"points": 39, "booster": None},
    "tadeasek532": {"points": 28, "booster": None},
    "Satranc599": {"points": 19, "booster": None},
    "TheRuleBreaker122": {"points": 19, "booster": None},
    "matewasfate": {"points": 19, "booster": None},
    "thedecentchescuber": {"points": 18, "booster": None},
    "schwarzerrabe": {"points": 18, "booster": 1.5},
    "TvojaLaska": {"points": 16, "booster": None},
    "yongzhengwang": {"points": 13, "booster": None},
    "Pejton_bt": {"points": 13, "booster": 1.7},
    "Ozgur3838": {"points": 11, "booster": None},
    "Justinsenpai": {"points": 9, "booster": None},
    "shailesh777": {"points": 8, "booster": None},
    "ZoTsihoarana": {"points": 7, "booster": None},
    "DarkOnWeakBot": {"points": 7, "booster": 1.4},
    "german11": {"points": 6, "booster": None},
    "LAFLAUTADORADA": {"points": 6, "booster": None},
    "emiliocba": {"points": 6, "booster": 1.1},
    "healLan": {"points": 6, "booster": 1.2},
    "MysteryPhantom7": {"points": 5, "booster": None},
    "Atharv_2008": {"points": 4, "booster": None},
    "Gloria1959": {"points": 4, "booster": None},
    "Sotapana_ass": {"points": 4, "booster": None},
    "nikoforgione": {"points": 4, "booster": None},
    "Entrenador3talentos": {"points": 4, "booster": None},
    "yonis1111": {"points": 4, "booster": 1.3},
    "Capi48": {"points": 3, "booster": None},
    "OneOfTheWorldsBest": {"points": 3, "booster": None},
    "kenedyKimutai": {"points": 2, "booster": None},
    "mrsst": {"points": 2, "booster": None},
    "SparkToBlack": {"points": 2, "booster": None},
    "sheun": {"points": 2, "booster": None},
    "Omabc": {"points": 2, "booster": None},
}


new_table_json = """
{"rank":1,"score":42,"rating":2426,"username":"stambul65","performance":2090}
{"rank":2,"score":12,"rating":1833,"username":"Conrad_Gagnon","performance":1858}
{"rank":3,"score":9,"rating":1591,"username":"okoh11122233","flair":"smileys.winking-face-with-tongue","performance":1973}
{"rank":4,"score":5,"rating":1647,"username":"DarkOnWeakBot","title":"BOT","performance":1807}
{"rank":5,"score":0,"rating":2123,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5}
{"rank":6,"score":0,"rating":1601,"username":"jash_the_goat","flair":"smileys.alien"}
{"rank":7,"score":0,"rating":1600,"username":"abdulJahangirov"}
{"rank":8,"score":0,"rating":1446,"username":"schwarzerrabe","performance":1337}
{"rank":9,"score":0,"rating":1312,"username":"Shaurya1718"}
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
