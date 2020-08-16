#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self):
        """初始化统计信息"""
        self.reset_stats()
        # 让游戏一开始处于非活动状态
        self.game_active = False
        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.score = 0