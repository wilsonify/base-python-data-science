export default function getStrength(actual_count: number, expected_count: number): number {
    const eps = 0.001;
    const result = actual_count / (expected_count + eps);
    return result
}

