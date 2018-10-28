import numpy as np
#HMM_weather
# obs:   观察状态
# states:真实(隐)状态
# startP:初始状态/概率
# transP:转移概率(隐状态)
# emitP :发射(输出)概率
startP = np.array([0.63,0.17,0.20])     #初始状态

trans_P = np.array([[0.5,0.375,0.125],  #状态转移矩阵
                    [0.25,0.125,0.625],
                    [0.25,0.375,0.375]])

emitP = np.array([[0.6,0.20,0.05],       #发射(输出)概率矩阵
                  [0.25,0.25,0.25],
                  [0.05,0.10,0.50]])

state1emit = startP*emitP[:,0]           #第一天天气预测概率

state2_mid = np.dot(state1emit,trans_P)  #第一天天气预测概率乘以转移概率矩阵
state2emit = state2_mid*emitP[:,1]       #第二天天气预测概率

state3_mid = np.dot(state2emit,trans_P)  #第二天天气预测概率乘以转移概率矩阵
state3emit = state3_mid*emitP[:,2]       #第三天天气预测概率

#第一天天气值
#第二天天气值
#第三天天气值
state1 = state1emit.argmax()
state2 = state2emit.argmax()
state3 = state3emit.argmax()

print(state1emit)
print(state2emit)
print(state3emit)

print(state1,state2,state3)