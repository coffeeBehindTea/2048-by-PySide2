import random
import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from ui_2049 import Ui_mainWindow


class Game(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.game_score = 0
        # self.alive = True
        self.matrix = [
            [self.lb1, self.lb2, self.lb3, self.lb4],
            [self.lb5, self.lb6, self.lb7, self.lb8],
            [self.lb9, self.lb10, self.lb11, self.lb12],
            [self.lb13, self.lb14, self.lb15, self.lb16],
        ]
        self.combed = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
        ]

        
        self.style = {
            "": {
                "bg": "#d6dee0",
            },
            # 0 ~ 4 灰色系  bg 背景颜色， fg字体颜色， fz字体大小
            0: {"bg": "#EEEEEE", "fg": "#EEEEEE", "fz": 30},
            2**1: {"bg": "#E5E5E5", "fg": "#707070", "fz": 30},
            2**2: {"bg": "#D4D4D4", "fg": "#707070", "fz": 30},
            # 8 ～ 16 橙色系
            2**3: {"bg": "#FFCC80", "fg": "#FAFAFA", "fz": 30},
            2**4: {"bg": "#FFB74D", "fg": "#FAFAFA", "fz": 30},
            # 32 ～ 64 红色系
            2**5: {"bg": "#FF7043", "fg": "#FAFAFA", "fz": 30},
            2**6: {"bg": "#FF5722", "fg": "#FAFAFA", "fz": 30},
            # 128～2048 黄色系
            2**7: {"bg": "#FFEE58", "fg": "#FAFAFA", "fz": 30},
            2**8: {"bg": "#FFEB3B", "fg": "#FAFAFA", "fz": 30},
            2**9: {"bg": "#FDD835", "fg": "#FAFAFA", "fz": 30},
            # 1024~2048 橙色系
            2**10: {"bg": "#FF9800", "fg": "#FAFAFA", "fz": 30},
            2**11: {"bg": "#FB8C00", "fg": "#FAFAFA", "fz": 28},
            # 4096 +  红色系
            2**12: {"bg": "#fb3030", "fg": "#FAFAFA", "fz": 28},
            2**13: {"bg": "#e92e2e", "fg": "#FAFAFA", "fz": 28},
            2**14: {"bg": "#da1e1e", "fg": "#FAFAFA", "fz": 24},
            # 2**15 +  黑色 超过2**15颜色不再改变
            2**15: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 22},
            2**16: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 20},
            2**17: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 20},
            2**18: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 20},
            2**19: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 18},
            2**20: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 17},
            2**21: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 16},
            2**22: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 15},
            2**23: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 14},
            2**24: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 13},
            2**25: {"bg": "#3a3a3a", "fg": "#E0E0E0", "fz": 12},
        }
        self.init_button()
        # print(self.style[0]['bg'])
        self.set_number()

        # self.score.setText("fuck you")
        self.show()
        # keyboard.hook(self.abc)
        # self.move_down()

    # def init_game(self):
    #     self.init_button()
    #     self.set_number()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            if self.move_up() != None:
                # print("moved up")

                self.set_number()
        elif event.key() == Qt.Key_Down:
            if self.move_down() != None:
                self.combed = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
        ]
                # print("moved down")
                self.set_number()
        elif event.key() == Qt.Key_Left:
            if self.move_left() != None:
                self.combed = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
        ]
                # print("moved left")
                self.set_number()
        elif event.key() == Qt.Key_Right:
            if self.move_right() != None:
                self.combed = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
        ]
                # print("moved right")
                self.set_number()
        elif event.key() == Qt.Key_R:
            self.restart()

    def get_color(self, color):
        color = color[1:]
        lis = []
        c = ""
        for i in range(0, 6, 2):
            lis.append(color[i : i + 2])
        for i in lis:
            c += str(int(eval("0x" + i)))
            c += ", "
        c = c[:-2]
        return c

    def init_button(self):
        # print(lst)
        for line in self.matrix:
            for lb in line:
                lb.setText("")
                lb.setStyleSheet(
                    f"background: rgb({self.get_color(self.style['']['bg'])});"
                )

    def set_number(self):
        b = random.choice(random.choice(self.matrix))
        while b.text() != "":
            b = random.choice(random.choice(self.matrix))
        b.setText(str("2") if random.randint(1, 11) <= 8 else str("4"))
        self.set_color(b)

    def set_color(self, butt):
        if butt.text() == "":
            butt.setStyleSheet(
                f"background: rgb({self.get_color(self.style['']['bg'])});"
            )
        else:
            txt_color = self.style[int(butt.text())]["fg"]
            butt.setStyleSheet(f"color: rgb({self.get_color(txt_color)});")
            butt.setStyleSheet(
                f"background: rgb({self.get_color(self.style[int(butt.text())]['bg'])});"
            )

    def move_down(self):
        flag = None
        for i in range(3):
            for row in range(2, -1, -1):
                for col in range(0, 4):
                    if (
                        self.matrix[row + 1][col].text() == self.matrix[row][col].text()
                        and self.matrix[row][col].text() != ""
                        and not (self.combed[row + 1][col])
                        and not (self.combed[row][col])
                    ):
                        num = int(self.matrix[row + 1][col].text()) * 2
                        self.matrix[row + 1][col].setText(str(num))
                        self.set_color(self.matrix[row + 1][col])
                        self.matrix[row][col].setText("")
                        self.set_color(self.matrix[row][col])
                        self.combed[row + 1][col] = True
                        self.combed[row][col] = False
                        print(self.combed)
                        flag = 1

                    elif (
                        self.matrix[row + 1][col].text() == ""
                        and self.matrix[row][col].text() != ""
                    ):
                        self.matrix[row + 1][col].setText(self.matrix[row][col].text())
                        self.set_color(self.matrix[row + 1][col])
                        self.matrix[row][col].setText("")
                        self.combed[row+1][col] = self.combed[row][col]
                        self.combed[row][col] = False
                        self.set_color(self.matrix[row][col])
                        flag = 1
        # print("after moved down",self.combed,'\n')
        self.combed = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
        ]
        # print("now combed",self.combed,'\n')
        return flag

    def move_up(self):
        flag = None
        for i in range(3):
            for row in range(1, 4):
                for col in range(0, 4):
                    if (
                        self.matrix[row - 1][col].text() == self.matrix[row][col].text()
                        and self.matrix[row][col].text() != ""
                        and not (self.combed[row - 1][col])
                        and not (self.combed[row][col])
                    ):
                        num = int(self.matrix[row - 1][col].text()) * 2
                        self.matrix[row - 1][col].setText(str(num))
                        self.set_color(self.matrix[row - 1][col])
                        self.matrix[row][col].setText("")
                        self.set_color(self.matrix[row][col])
                        self.combed[row - 1][col] = True
                        self.combed[row][col] = False
                        flag = 1

                    elif (
                        self.matrix[row - 1][col].text() == ""
                        and self.matrix[row][col].text() != ""
                    ):
                        self.matrix[row - 1][col].setText(self.matrix[row][col].text())
                        self.set_color(self.matrix[row - 1][col])
                        self.matrix[row][col].setText("")
                        self.set_color(self.matrix[row][col])
                        self.combed[row-1][col] = self.combed[row][col]
                        self.combed[row][col] = False
                        flag = 1
        # print("after moved up",self.combed,'\n')
        self.combed = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
        ]
        # print("now combed",self.combed,'\n')
        return flag

    def move_right(self):
        flag = None
        for i in range(3):
            for col in range(2, -1, -1):
                for row in range(0, 4):
                    if (
                        self.matrix[row][col + 1].text() == self.matrix[row][col].text()
                        and self.matrix[row][col].text() != ""
                        and not (self.combed[row][col + 1])
                        and not (self.combed[row][col])
                    ):
                        num = int(self.matrix[row][col + 1].text()) * 2
                        self.matrix[row][col + 1].setText(str(num))
                        self.set_color(self.matrix[row][col + 1])
                        self.matrix[row][col].setText("")
                        self.set_color(self.matrix[row][col])
                        self.combed[row][col + 1] = True
                        self.combed[row][col] = False
                        flag = 1

                    elif (
                        self.matrix[row][col + 1].text() == ""
                        and self.matrix[row][col].text() != ""
                    ):
                        self.matrix[row][col + 1].setText(self.matrix[row][col].text())
                        self.set_color(self.matrix[row][col + 1])
                        self.matrix[row][col].setText("")
                        self.set_color(self.matrix[row][col])
                        self.combed[row][col+1] = self.combed[row][col]
                        self.combed[row][col] = False
                        flag = 1
        # print("after moved right",self.combed,'\n')
        self.combed = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
        ]
        # print("now combed",self.combed,'\n')
        return flag

    def move_left(self):
        flag = None
        for i in range(3):
            # 从第二列向右遍历
            for col in range(1, 4):
                # 遍历每行
                for row in range(0, 4):
                    # 如果当前位置左侧一列的数和当前位置相同则合并
                    if (
                        self.matrix[row][col - 1].text() == self.matrix[row][col].text()
                        and self.matrix[row][col].text() != ""
                        and not (self.combed[row][col - 1])
                        and not (self.combed[row][col])
                    ):
                        # 合并x2
                        num = int(self.matrix[row][col - 1].text()) * 2
                        # 设置左边的数
                        self.matrix[row][col - 1].setText(str(num))
                        # 更新颜色
                        self.set_color(self.matrix[row][col - 1])
                        # 设置当前的数为空
                        self.matrix[row][col].setText("")
                        # 更新颜色
                        self.set_color(self.matrix[row][col])
                        # 把左侧合并后的新位置设为combed，当前位置为false
                        self.combed[row][col - 1] = True
                        self.combed[row][col] = False
                        flag = 1
                    # 如果左边位置为空且当前位置不为空
                    elif (
                        self.matrix[row][col - 1].text() == ""
                        and self.matrix[row][col].text() != ""
                    ):
                        # 把左边的位置设置数字为当前位置
                        self.matrix[row][col - 1].setText(self.matrix[row][col].text())
                        # 更新左边列的颜色
                        self.set_color(self.matrix[row][col - 1])
                        # 设置当前位置数为空
                        self.matrix[row][col].setText("")
                        # 更新当前颜色
                        self.set_color(self.matrix[row][col])
                        self.combed[row][col-1] = self.combed[row][col]
                        self.combed[row][col] = False
                        flag = 1
        # print("after moved left",self.combed)
        self.combed = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
        ]
        # print("now combed",self.combed,'\n')
        return flag

    def restart(self):
        self.init_button()
        self.set_number()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Game()
    # print(window.grids)
    sys.exit(app.exec_())
