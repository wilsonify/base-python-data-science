
def main():
    raw_digits = [
        """11111
           1...1
           1...1
           1...1
           11111""",
        """..1..
           ..1..
           ..1..
           ..1..
           ..1..""",
        """11111
           ....1
           11111
           1....
           11111""",
        """11111
           ....1
           11111
           ....1
           11111""",
        """1...1
           1...1
           11111
           ....1
           ....1""",
        """11111
           1....
           11111
           ....1
           11111""",
        """11111
           1....
           11111
           1...1
           11111""",
        """11111
           ....1
           ....1
           ....1
           ....1""",
        """11111
           1...1
           11111
           1...1
           11111""",
        """11111
           1...1
           11111
           ....1
           11111""",
    ]

    def make_digit(raw_digit):
        return [
            1 if c == "1" else 0 for row in raw_digit.split("\n") for c in row.strip()
        ]

    inputs_ = list(map(make_digit, raw_digits))

    targets = [[1 if i == j else 0 for i in range(10)] for j in range(10)]

    random.seed(0)  # to get repeatable results
    input_size = 25  # each input is a vector of length 25
    num_hidden = 5  # we'll have 5 neurons in the hidden layer
    output_size = 10  # we need 10 outputs for each input

    # each hidden neuron has one weight per input, plus a bias weight
    hidden_layer = [
        [random.random() for _ in range(input_size + 1)] for _ in range(num_hidden)
    ]

    # each output neuron has one weight per hidden neuron, plus a bias weight
    output_layer = [
        [random.random() for _ in range(num_hidden + 1)] for _ in range(output_size)
    ]

    # the network starts out with random weights
    _network = [hidden_layer, output_layer]

    # 10,000 iterations seems enough to converge
    for _ in range(10000):
        for input_vector_, target_vector in zip(inputs_, targets):
            backpropagate(_network, input_vector_, target_vector)

    def predict(in_put):
        return feed_forward(_network, in_put)[-1]

    for i, input_i in enumerate(inputs_):
        outputs_ = predict(input_i)
        logging.debug("i = {}".format(i))
        logging.info("%r", "[round(p, 2) for p in outputs_] ={}".format([round(p, 2) for p in outputs_]))

    logging.info(""".@@@....@@..@@....@@.@@@.""")
    # noinspection PyPep8
    logging.info(
        "%r",
        "rounded predictions {}".format(
            [
                round(x, 2)
                for x in predict(
                [
                    0,
                    1,
                    1,
                    1,
                    0,
                    0,
                    0,
                    0,
                    1,
                    1,
                    0,
                    0,
                    1,
                    1,
                    0,
                    0,
                    0,
                    0,
                    1,
                    1,
                    0,
                    1,
                    1,
                    1,
                    0,
                ]
            )
            ]
        ),
    )  # .@@@.

    logging.info(""".@@@.@..@@.@@@.@..@@.@@@.""")
    # noinspection PyPep8
    logging.info(
        "%r",
        "rounded predictions {}".format(
            [
                round(x, 2)
                for x in predict(
                [
                    0,
                    1,
                    1,
                    1,
                    0,
                    1,
                    0,
                    0,
                    1,
                    1,
                    0,
                    1,
                    1,
                    1,
                    0,
                    1,
                    0,
                    0,
                    1,
                    1,
                    0,
                    1,
                    1,
                    1,
                    0,
                ]
            )
            ]
        ),
    )


if __name__ == "__main__":
    dictConfig(config.LOGGING_CONFIG_DICT)
    main()
