def symbolic(score, documents_complete):
    if documents_complete and score >= 70:
        return "Review"
    else:
        return "Hold"
def probability_based(probability):
    if probability >= 0.70:
        return "Review"
    else:
        return "Hold"
cases = [
    ("Complete High", 82, True, 0.81),
    ("Complete Low", 68, True, 0.74),
    ("Incomplete High", 91, False, 0.88),
    ("Boundary", 70, True, 0.70)
]
print("Case | Rule-Based | Probability-Based | Disagreement")

for name, score, documents, probability in cases:
    rule_result = symbolic(score, documents)
    probability_result = probability_based(probability)
    disagreement = rule_result != probability_result
    print(name, rule_result, probability_result, disagreement, sep=" | ")