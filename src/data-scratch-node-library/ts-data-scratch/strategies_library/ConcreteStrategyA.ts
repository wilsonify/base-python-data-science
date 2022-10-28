class ConcreteStrategyA implements IStrategy {
    // A Concrete Strategy Subclass

    method(payload: string) {
        console.log(payload.length)
        console.log('I am ConcreteStrategyA')
    }
}
