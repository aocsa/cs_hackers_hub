
#[test]
fn my_test() {
    assert!(false);
}

fn partition(arr:&mut Vec<i32>, begin:usize, end:usize, pivot_index:usize) -> usize {
    arr.swap(begin, pivot_index);
    let x = arr[begin];
    let mut i = begin;
    let mut j = begin + 1;
    while j <= end {
        if arr[j] <= x {
            i += 1;
            arr.swap(i, j);
        }
        j += 1;
    }
    arr.swap(i, begin);
    i
}

fn partition_arr(arr:&mut [i32], pivot_index:usize) -> usize {
    let begin = 0;
    let end = arr.len() - 1;
    arr.swap(begin, pivot_index);
    let x = arr[begin];
    let mut i = begin;
    let mut j = begin + 1;
    while j <= end {
        if arr[j] <= x {
            i += 1;
            arr.swap(i, j);
        }
        j += 1;
    }
    arr.swap(i, begin);
    i
}


fn quick_sort(arr:&mut Vec<i32>, begin: usize, end:usize){
    if begin < end {
        let pivot_index = begin; // rand(begin, end)
        // println!("begin={} | end={} ", begin, end);
        let mid = partition(arr, begin, end, pivot_index);
        // println!("mid: {}", mid);
        if mid > 0 {
            quick_sort(arr, begin, mid - 1);
        }
        quick_sort(arr, mid + 1, end);
    }
}

fn quick_select(arr:&mut Vec<i32>, begin:usize, end:usize, k:usize) -> i32 {
    if begin == end {
        return arr[begin];
    }
    assert!(begin < end);
    let pivot_index = begin; // rand(begin, end)
    let mid = partition(arr, begin, end, pivot_index);
    if mid == k {
        return arr[k]
    }
    if k < mid {
        return quick_select(arr, begin, mid - 1, k);
    } else {
        return quick_select(arr, mid + 1, end, k);
    }
}

fn quick_sort_arr(arr:&mut [i32]) {
    if arr.len() > 0 {
        let pivot_index = 0; // rand(begin, end)
        let mid = partition_arr(&mut arr[..], pivot_index);
        quick_sort_arr(&mut arr[..mid]);
        quick_sort_arr(&mut arr[mid+1..]);
    }
}

fn greet(x: String) {
    println!("Hello to  {}", x);
}

fn main() {
    let my_greeting = "Hello world!".to_string();
    greet(my_greeting);
    // let mut out: Vec<u64> = Vec::new();
    // { 5, 7, 2, 9, 1 };

    let mut arr = vec![5, 7, 2, 9, 1];
    println!("{:?}", arr);
    let len = arr.len() - 1;

    let topk = quick_select(&mut arr, 0, len, 1);
    println!("topk {} from {:?}", topk, arr);

    quick_sort(&mut arr, 0, len);
    println!("sorted: {:?}", arr);

    let mut arr_2 = vec![5, 7, 2, 9, 1];
    quick_sort_arr(&mut arr_2);
    print!("sorted_arr: {:?}", arr_2);
}
