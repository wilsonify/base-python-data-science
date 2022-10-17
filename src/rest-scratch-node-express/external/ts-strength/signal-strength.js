"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getStrength = void 0;
function getStrength(actual_count, expected_count) {
    const eps = 0.001;
    const result = actual_count / (expected_count + eps);
    return result;
}
exports.getStrength = getStrength;
