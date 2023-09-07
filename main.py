# from scrapy import cmdline
# import schedule
# import time

# # spider = "rilispider"

# # def job(spider):
# #     cmdline.execute(f"scrapy crawl {spider}".split())
# # schedule.every(10).seconds.do(job(spider=spider))
# # while True:
# #     schedule.run_pending()
# #     time.sleep(1)



# def job():
#     cmdline.execute(f"scrapy crawl rilispider".split())

# schedule.every(1).minutes.do(job)
# # schedule.every().hour.do(job)
# # schedule.every().day.at("10:30").do(job)
# # schedule.every().monday.do(job)
# # schedule.every().wednesday.at("13:15").do(job)
# # schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# # schedule.every().minute.at(":17").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

import threading
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
from scrapy import cmdline


def timer(n):
    while True:
        time.sleep(n)

class myshcedule(object):

    def job2(self, spider):
        cmdline.execute(f"scrapy crawl {spider}".split())

    def start_jobs(self, spider):
        scheduler = BlockingScheduler()
        scheduler.add_job(func=self.job2, args=[spider],
                          trigger="interval", hours=24)  # 这里是调度的关键
        scheduler.start()

    def update_thread(self, spider):
        thread = threading.Thread(target=self.start_jobs, args=[spider])
        thread.start()
        print("start")

if __name__ == '__main__':
    app = myshcedule()
    app.update_thread("rilispider")
    timer(10) 
