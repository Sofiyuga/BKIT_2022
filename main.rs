/// итеративная версия
fn fib_iter(n: u64) -> u64 {
// создание двух изменяемых переменных
    let (mut cur, mut next) = (0u64, 1u64);
    for _ in 0u64..n {
        let tmp = cur + next;
        cur = next;
        next = tmp;
    }
    cur
}

/// рекурсивная версия
///64битное число целое неотрицательное
fn fib_recursive(n: u64) -> u64 {
//// функция сопоставления
    match n {
        0 | 1 => n,
        n => fib_recursive(n - 1) + fib_recursive(n - 2),
    }
}

fn main() {
///создание вектора
    let fns = vec![(fib_iter as fn(u64) -> u64, "iterative implementation:"),
                   (fib_recursive as fn(u64) -> u64, "recursive implementation:")];
    for (f, desc) in fns {
        let r = (0u64..10).map(f).collect::<Vec<u64>>();
        println!("{} \n{:?}\n", desc, r);
    }
}
