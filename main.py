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
    # app = myshcedule()
    # app.update_thread("rilispider")
    # timer(10) 

    from dotenv import load_dotenv
    from pathlib import Path
    print(Path(Path.cwd(),".env"))
    load_dotenv(dotenv_path=Path(Path.home(),"env_config/.env_jinshidata"),override=True)

    from scrapy import cmdline
    cmdline.execute("scrapy crawl rilispider".split())


  
