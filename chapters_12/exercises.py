import sys

import pygame

class Testkey:
    """观察键盘行为的类"""
    def __init__(self):
        """初始化属性"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Test Key")

    def run_game(self):
        """主循环"""
        while True:
            # 监听健康并打印
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)

            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__main__':
    # 创建并运行游戏
    ai = Testkey()
    ai.run_game()