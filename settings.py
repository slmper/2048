#!/usr/bin/env python 
# -*- coding:utf-8 -*-


class Settings():
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (251, 248, 241)
        # 背景板设置
        self.bgp_color = (187, 173, 160)
        self.bgp_place = ((50, 50), (400, 400))
