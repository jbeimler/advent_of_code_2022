var lineReader = require('line-reader');

let all_calories: Array<number> = [];
let cur_calories: number = 0;


lineReader.eachLine('../elf_data.txt', function(line: string, last: boolean) {
  let each_ln = line.trim();
  if (each_ln.length == 0) { 
    all_calories.push(cur_calories);
    console.log(`🧝‍♀️ number ${all_calories.length} has ${cur_calories} calories.`);
    cur_calories = 0;
  } else {
    cur_calories = cur_calories + Number(each_ln);
    
  }

  if (last) {
    all_calories.sort((one, two) => (one > two ? -1 : 1));

    console.log(`\nThe 🧝‍♀️ with the most calories has ${all_calories[0]} calories.`);
    console.log(`\nThe top 3 🧝‍♀️ with the most calories have ${all_calories.slice(0,3).reduce((a, b) => a + b, 0)} calories.`)

    return false; // stop reading
    
    141783
  }
});