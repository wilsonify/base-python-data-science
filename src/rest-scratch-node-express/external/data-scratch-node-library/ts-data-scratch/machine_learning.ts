// data splitting

function  split_data(data:Array<Array<number>>, prob:number) {
    // split data into fractions [prob, 1 - prob]
    var results = { "train":[], "test":[] }
    for (var i = 0; i < data.length; i += 1 ) {
        var row=data[i]
        if (Math.random() < prob) {
            results["test"].push(row)
        } else {
            results["train"].push(row)
        }
    }
    return results
}

function train_test_split(x:Array<Array<number>>, y:Array<number>, test_pct:number) {
    var results = {
        "x_train":[],
        "y_train":[],
        "x_test":[],
        "y_test":[]
    }
    for (var i = 0; i < x.length; i += 1 ) {
        var x_i = x[i]
        var y_i = y[i]
        if (Math.random() < test_pct) {
            results["x_test"].push(x_i)
            results["y_test"].push(y_i)
        } else {
            results["x_train"].push(x_i)
            results["y_train"].push(y_i)
        }        
    }
    return results
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
