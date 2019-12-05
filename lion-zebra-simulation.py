import matplotlib.pyplot as plt
import matplotlib.style

#草食動物の総数
her_0 = 10
#肉食動物の総数
met_0 = 1
#草食動物の時間に対する増加の比例定数
her_bo_1 = 0.5
#草食動物と肉食動物が出会う確率の比例定数
enc_1 = 1.2
#肉食動物の死亡の比例定数
dh_2 = 0.1
#肉食動物の増加の比例定数
k_2 = 0.07
#時間
year = 100
#草食動物の数
her = []
#肉食動物の数
met = []
#時間
TY = []

#シミュレーション
her.append(her_0 / (her_bo_1/enc_1))
met.append(met_0 / (her_bo_1/enc_1))
E = dh_2 / her_bo_1
K = k_2 / enc_1
f = year / (1/her_bo_1)
a = 0
i = 0
TY.append(0)

while i < f:

    her.append(her[a] + 0.1*(her[a] - her[a]*met[a]))
    met.append(met[a] + 0.1*(-E*met[a] + K*her[a]*met[a]))

    i = i + 0.1
    a = a + 1
    TY.append(i)

#描画
fig, ax = plt.subplots()

ax.plot(TY, her, label='herbivore')
ax.plot(TY, met, label='carnivore')
ax.legend()

plt.show()
