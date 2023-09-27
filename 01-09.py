# 01「パタトクカシーー」
a ="パタトクカシー"
print(a[0:8:2])


# 02「パトカー」＋「タクシー」＝「パタトクカシーー」
#　自力でないです・・・
words = ["パトカー" , "タクシー"]
letters = [list(word) for word in words]

combined = zip(*letters)
d =''.join([''.join(pair) for pair in combined])
print(d)
