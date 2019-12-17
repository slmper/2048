#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from card import Card
import random


def start():
    cards = [[Card(0), Card(0), Card(0), Card(0)],
             [Card(0), Card(0), Card(0), Card(0)],
             [Card(0), Card(0), Card(0), Card(0)],
             [Card(0), Card(0), Card(0), Card(0)]]
    base_card(cards)
    base_card(cards)
    return cards


def basenum():
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


def print_cards(cards):
    for x in range(4):
        for y in range(4):
            num = cards[x][y].value
            if num:
                print("%4d"% (num), end="|")
            else:
                print("    ", end="|")
            if y == 3:
                print("")


def check(cards):
    for x in range(4):
        for y in range(4):
            if cards[x][y].value == 0 or\
                    (y < 3 and (cards[x][y].value == cards[x][y+1].value or cards[y][x].value == cards[y+1][x].value)):
                return True
    print("游戏结束！")
    return False


def up_option(cards):
    flag = False
    for y in range(4):
        x = 0
        while x < 4:
            nextn = -1
            m = x + 1
            for m in range(m, 4):
                if cards[m][y].value != 0:
                    nextn = m
                    break
            if nextn != -1:
                if cards[x][y].value == 0:
                    cards[x][y].value = cards[nextn][y].value
                    cards[nextn][y].value = 0
                    x -= 1
                    flag = True
                elif cards[x][y].value == cards[nextn][y].value:
                    cards[x][y].value = cards[x][y].value * 2
                    cards[nextn][y].value = 0
                    flag = True
            x += 1
    if flag:
        base_card(cards)
    else:
        print("该操作无法执行")
    return cards


def down_option(cards):
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
    else:
        print("该操作无法执行")
    return cards


def left_option(cards):
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
    else:
        print("该操作无法执行")
    return cards


def right_option(cards):
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
    else:
        print("该操作无法执行")
    return cards
