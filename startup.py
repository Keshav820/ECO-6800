from dao import db_init
import controller

if __name__ == '__main__':
    db_init.startup()
    controller.startup()
