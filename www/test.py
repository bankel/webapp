import asyncio
import orm
import random
from models import User, Blog, Comment


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop, user='www', password='password', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()


# 要运行协程，需要使用事件循环
if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test(loop))
    # print('Test finished.')
    # loop.close()
    pass
