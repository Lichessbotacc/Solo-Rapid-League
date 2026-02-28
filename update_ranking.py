import json

# Aktuelle Rangliste als Dict: username -> {'points': int, 'booster': float or None}
current_ranking = {
    "stambul65": {"points": 206, "booster": 2.0},
    "nopainogain": {"points": 50, "booster": 1.8},
    "DarkOnCrack": {"points": 46, "booster": 1.7},
    "mang0sunr1s3": {"points": 41, "booster": 1.2},
    "Conrad_Gagnon": {"points": 30, "booster": 1.6},
    "ComeToBaba1": {"points": 29, "booster": 1.9},
    "kubak5": {"points": 23, "booster": None},
    "Satranc599": {"points": 19, "booster": None},
    "TheRuleBreaker122": {"points": 19, "booster": None},
    "tadeasek532": {"points": 17, "booster": None},
    "yongzhengwang": {"points": 13, "booster": None},
    "matewasfate": {"points": 11, "booster": 1.4},
    "Ozgur3838": {"points": 9, "booster": None},
    "shailesh777": {"points": 8, "booster": 1.5},
    "MysteryPhantom7": {"points": 5, "booster": None},
    "Atharv_2008": {"points": 4, "booster": None},
    "german11": {"points": 4, "booster": None},
    "Konariq7": {"points": 4, "booster": 1.3},
    "Justinsenpai": {"points": 2, "booster": None},
    "schwarzerrabe": {"points": 2, "booster": None},
    "kenedyKimutai": {"points": 2, "booster": 1.1},
}


new_table_json = """
{"rank":1,"score":72,"rating":2382,"username":"stambul65","performance":2389}
{"rank":2,"score":20,"rating":2041,"username":"ComeToBaba1","flair":"objects.crown","performance":2087}
{"rank":3,"score":19,"rating":2088,"username":"nopainogain","flair":"activity.chess-pawn","performance":2009}
{"rank":4,"score":15,"rating":2069,"username":"DarkOnCrack","flair":"nature.glowing-star","patronColor":5,"performance":2110}
{"rank":5,"score":13,"rating":1814,"username":"Conrad_Gagnon","performance":1760}
{"rank":6,"score":8,"rating":2093,"username":"shailesh777","performance":2090}
{"rank":7,"score":7,"rating":1649,"username":"matewasfate","performance":1733}
{"rank":8,"score":4,"rating":2104,"username":"Konariq7","flair":"nature.glowing-star","patronColor":6,"performance":2383}
{"rank":9,"score":2,"rating":2168,"username":"mang0sunr1s3","flair":"symbols.orange-heart","patronColor":6,"performance":2610}
{"rank":10,"score":2,"rating":2173,"username":"kenedyKimutai","flair":"activity.chess-pawn","performance":1797}
{"rank":11,"score":2,"rating":1403,"username":"german11","patronColor":10,"performance":1565}
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
