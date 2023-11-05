import importlib
import os
import time

from .plugin import plugins


class Bot:
    def __init__(self, name: str):
        self.name = name
        self.user_name = "You"
        self.plugins = plugins
        self.plugin_num = 0

    def load_plugins(self):
        """
        从插件目录加载插件
        :return:
        """
        print("[system] 开始加载插件...")
        time.sleep(1)

        dirs = os.listdir("plugins")
        for file in dirs:
            if not os.path.isfile(file):
                print(f"[system] 正在加载插件：{file}")
                importlib.import_module("plugins." + file)
                self.plugin_num += 1

        for plug in self.plugins:
            # 按优先级排序
            plug.sort()

        print(f"[system] 插件加载完成，共计加载{self.plugin_num}个插件，{sum([i.get_num() for i in plugins])}个处理函数\n")
        time.sleep(1)
        print("-" * 18)
        for i in "start conversation->\n\n":
            print(i, end="")
            time.sleep(0.02)
        time.sleep(0.2)

    def start(self):
        """
        开始获取、处理消息
        :return:
        """
        while True:
            self.handle(self.rec_msg())

    def handle(self, msg):
        """
        分派消息到插件、处理消息
        :param msg:
        :return:
        """
        for plugin in self.plugins:
            for match in plugin.get_match(msg):
                match.handle(self, msg)
                if match.block:
                    return

    def send_msg(self, msg):
        """
        打印消息的方法
        :param msg:
        :return:
        """
        print(f"{self.name}: {msg}")

    def rec_msg(self):
        """
        接受消息的方法
        :return:
        """
        return input(self.user_name + ": ")
