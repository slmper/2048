#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
from settings import Settings
import game_function as gf
from button import Button
from game_stats import GameStats


def run_ganme():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("2048")
    stats = GameStats()
    # 创建Play按钮
    play_button = Button(screen, "Play")
    cards = gf.start_game(screen, stats)
    # 开始游戏主循环
    while True:
        gf.check_events(cards, stats, play_button)
        if stats.game_active:
            gf.check(cards, stats)
        gf.update_screen(ai_settings, screen, cards, stats, play_button)

run_ganme()