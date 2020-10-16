hei=input("身長を入力 (cm)")
wei=input("体重を入力 (kg)")
height=int(hei)
weight=int(wei)
if height>0 and weight>0:
    bmi=int(weight)/(int(height)/100)**2
    print(round(bmi))
else:
    print("error")
