import os

from dsl import machine_learning

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def accuracy(self, body):
    tp = body["tp"]
    fp = body["fp"]
    fn = body["fn"]
    tn = body["tn"]
    result = machine_learning.accuracy(tp, fp, fn, tn)
    self.publish(result)


def f1_score(self, body):
    tp = body["tp"]
    fp = body["fp"]
    fn = body["fn"]
    tn = body["tn"]
    result = machine_learning.f1_score(tp, fp, fn, tn)
    self.publish(result)


def precision(self, body):
    tp = body["tp"]
    fp = body["fp"]
    fn = body["fn"]
    tn = body["tn"]
    result = machine_learning.precision(tp, fp, fn, tn)
    self.publish(result)


def recall(self, body):
    tp = body["tp"]
    fp = body["fp"]
    fn = body["fn"]
    tn = body["tn"]
    result = machine_learning.recall(tp, fp, fn, tn)
    self.publish(result)


def split_data(self, body):
    mat = body["mat"]
    p = body['p']
    result = machine_learning.split_data(mat, p)
    self.publish(result)


def train_test_split(self, body):
    x = body["x"]
    y = body["y"]
    p = body["p"]
    x_train, x_test, y_train, y_test = machine_learning.train_test_split(x, y, p)
    result = dict(
        x_train=x_train,
        x_test=x_test,
        y_train=y_train,
        y_test=y_test
    )
    self.publish(result)
