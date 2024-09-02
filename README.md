# base-python-data-science
based on https://github.com/joelgrus/data-science-from-scratch

base python, few dependencies

| folder | description |
| ------ | ----------- |
| data-scratch-library | python library code | 
| data-scratch-matplotlib | plot code that depends on matplotlib | 
| data-scratch-scrape | scraping code that depends on requests and beautiful soup |
| data-scratch-cpp-library | port to C++ |
| data-scratch-node-library | port to javascript |
| data-scratch-amqp | amqp based pika consumer |
| data-scratch-mqtt | mqtt based paho consumer |
| rest-scratch-node-express | port to javascript express server |
| rest-scratch-flask | REST based flask server |
| rest-client-ts-node | REST based typescript client |
| rest-scratch-pistache | REST based C++ pistache server |
| rest-scratch-rust | REST based rust server |

# install

```
git clone https://github.com/wilsonify/base-python-data-science.git
cd src/data-scratch
python -m pip install -r requirements.txt
python setup.py install
```

# test

```
python -m pip install -r test-requirements.txt
python -m pytest
```

# usage

```
import data_science_from_scratch 
```


