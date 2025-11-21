// data splitting

export function split_data(data:Array<Array<number>>, prob:number) {
    // split data into fractions [prob, 1 - prob]
    const results = { "train":[] as Array<Array<number>>, "test":[] as Array<Array<number>> }
    for (const row of data) {
        if (Math.random() < prob) {
            results["test"].push(row)
        } else {
            results["train"].push(row)
        }
    }
    return results
}

export function train_test_split(x:Array<Array<number>>, y:Array<number>, test_pct:number) {
    const results = {
        "x_train":[] as Array<Array<number>>,
        "y_train":[] as Array<number>,
        "x_test":[] as Array<Array<number>>,
        "y_test":[] as Array<number>
    }
    for (const [i, x_i] of x.entries()) {
        const y_i = y[i]
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

export function accuracy(tp:number, fp:number, fn:number, tn:number) {
    const correct = tp + tn
    const total = tp + fp + fn + tn
    return correct / total
}

export function precision(tp:number, fp:number, fn:number, tn:number) {
    return tp / (tp + fp)
}

export function recall(tp:number, fp:number, fn:number, tn:number) {
    return tp / (tp + fn)
}

export function f1_score(tp:number, fp:number, fn:number, tn:number) {
    const p = precision(tp, fp, fn, tn)
    const r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)
}
