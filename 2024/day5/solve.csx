using System.Collections.Generic;
using System.Linq;
using Internal;

Func<string, int?> tryParse = s => int.TryParse(s, out int n) ? (int?)n : null;

var rules = new List<List<int>>();
var updates = new List<List<int>>();
int part1 = 0;
int part2 = 0;

foreach (var line in File.ReadLines("input.txt"))
{
    if (line.Contains("|"))
    {
        rules.Add(line
            .Trim()
            .Split("|")
            .Select(x => tryParse(x))
            .Where(x => x.HasValue)
            .Select(x => x.Value)
            .ToList());
    }
    else if (line.Contains(","))
    {
        updates.Add(line
            .Trim()
            .Split(",")
            .Select(x => tryParse(x))
            .Where(x => x.HasValue)
            .Select(x => x.Value)
            .ToList());
    }
}

foreach (var update in updates)
{
    var solution = new List<int>(update);
    foreach (var page in update)
    {
        foreach (var rule in rules)
        {
            if (rule[0] == page && update.Contains(rule[1]))
            {
                var page_idx = solution.IndexOf(rule[0]);
                var dep_idx = solution.IndexOf(rule[1]);
                if (page_idx > dep_idx)
                {
                    solution.Remove(page);
                    solution.Insert(dep_idx, page);
                }
            }
        }
    }
    if (update.SequenceEqual(solution))
    {
        part1 += solution[solution.Count / 2];
    }
    else
    {
        part2 += solution[solution.Count / 2];
    }
}

Console.WriteLine(part1.ToString());
Console.WriteLine(part2.ToString());