import {distance, vector_subtract, scalar_multiply} from "./linear_algebra" 

type NumericFunction = (x: number) => number;
type NumericArray = Array<number>;

function sum_of_squares(v:Array<number>):number {
    /* computes the sum of squared elements in v */
    var result = 0;
    for (var i = 0; i < v.length; i += 1) {
        result+=Math.pow(i, 2);
    }
    return result;
  }
  

function difference_quotient(f:NumericFunction, x:number, h:number):number {
    return (f(x + h) - f(x)) / h;    
}

function partial_difference_quotient(f:NumericFunction, v:Array<number>, i:number, h:number):number {
    // add h to just the i-th element of v
    var item;
    var result = 0;
    for (var j = 0; j < v.length; j += 1) {
        item = 0;
        if (j === i) { item = h; }
        result += (f(v[j] + item) - f(v[j])) / h;
    }        
    return result;
}
   
function estimate_gradient(f:NumericFunction, v:Array<number>, h:number = 1e-05):Array<number> {
    var result:Array<number> = [];
    for (var i = 0, _pj_a = v.length; i < _pj_a; i += 1) {
        result.push(partial_difference_quotient(f, v, i, h));
    }
    return result;
  }
  
  
function step(v:NumericArray, direction:NumericArray, step_size:number) {
    // move step_size in the direction from v
    var result:Array<number> = [];
    for (var i = 0, _pj_a = v.length; i < _pj_a; i += 1) {
      var v_i = v[i];
      var direction_i = direction[i];
      result.push(v_i + step_size * direction_i);
    }
    return result;
  }
  
function sum_of_squares_gradient(v:NumericArray):NumericArray {
    var result = []; 
    for (var i = 0; i < v.length; i += 1) {
      var v_i = v[i];
      result.push(2 * v_i);
    }  
    return result;
  }


function safe(f:NumericFunction) {
    // define a new function that wraps f and return it
    function safe_f(...args) {
        try {
            return f(...args);
        } catch (e) {
            return Number.parseFloat("inf");
      }
    }
    return safe_f;
  }

// minimize / maximize batch
        
function minimize_batch(target_fn:NumericFunction, gradient_fn:NumericFunction, theta_0:number, tolerance:number = 1e-06) {
    //use gradient descent to find theta that minimizes target function
    var gradient;
    var next_theta;
    var next_thetas;
    var next_value;
    var step_sizes =[100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 1e-05];
    var theta= theta_0;
    var value;
    target_fn = safe(target_fn); // safe version of target_fn
    value = target_fn(theta); // value we're minimizing
    while (true) {
        gradient = gradient_fn(theta);

    next_thetas = function () {
        var _pj_a = [],
        _pj_b = step_sizes;
        for (var _pj_c = 0, _pj_d = _pj_b.length; _pj_c < _pj_d; _pj_c += 1) {
            var step_size = _pj_b[_pj_c];
            _pj_a.push(step(theta, gradient, -step_size));
      }

      return _pj_a;
    }.call(this);

    // choose next_theta that minimizes the error function
    next_theta = Math.min(next_thetas, { "key": target_fn });
    next_value = target_fn(next_theta);

    if (Math.abs(value - next_value) < tolerance) {
        // if converging, stop
      return theta;
    } else {
      [theta, value] = [next_theta, next_value];
    }
  }
}


def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negate_all(f):
    """the same when f returns a list of numbers"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]


def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(
        negate(target_fn), negate_all(gradient_fn), theta_0, tolerance
    )



// minimize / maximize stochastic



def in_random_order(data):
    """generator that returns the elements of data in random order"""
    indexes = [i for i, _ in enumerate(data)]  # create a list of indexes
    random.shuffle(indexes)  # shuffle them
    for i in indexes:  # return the data in that order
        yield data[i]


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = list(zip(x, y))
    theta = theta_0  # initial guess
    alpha = alpha_0  # initial step size
    min_theta, min_value = None, float("inf")  # the minimum so far
    iterations_with_no_improvement = 0

    # if we ever go 100 iterations with no improvement, stop
    while iterations_with_no_improvement < 100:
        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

        if value < min_value:
            # if we've found a new minimum, remember it
            # and go back to the original step size
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            # otherwise we're not improving, so try shrinking the step size
            iterations_with_no_improvement += 1
            alpha *= 0.9

        # and take a gradient step for each of the data points
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta


def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_stochastic(
        negate(target_fn), negate_all(gradient_fn), x, y, theta_0, alpha_0
    )


def main():
    logging.info("using the gradient")

    _v = [random.randint(-10, 10) for _ in range(3)]

    _tolerance = 0.0000001

    while True:
        # print v, sum_of_squares(v)
        _gradient = sum_of_squares_gradient(_v)  # compute the gradient at v
        next_v = step(_v, _gradient, -0.01)  # take a negative gradient step
        if distance(next_v, _v) < _tolerance:  # stop if we're converging
            break
        _v = next_v  # continue if we're not

    logging.info("%r", "minimum v {}".format(_v))
    logging.info("%r", "minimum value {}".format(sum_of_squares(_v)))

    logging.info("using minimize_batch")

    _v = [random.randint(-10, 10) for _ in range(3)]

    _v = minimize_batch(sum_of_squares, sum_of_squares_gradient, _v)

    logging.info("%r", "minimum v  = {}".format(_v))
    logging.info("%r", "minimum value = {}".format(sum_of_squares(_v)))

