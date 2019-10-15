import time
from pollinghub import PollingHub, Pollee


def print_msg(msg):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ": " + msg)


def test_polling_hub():
    hub = PollingHub()

    p1 = Pollee('p1', 2, print_msg, 'p1 triggered')
    p2 = Pollee('p2', 1, print_msg, 'p2 triggered')
    p3 = Pollee('p3', 5, print_msg, 'p3 triggered')

    hub.reg(p1)
    hub.reg(p2)
    hub.reg(p3)

    hub.start()
    time.sleep(10)
    hub.stop()


if __name__ == '__main__':
    test_polling_hub()
