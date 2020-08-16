#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pygame
class Card:
    def __init__(self, screen, x, y, value=0, card_color=[(255, 255, 255), (204, 192, 180)]):
        self.screen = screen
        self.__value = value
        self.x = x
        self.y = y
        # card_color[0]为卡片数字颜色，card_color[1]为卡片背景色
        self.card_color = card_color
        self.screen_rect = screen.get_rect()

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def blitme(self):
        self.num_color_choose()
        card_rect = pygame.draw.rect(self.screen, self.card_color[1], (66+96*self.y, 66+96*self.x, 80, 80), 0)
        self.draw_num(card_rect)

    def draw_num(self, card_rect):
        # 绘制卡片
        num_str = str(self.value)
        num_size = 60
        if self.value >= 1024:
            num_size = 48
        font = pygame.font.SysFont(None, num_size)
        num_image = font.render(num_str, True, self.card_color[0], self.card_color[1])
        num_rect = num_image.get_rect()
        num_rect.centerx = card_rect.centerx
        num_rect.centery = card_rect.centery
        self.screen.blit(num_image, num_rect)

    def num_color_choose(self):
        if self.value == 0:
            self.card_color[0] = (204, 192, 180)
            self.card_color[1] = (204, 192, 180)
        elif self.value == 2:
            self.card_color[0] = (119, 110, 101)
            self.card_color[1] = (238, 228, 218)
        elif self.value == 4:
            self.card_color[0] = (119, 110, 101)
            self.card_color[1] = (236, 224, 202)
        elif self.value == 8:
            self.card_color[0] = (255, 255, 255)
            self.card_color[1] = (242, 177, 121)
        elif self.value == 16:
            self.card_color[0] = (255, 255, 255)
            self.card_color[1] = (236, 141, 83)
        elif self.value == 32:
            self.card_color[0] = (255, 255, 255)
            self.card_color[1] = (245, 124, 95)
        elif self.value == 64:
            self.card_color[0] = (255, 255, 255)
            self.card_color[1] = (233, 89, 55)
        elif self.value == 128:
            self.card_color[0] = (255, 255, 255)
            self.card_color[1] = (243, 217, 107)
        elif self.value == 256:
            self.card_color[0] = (255, 255, 255)
            self.card_color[1] = (241, 208, 75)
        elif self.value == 512:
            self.card_color[0] = (255, 255, 255)
            self.card_color[1] = (228, 192, 42)
        elif self.value == 1024:
            self.card_color[0] = (255, 255, 255)
            self.card_color[1] = (227, 184, 19)
        else:
            self.card_color[0] = (255, 255, 255)
            self.card_color[1] = (236, 196, 0)

