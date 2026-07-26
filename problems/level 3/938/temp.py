import timeit
import numpy as np

matrix = np.full((2048, 2048), -1, dtype=np.int16)
matrix[123, 456] = 7
i, j = 123, 456
sentinel = np.int16(-1)

cases = {
    "raw_neq_literal": "matrix[i, j] != -1",
    "neq_np_int16_cached": "matrix[i, j] != sentinel",
    "eq_literal": "matrix[i, j] == -1",
    "eq_np_int16_cached": "matrix[i, j] == sentinel",
}

setup_globals = {
    "matrix": matrix,
    "i": i,
    "j": j,
    "sentinel": sentinel,
}

repeat = 7
number = 1_000_000
results = []
for name, stmt in cases.items():
    times = timeit.repeat(stmt, globals=setup_globals, repeat=repeat, number=number)
    best = min(times)
    avg = sum(times) / len(times)
    ns_per_op_best = best / number * 1e9
    ns_per_op_avg = avg / number * 1e9
    results.append((name, ns_per_op_best, ns_per_op_avg))

results.sort(key=lambda x: x[1])

print(f"matrix dtype: {matrix.dtype}, shape: {matrix.shape}")
print(f"timings: best of {repeat}, {number:,} iterations each\n")
print(f"{'case':24} {'best ns/op':>12} {'avg ns/op':>12}")
print('-' * 52)
for name, best_ns, avg_ns in results:
    print(f"{name:24} {best_ns:12.2f} {avg_ns:12.2f}")

print("\ncorrectness check:")
print("matrix[i, j] value:", matrix[i, j])
print("raw != -1:", matrix[i, j] != -1)
print("!= np.int16(-1):", matrix[i, j] != sentinel)