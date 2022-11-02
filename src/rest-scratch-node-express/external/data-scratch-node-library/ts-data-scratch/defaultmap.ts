import { ParserFunction } from "./type-helpers";

/*
Python’s defaultdict is really useful:
from collections import defaultdict
d = defaultdict(lambda: [])
d['a'] += [1, 2, 3]
d['a'] += [4]
print(d['a']) # [1, 2, 3, 4]
print(d['b']) # []
here’s a JavaScript version, using builtin Map 
*/
export class DefaultMap extends Map {
  getDefaultValue: ParserFunction;
  constructor(getDefaultValue:ParserFunction) {
    super();
    this.getDefaultValue = getDefaultValue;
  }
  get = (key: string) => {
    if (!this.has(key)) {
      this.set(key, this.getDefaultValue(key));
    }

    return super.get(key);
  };
};