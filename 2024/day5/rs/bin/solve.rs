use std::env;
use std::fs;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = env::args().collect::<Vec<String>>();
    if args.len() == 1 {
        return Err("Please provide a file to process".into());
    }
    let file = fs::read_to_string(args.get(1).unwrap())?;

    let mut rules: Vec<Vec<i32>> = Vec::new();
    let mut updates: Vec<Vec<i32>> = Vec::new();
    file.split("\n").for_each(|line| {
        if line.contains("|") {
            let rule: Vec<i32> = line
                .trim()
                .split("|")
                .map(|part| part.parse::<i32>().unwrap())
                .collect();
            rules.push(rule);
        } else if line.contains(",") {
            let update: Vec<i32> = line
                .trim()
                .split(",")
                .map(|part| part.parse::<i32>().unwrap())
                .collect();
            updates.push(update);
        }
    });

    let mut part1 = 0;
    let mut part2 = 0;

    for update in &updates {
        let mut solution = update.to_owned();
        for page in update {
            for rule in &rules {
                if rule.get(0).unwrap() == page && update.contains(rule.get(1).unwrap()) {
                    let page_idx = solution.iter().position(|x| x == page).unwrap();
                    let dep_idx = solution
                        .iter()
                        .position(|x| x == rule.get(1).unwrap())
                        .unwrap();
                    if page_idx > dep_idx {
                        solution.remove(page_idx);
                        solution.insert(dep_idx, *page);
                    }
                }
            }
        }
        if update == &solution {
            part1 += solution.get(solution.len() / 2).unwrap();
        } else {
            part2 += solution.get(solution.len() / 2).unwrap();
        }
    }

    println!("{}", part1);
    println!("{}", part2);

    Ok(())
}
