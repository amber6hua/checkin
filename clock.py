from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import tzlocal
from auto_checkin import checkin
import asyncio

sched = BlockingScheduler(timezone=str(tzlocal.get_localzone()))


@sched.scheduled_job('interval', hours=15)
def timed_job():
    print('This job is run.')
    checkin()


sched.start()
