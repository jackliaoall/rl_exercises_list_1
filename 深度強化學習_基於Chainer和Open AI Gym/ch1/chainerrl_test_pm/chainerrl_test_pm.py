# -*- coding: utf-8 -*-
"""
ChainerRL確認用プログラム（パックマン）
Copyright(c) 2018 Koji Makino and Hiromitsu Nishizaki All Rights Reserved.
"""
import gym
env = gym.make('MsPacman-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
