import numpy as np
# viterbi_weathaer
# obs:   观察状态
# states:真实(隐)状态
# startP:初始状态/概率
# transP:转移概率(隐状态)
# emitP :发射(输出)概率
startP = np.array([0.63,0.17,0.20])      #初始状态
transP = np.array([[0.5, 0.375, 0.125],  #状态转移矩阵
                    [0.25, 0.125, 0.625],
                    [0.25, 0.375, 0.375]])

emitP = np.array([[0.6, 0.20, 0.05],     #发射(输出)概率矩阵
                  [0.25, 0.25, 0.25],
                  [0.05, 0.10, 0.50]])


state1emit = startP*emitP[:,0]   #第一天天气预测概率
state2emit = np.array([max(state1emit*transP[:,i])*emitP[i,1] for i in range(3)])  #第二天天气预测概率
state3emit = np.array([max(state2emit*transP[:,i])*emitP[i,2] for i in range(3)])  #第三天天气预测概率


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