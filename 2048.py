#!/usr/bin/env python 
# -*- coding:utf-8 -*-.
import funcs


def main():
    # 游戏开始, 随机生成两个基数
    cards = funcs.start()
    funcs.print_cards(cards)

    # w为上指令，s为下指令，a为左指令，d为右指令
    while funcs.check(cards):
        option = input()
        if option == 'w':
            funcs.up_option(cards)
            funcs.print_cards(cards)
        if option == 's':
            funcs.down_option(cards)
            funcs.print_cards(cards)
        if option == 'a':
            funcs.left_option(cards)
            funcs.print_cards(cards)
        if option == 'd':
            funcs.right_option(cards)
            funcs.print_cards(cards)


if __name__ == '__main__':
    main()
