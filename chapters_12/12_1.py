import sys

import pygame

class Blue_Window:
    """创建蓝色背景的窗口"""
    def __init__(self):
        """初始化窗口属性"""
        pygame.init()

        self.screen = pygame.display.set_mode((1300,900))
        pygame.display.set_caption("Blue Window")

        # 设置蓝色背景
        self.bg_color = (0,0,230)

    def show_window(self):
        """显示窗口"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.bg_color)

            pygame.display.flip()

window = Blue_Window()
window.show_window()
