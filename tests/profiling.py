from datetime import datetime

from antlr4 import FileStream

from complexity.visitors.cpp_visitor import CPPABCVisitor


def profiling():
    file_name = 'code/cpp/crazy.cpp'
    ABCVisitor = CPPABCVisitor
    time_limit = 0.5  # seconds

    print(f'Profiling for {file_name}')
    print(f'Time limit is {time_limit}s')

    times = list()
    for i in range(10):
        input = FileStream(file_name, encoding='utf8').strdata
        start_time = datetime.now()
        visitor = ABCVisitor.from_code(input, time_limit=time_limit)
        delta_time = datetime.now() - start_time
        times.append(delta_time.total_seconds() * 1000)
        print('.' if visitor.success else 'F', end='', flush=True)

    print()
    print(f'a: {visitor.a}')
    print(f'b: {visitor.b}')
    print(f'c: {visitor.c}')
    print(f'ABC score: {visitor.abc_score}\n')

    mid = sorted(times[1:])[(len(times) - 1) // 2]
    caching_time = times[0] - mid
    print(f'caching time: {format(caching_time, ".5f")}ms')
    print(f'min: {format(min(times[1:]), ".5f")}ms')
    print(f'mid: {format(mid, ".5f")}ms')
    print(f'max: {format(max(times[1:]), ".5f")}ms')


if __name__ == '__main__':
    profiling()
