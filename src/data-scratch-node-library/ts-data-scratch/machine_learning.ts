// data splitting

function  split_data(data:Array<Array<number>>, prob:number) {
    // split data into fractions [prob, 1 - prob]
    var results = new Map<string,Array<Array<number>>>()
    results.set("train",[])
    results.set("test",[])
    for (var i = 0; i < data.length; i += 1 ) {
        var row=data[i]
        var selected = "train"
        if (Math.random() < prob) {
            selected = "test"
        }
        var results_selected = results.get(selected) 
        results_selected.push(row)
    }
    return results
}

function  train_test_split(x, y, test_pct) {
    data = list(zip(x, y))  # pair corresponding values
    train, test = split_data(data, 1 - test_pct)  # split the dataset of pairs
    x_train, y_train = list(zip(*train))  # magical un-zip trick
    x_test, y_test = list(zip(*test))
    return x_train, x_test, y_train, y_test
}

// correctness

function  accuracy(tp:number, fp:number, fn:number, tn:number) {
    var correct = tp + tn
    var total = tp + fp + fn + tn
    return correct / total
}

function  precision(tp:number, fp:number, fn:number, tn:number) {
    return tp / (tp + fp)
}

function  recall(tp:number, fp:number, fn:number, tn:number) {
    return tp / (tp + fn)
}

function  f1_score(tp:number, fp:number, fn:number, tn:number) {
    var p = precision(tp, fp, fn, tn)
    var r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)
}
