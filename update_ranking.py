import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "stambul65": {"points": 396, "booster": 2.0},
    "nopainogain": {"points": 96, "booster": 1.3},
    "Conrad_Gagnon": {"points": 62, "booster": 1.8},
    "ComeToBaba1": {"points": 62, "booster": 1.9},
    "DarkOnCrack": {"points": 54, "booster": 1.5},
    "mang0sunr1s3": {"points": 41, "booster": None},
    "kubak5": {"points": 29, "booster": 1.2},
    "Konariq7": {"points": 21, "booster": None},
    "Satranc599": {"points": 19, "booster": None},
    "TheRuleBreaker122": {"points": 19, "booster": None},
    "thedecentchescuber": {"points": 18, "booster": 1.1},
    "tadeasek532": {"points": 17, "booster": None},
    "yongzhengwang": {"points": 13, "booster": None},
    "TvojaLaska": {"points": 13, "booster": None},
    "matewasfate": {"points": 11, "booster": None},
    "schwarzerrabe": {"points": 10, "booster": None},
    "Ozgur3838": {"points": 9, "booster": None},
    "shailesh777": {"points": 8, "booster": None},
    "german11": {"points": 6, "booster": None},
    "MysteryPhantom7": {"points": 5, "booster": None},
    "Atharv_2008": {"points": 4, "booster": None},
    "Gloria1959": {"points": 4, "booster": 1.7},
    "Sotapana_ass": {"points": 4, "booster": 1.6},
    "Capi48": {"points": 3, "booster": 1.4},
    "Justinsenpai": {"points": 2, "booster": None},
    "kenedyKimutai": {"points": 2, "booster": None},
    "mrsst": {"points": 2, "booster": None},
    "SparkToBlack": {"points": 2, "booster": None},
    "sheun": {"points": 2, "booster": None},
}


new_table_json = """
{"rank":1,"score":58,"rating":2391,"username":"stambul65","performance":2368}
{"rank":2,"score":21,"rating":1848,"username":"Conrad_Gagnon","performance":2096}
{"rank":3,"score":15,"rating":1987,"username":"kubak5","performance":1950}
{"rank":4,"score":8,"rating":2053,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":2036}
{"rank":5,"score":7,"rating":1793,"username":"ZoTsihoarana","flair":"symbols.peace-symbol","performance":1847}
{"rank":6,"score":6,"rating":1713,"username":"Justinsenpai","performance":1698}
{"rank":7,"score":5,"rating":2036,"username":"nopainogain","flair":"activity.chess-pawn","performance":1929}
{"rank":8,"score":3,"rating":2127,"username":"emiliocba","flair":"nature.pig-face","performance":1832}
{"rank":9,"score":2,"rating":2103,"username":"Konariq7","flair":"nature.glowing-star","patronColor":6,"performance":2043}
{"rank":10,"score":2,"rating":1630,"username":"matewasfate","performance":1805}
{"rank":11,"score":2,"rating":1455,"username":"Ozgur3838","performance":1644}
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
