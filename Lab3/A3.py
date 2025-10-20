prev = int(input()) 
curr = int(input())  

if curr >= prev:
    volume = curr - prev
else:
    volume = 10000 - prev + curr

if volume <= 300:
    payment = 21.0
elif volume <= 600:
    payment = 21 + (volume - 300) * 0.06
elif volume <= 800:
    payment = 21 + 300 * 0.06 + (volume - 600) * 0.04
else:
    payment = 21 + 300 * 0.06 + 200 * 0.04 + (volume - 800) * 0.025

avg_price = payment / volume if volume > 0 else 0

print(f"ќбъем использованного газа: {volume} куб. м")
print(f"—умма оплаты: {payment:.2f} $")
print(f"—редн€€ цена за кубометр: {avg_price:.2f} $")