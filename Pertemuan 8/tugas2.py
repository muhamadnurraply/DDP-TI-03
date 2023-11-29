nilai= int(input("masukan nilai: "))
def UTS_DDP (nilai):
    if nilai <= 60:
        return "failed"
    elif nilai <= 70:
        return "good"
    elif nilai <= 80:
        return "very good"
    elif nilai <= 100:
        return "perfect"
    else:
        return "nilai tidak valid!"
print(nilai)

    