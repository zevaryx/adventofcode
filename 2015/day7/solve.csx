#nullable enable
using System.Text.RegularExpressions;

class Command
{
    public string? reg_1;
    public string? reg_2;
    public string? op;
}

int SolveFor(string dest, ref Dictionary<string, Command> commands, ref Dictionary<string, int> registers, int count = 0)
{
    var data = commands[dest];
    if (!registers.ContainsKey(dest))
    {
        int reg_1_value = 0;
        int reg_2_value = 0;
        if (!String.IsNullOrEmpty(data.reg_1))
        {
            if (!int.TryParse(data.reg_1, out reg_1_value))
            {
                reg_1_value = SolveFor(data.reg_1, ref commands, ref registers, count + 1);
            }
        }
        if (!String.IsNullOrEmpty(data.reg_2))
        {
            if (!int.TryParse(data.reg_2, out reg_2_value))
            {
                reg_2_value = SolveFor(data.reg_2, ref commands, ref registers, count + 1);
            }
        }
        if (!String.IsNullOrEmpty(data.op))
        {
            if (data.op == "NOT")
            {
                registers[dest] = ~reg_2_value;
            }
            else if (data.op == "OR")
            {
                registers[dest] = reg_1_value | reg_2_value;
            }
            else if (data.op == "AND")
            {
                registers[dest] = reg_1_value & reg_2_value;
            }
            else if (data.op == "XOR")
            {
                registers[dest] = reg_1_value ^ reg_2_value;
            }
            else if (data.op == "RSHIFT")
            {
                registers[dest] = reg_1_value >> reg_2_value;
            }
            else if (data.op == "LSHIFT")
            {
                registers[dest] = reg_1_value << reg_2_value;
            }
        }
        else
        {
            registers[dest] = reg_1_value;
        }
    }
    return registers[dest];
}

var commands = new Dictionary<string, Command>();
var registers = new Dictionary<string, int>();
var parser = new Regex(@"(?<reg_1>[a-z]{1,}|\d{1,})? ?(?<op>[A-Z]{1,})? ?(?<reg_2>[a-z]{1,}|\d{1,})? ?-> (?<dest>[a-z]{1,})");
foreach (var line in File.ReadLines("input.txt"))
{
    var match = parser.Match(line);
    commands.Add(match.Groups["dest"].ToString(), new Command() { op = match.Groups["op"].Value, reg_1 = match.Groups["reg_1"].Value, reg_2 = match.Groups["reg_2"].Value });
}

var part1 = SolveFor("a", ref commands, ref registers);

registers.Clear();
commands["b"] = new Command() { op = null, reg_1 = part1.ToString(), reg_2 = null };

var part2 = SolveFor("a", ref commands, ref registers);

Console.WriteLine($"Part 1: {part1}\nPart 2: {part2}");