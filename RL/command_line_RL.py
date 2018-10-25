'''
步骤：创建Q表——选择动作——环境反馈——更新环境
'''

import numpy as np
import pandas as pd
import  time

# 设置参数
np.random.seed(2) #伪随机数生成
N_STATES = 6 #1维世界的宽度，即状态的数量
ACTIONS = ['left','right'] #探索者可能的动作
EPSILON = 0.9 #贪婪度 greedy值
ALPHA = 0.1 #学习率
GAMMA = 0.9 #奖励衰减率
MAX_EPISODES = 4 #最大回合数
FRESH_TIME = 0.3 #动作间隔时间

# 创建Q table
def build_q_table(n_states,actions):
    table = pd.DataFrame(np.zeros([n_states,len(actions)]),columns=actions)
    return table

# 选择动作action
def choose_action(state,q_table):
    state_actions = q_table.iloc[state,:] #iloc对DataFrame数字索引，状态state的全部action值，index为actions
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0): #非贪婪或者state未尝试过
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.argmax() #贪婪模式,argmax()取index
    return action_name #返回action

# 环境反馈，奖励
def get_env_feedback(S, A):
    # 根据环境进行反馈
    if A == 'right':    # 右移
        if S == N_STATES - 2:   # 终点前一步
            S_ = 'terminal' # 下一步就是终点
            R = 1
        else:
            S_ = S + 1 # 继续右移
            R = 0
    else:   # 左移
        R = 0
        if S == 0:
            S_ = S  # 到达最左边
        else:
            S_ = S - 1 # 继续左移
    return S_, R
# 创建和更新环境
def update_env(S, episode, step_counter):
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T'创造环境
    # 环境更新
    if S == 'terminal':
        print('Episode %s: total_steps = %s' % (episode+1, step_counter))
        time.sleep(2)
    else:
        env_list[S] = 'o'
        print(''.join(env_list))
        time.sleep(FRESH_TIME)

# 主函数
def rl():
    q_table = build_q_table(N_STATES, ACTIONS)  # 初始 q table
    for episode in range(MAX_EPISODES):     # 回合
        step_counter = 0
        S = 0   # 回合初始位置
        is_terminated = False   # 是否回合结束
        update_env(S, episode, step_counter)    # 环境更新
        while not is_terminated:

            A = choose_action(S, q_table)   # 选行为
            S_, R = get_env_feedback(S, A)  # 实施行为并得到环境的反馈
            q_predict = q_table.loc[S, A]    # 估算的(状态-行为)值
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()   #  实际的(状态-行为)值 (回合没结束)
            else:
                q_target = R     #  实际的(状态-行为)值 (回合结束)
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  #  q_table 更新
            S = S_  # 探索者移动到下一个 state

            update_env(S, episode, step_counter+1)  # 环境更新

            step_counter += 1
    return q_table

if __name__ == "__main__":
    q_table = rl()
    print('\rQ-table:\r',q_table)