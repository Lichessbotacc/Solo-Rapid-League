import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "stambul65": {"points": 62, "booster": 2.0},
    "mang0sunr1s3": {"points": 38, "booster": 1.9},
    "kubak5": {"points": 23, "booster": 1.8},
    "DarkOnCrack": {"points": 21, "booster": 1.7},
    "nopainogain": {"points": 20, "booster": 1.6},
    "Satranc599": {"points": 19, "booster": 1.5},
    "TheRuleBreaker122": {"points": 19, "booster": 1.4},
    "tadeasek532": {"points": 17, "booster": 1.3},
    "Conrad_Gagnon": {"points": 15, "booster": 1.2},
    "yongzhengwang": {"points": 13, "booster": 1.1},
    "ComeToBaba1": {"points": 9, "booster": None},
    "Ozgur3838": {"points": 9, "booster": None},
    "MysteryPhantom7": {"points": 5, "booster": None},
    "Atharv_2008": {"points": 4, "booster": None},
    "matewasfate": {"points": 4, "booster": None},
    "Justinsenpai": {"points": 2, "booster": None},
    "german11": {"points": 2, "booster": None},
    "schwarzerrabe": {"points": 2, "booster": None},
}


new_table_json = """
{"rank":1,"score":62,"rating":2375,"username":"stambul65","performance":2503}
{"rank":2,"score":38,"rating":2162,"username":"mang0sunr1s3","flair":"symbols.orange-heart","patronColor":6,"performance":2174}
{"rank":3,"score":23,"rating":2009,"username":"kubak5","performance":2166}
{"rank":4,"score":21,"rating":2052,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":1903}
{"rank":5,"score":20,"rating":2110,"username":"nopainogain","flair":"activity.chess-pawn","performance":2083}
{"rank":6,"score":19,"rating":2283,"username":"Satranc599","flair":"activity.1st-place-medal","patronColor":1,"performance":2453}
{"rank":7,"score":19,"rating":2094,"username":"TheRuleBreaker122","flair":"smileys.alien-monster","performance":2087}
{"rank":8,"score":17,"rating":2198,"username":"tadeasek532","performance":2115}
{"rank":9,"score":15,"rating":1827,"username":"Conrad_Gagnon","performance":1765}
{"rank":10,"score":13,"rating":2112,"username":"yongzhengwang","flair":"smileys.ghost","performance":1968}
{"rank":11,"score":9,"rating":2030,"username":"ComeToBaba1","flair":"objects.crown","performance":2171}
{"rank":12,"score":9,"rating":1528,"username":"Ozgur3838","performance":1820}
{"rank":13,"score":5,"rating":1647,"username":"MysteryPhantom7","flair":"nature.shooting-star","performance":1779}
{"rank":14,"score":4,"rating":1882,"username":"Atharv_2008","performance":1764}
{"rank":15,"score":4,"rating":1669,"username":"matewasfate","performance":1510}
{"rank":16,"score":2,"rating":1673,"username":"Justinsenpai","performance":1786}
{"rank":17,"score":2,"rating":1384,"username":"german11","patronColor":10,"performance":1722}
{"rank":18,"score":2,"rating":1496,"username":"schwarzerrabe","performance":1418}
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
