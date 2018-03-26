from flask import Flask
from ss_sale.app import create_app
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

application = create_app('development')


if __name__ == '__main__':
    application.run()
