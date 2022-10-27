class ConcreteStrategyA implements IStrategy {
    // A Concrete Strategy Subclass

    method(payload) {
        console.log(payload.length)
        console.log('I am ConcreteStrategyA')
    }
}
