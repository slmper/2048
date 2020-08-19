#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self):
        """初始化统计信息"""
        self.reset_stats()
        # 让游戏一开始处于非活动状态
        self.game_active = False
        # 在任何情况下都不应重置最高得分
        self.db = pymysql.connect("localhost", "root", "xuwl", "2048_high_score", charset='utf8')
        cursor = self.db.cursor()
        cursor.execute("""select high_score from high_scores where max_score='T'""")
        self.db.commit()
        result = cursor.fetchall()
        self.high_score = result[0][0]
        self.high_score_true = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.score = 0