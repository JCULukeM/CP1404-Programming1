"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def score_calc(score):
    if score > 100 or score < 0:
        return ("Invalid score")
    elif score >= 90:
        return ("Excellent")
    elif score >= 50:
        return ("Pass")
    else:
        return ("Bad")

# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    print (score_calc(score))

main()
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")