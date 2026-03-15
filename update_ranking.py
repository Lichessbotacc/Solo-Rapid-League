import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "stambul65": {"points": 306, "booster": 2.0},
    "nopainogain": {"points": 91, "booster": 1.9},
    "Conrad_Gagnon": {"points": 52, "booster": 1.7},
    "DarkOnCrack": {"points": 51, "booster": 1.3},
    "mang0sunr1s3": {"points": 41, "booster": None},
    "ComeToBaba1": {"points": 29, "booster": None},
    "kubak5": {"points": 26, "booster": 1.2},
    "Satranc599": {"points": 19, "booster": None},
    "TheRuleBreaker122": {"points": 19, "booster": None},
    "Konariq7": {"points": 18, "booster": 1.6},
    "tadeasek532": {"points": 17, "booster": None},
    "thedecentchescuber": {"points": 15, "booster": 1.8},
    "yongzhengwang": {"points": 13, "booster": None},
    "matewasfate": {"points": 11, "booster": None},
    "schwarzerrabe": {"points": 10, "booster": 1.4},
    "TvojaLaska": {"points": 10, "booster": 1.5},
    "Ozgur3838": {"points": 9, "booster": None},
    "shailesh777": {"points": 8, "booster": None},
    "german11": {"points": 6, "booster": None},
    "MysteryPhantom7": {"points": 5, "booster": None},
    "Atharv_2008": {"points": 4, "booster": None},
    "Justinsenpai": {"points": 2, "booster": None},
    "kenedyKimutai": {"points": 2, "booster": None},
    "mrsst": {"points": 2, "booster": 1.1},
}


new_table_json = """
{"rank":1,"score":45,"rating":2342,"username":"stambul65","performance":2177}
{"rank":2,"score":33,"rating":2105,"username":"ComeToBaba1","flair":"objects.crown","performance":2206}
{"rank":3,"score":6,"rating":1787,"username":"Conrad_Gagnon","performance":1830}
{"rank":4,"score":4,"rating":2004,"username":"Gloria1959","flair":"travel-places.desert-island","performance":2169}
{"rank":5,"score":4,"rating":2023,"username":"Sotapana_ass","performance":1989}
{"rank":6,"score":3,"rating":2061,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":2288}
{"rank":7,"score":3,"rating":2286,"username":"Capi48","performance":1805}
{"rank":8,"score":3,"rating":2034,"username":"nopainogain","flair":"activity.chess-pawn","performance":1725}
{"rank":9,"score":3,"rating":2000,"username":"kubak5","performance":1602}
{"rank":10,"score":2,"rating":1786,"username":"thedecentchescuber","performance":2486}
{"rank":11,"score":2,"rating":2115,"username":"Konariq7","flair":"nature.glowing-star","patronColor":6,"performance":2212}
{"rank":12,"score":2,"rating":1983,"username":"SparkToBlack","flair":"activity.sparkler","performance":2039}
{"rank":13,"score":2,"rating":1976,"username":"sheun","flair":"activity.trophy","performance":1693}
{"rank":14,"score":2,"rating":1614,"username":"TvojaLaska","flair":"activity.heart-suit","performance":1668}
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
