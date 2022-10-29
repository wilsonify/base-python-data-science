
interface Iaccuracy {
    tp: any;
    fp: any;
    fn: any;
    tn: any;
};

const accuracy_strategy = (body: Iaccuracy) => new Promise(
    async (resolve, reject) => {
        try {
            var tp = body.tp
            var fp = body.fp
            var fn = body.fn
            var tn = body.tn
            var result = accuracy(tp, fp, fn, tn)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve accuracy ${e}`)
            );
        }
    }
)

interface If1_score {
    tp: any;
    fp: any;
    fn: any;
    tn: any;
}

const f1_score_strategy = (body: If1_score) => new Promise(
    async (resolve, reject) => {
        try {
            var tp = body.tp
            var fp = body.fp
            var fn = body.fn
            var tn = body.tn
            var result = f1_score(tp, fp, fn, tn)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve distance ${e}`)
            );
        }
    }
)

interface Iprecision {
    tp: any;
    fp: any;
    fn: any;
    tn: any;
}

const precision_strategy = (body: Iprecision) => new Promise(
    async (resolve, reject) => {
        try {
            var tp = body.tp
            var fp = body.fp
            var fn = body.fn
            var tn = body.tn
            var result = precision(tp, fp, fn, tn)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve precision ${e}`)
            );
        }
    }
)

interface Irecall {
    tp: any;
    fp: any;
    fn: any;
    tn: any;
}

const recall_strategy = (body: Irecall) => new Promise(
    async (resolve, reject) => {
        try {
            var tp = body.tp
            var fp = body.fp
            var fn = body.fn
            var tn = body.tn
            var result = recall(tp, fp, fn, tn)
            resolve(console.log(result));

        } catch (e) {
            reject(
                console.log(`unable to resolve recall ${e}`)
            );
        }
    }
)

interface Isplit_data {
    mat: any;
    p: any;
}

const split_data_strategy = (body: Isplit_data) => new Promise(
    async (resolve, reject) => {
        try {
            var mat = body.mat
            var p = body.p
            var result = split_data(mat, p)
            resolve(console.log(result));

        } catch (e) {
            reject(
                console.log(`unable to resolve split_data ${e}`)
            );
        }
    }
)

interface Itrain_test_split {
    x: any;
    y: any;
    p: any;
}

const train_test_split_strategy = (body: Itrain_test_split) => new Promise(
    async (resolve, reject) => {
        try {
            var x = body.x
            var y = body.y
            var p = body.p
            var result = train_test_split(x, y, p)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve train_test_split ${e}`)
            );
        }
    }
)
