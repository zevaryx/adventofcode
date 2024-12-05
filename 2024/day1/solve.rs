use std::fs;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let file = fs::read_to_string("input.txt")?;

    let mut list1: Vec<i32> = Vec::new();
    let mut list2: Vec<i32> = Vec::new();

    let mut distance = 0;
    let mut simulartiry = 0;

    file.split("\n").for_each(|line| {
        let items: Vec<i32> = line
            .trim()
            .split("   ")
            .map(|item| item.parse::<i32>().unwrap())
            .collect();

        list1.push(*items.get(0).unwrap());
        list2.push(*items.get(1).unwrap());
    });

    list1.sort();
    list2.sort();

    for idx in 0..list1.len() {
        let item1 = list1.get(idx).unwrap();
        distance += (item1 - list2.get(idx).unwrap()).abs();
        simulartiry += item1 * list2.iter().filter(|&n| n == item1).count() as i32;
    }

    println!("{}", distance);
    println!("{}", simulartiry);

    Ok(())
}
