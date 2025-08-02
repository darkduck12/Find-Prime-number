import threading
import time


class CalculationTask:
    def __init__(self):
        self.keep_running = True
        self.oshu = False
        self.odd = False
        self.result = 0  # 存储计算结果

    def load_new_number(self, new_number):
        filename = '质数,素数查找'
        with open(filename, 'a') as f_obj:
            f_obj.write(str(new_number) + "\n")

    def get_number(self):
        with open("质数,素数数字最后保存", "r") as f:
            number = int(f.read())
            return number

    def run(self):
        number = self.get_number()
        """主计算任务"""
        while self.keep_running:

            # 计算过程
            number_2 = number % 2
            if number_2 == 0:
                self.oshu = True
            elif number_2 != 0:
                self.oshu = False

            number_3 = number % 2
            if number_3 == 1:
                self.odd = True
            elif number_3 != 1:
                self.odd = False

            if self.oshu:
                pass
            elif self.odd:
                for i in range(3, int(number)):
                    if number % i == 0:
                        break
                else:
                    self.load_new_number(number)
                    self.result = number  # 更新结果
                    print(f"Current value: {number}")
                    time.sleep(1)

            self.oshu = False
            self.odd = False
            number += 1

        # 循环结束后保存结果
        self.save_result()

    def save_result(self, filename="质数,素数数字最后保存"):
        """保存结果到文件"""
        with open(filename, 'w') as f_last:
            f_last.write(str(self.result))
        print(f"Result saved to {filename}: {self.result}")

    def stop(self):
        self.keep_running = False


# 使用示例
task = CalculationTask()
worker = threading.Thread(target=task.run)
worker.start()

input("Press Enter to stop calculation...\n")
task.stop()
worker.join()
