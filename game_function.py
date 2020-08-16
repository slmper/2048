#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
import pygame
import random
from card import Card


def check_events(cards, stats, play_button):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN and stats.game_active:
            if event.key == pygame.K_UP:
                event_up(cards)
            elif event.key == pygame.K_DOWN:
                event_down(cards)
            elif event.key == pygame.K_LEFT:
                event_left(cards)
            elif event.key == pygame.K_RIGHT:
                event_right(cards)


def check_play_button(stats, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True


def check(cards, stats):
    for x in range(4):
        for y in range(4):
            if cards[x][y].value == 0 or\
                    (y < 3 and (cards[x][y].value == cards[x][y+1].value or cards[y][x].value == cards[y+1][x].value)):
                stats.game_active = True
                return None
    stats.game_active = False


def event_up(cards):
    flag = False
    for y in range(4):
        x = 0
        while x < 4:
            nextn = -1
            m = x + 1
            # 找到下一个值不为零的卡片
            for m in range(m, 4):
                if cards[m][y].value != 0:
                    nextn = m
                    break
            if nextn != -1:
                if cards[x][y].value == 0:
                    cards[x][y].value, cards[nextn][y].value = cards[nextn][y].value, cards[x][y].value
                    x -= 1
                    flag = True
                elif cards[x][y].value == cards[nextn][y].value:
                    cards[x][y].value = cards[x][y].value * 2
                    cards[nextn][y].value = 0
                    flag = True
            x += 1
    if flag:
        base_card(cards)


def event_down(cards):
    flag = False
    for y in range(4):
        x = 3
        while x > -1:
            nextn = -1
            m = x - 1
            for m in range(m, -1, -1):
                if cards[m][y].value != 0:
                    nextn = m
                    break
            if nextn != -1:
                if cards[x][y].value == 0:
                    cards[x][y].value = cards[nextn][y].value
                    cards[nextn][y].value = 0
                    x += 1
                    flag = True
                elif cards[x][y].value == cards[nextn][y].value:
                    cards[x][y].value = cards[x][y].value * 2
                    cards[nextn][y].value = 0
                    flag = True
            x -= 1
    if flag:
        base_card(cards)


def event_left(cards):
    flag = False
    for x in range(4):
        y = 0
        while y < 4:
            nextn = -1
            m = y + 1
            for m in range(m, 4):
                if cards[x][m].value != 0:
                    nextn = m
                    break
            if nextn != -1:
                if cards[x][y].value == 0:
                    cards[x][y].value = cards[x][nextn].value
                    cards[x][nextn].value = 0
                    y -= 1
                    flag = True
                elif cards[x][y].value == cards[x][nextn].value:
                    cards[x][y].value = cards[x][y].value * 2
                    cards[x][nextn].value = 0
                    flag = True
            y += 1
    if flag:
        base_card(cards)


def event_right(cards):
    flag = False
    for x in range(4):
        y = 3
        while y > -1:
            nextn = -1
            m = y - 1
            for m in range(m, -1, -1):
                if cards[x][m].value != 0:
                    nextn = m
                    break
            if nextn != -1:
                if cards[x][y].value == 0:
                    cards[x][y].value = cards[x][nextn].value
                    cards[x][nextn].value = 0
                    y += 1
                    flag = True
                elif cards[x][y].value == cards[x][nextn].value:
                    cards[x][y].value = cards[x][y].value * 2
                    cards[x][nextn].value = 0
                    flag = True
            y -= 1
    if flag:
        base_card(cards)


def update_screen(ai_settings, screen, cards, stats, play_button):
    """更新屏幕上的图片，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 绘制背景板
    pygame.draw.rect(screen, ai_settings.bgp_color, ai_settings.bgp_place, 0)
    draw_cards(cards)
    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def draw_cards(cards):
    for x in range(0, 4):
        for y in range(0, 4):
            cards[x][y].blitme()


def start_game(screen, stats):
    # 创建卡片对象组，随机生成两个基数
    cards = [[Card(screen, 0, 0), Card(screen, 0, 1), Card(screen, 0, 2), Card(screen, 0, 3)],
             [Card(screen, 1, 0), Card(screen, 1, 1), Card(screen, 1, 2), Card(screen, 1, 3)],
             [Card(screen, 2, 0), Card(screen, 2, 1), Card(screen, 2, 2), Card(screen, 2, 3)],
             [Card(screen, 3, 0), Card(screen, 3, 1), Card(screen, 3, 2), Card(screen, 3, 3)]]
    base_card(cards)
    base_card(cards)
    return cards


def basenum():
    # 卡片初始值90%为2,10%为4
    if random.randint(1, 10) == 10:
        return 4
    else:
        return 2


def base_card(cards):
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    while True:
        if cards[x][y].value != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        else:
            cards[x][y].value = basenum()
            return cards