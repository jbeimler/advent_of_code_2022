package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("../elf_data.txt")
	var all_calories []int
	var cur_calories int = 0
	if err != nil {
		log.Fatalf("failed to open")

	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		each_ln := strings.TrimSpace(scanner.Text())
		if len(each_ln) == 0 {
			all_calories = append(all_calories, cur_calories)
			fmt.Printf("🧝‍♀️ number %3d has %5d calories.\n", len(all_calories), cur_calories)
			cur_calories = 0
		} else {
			tmp_cals, _ := strconv.Atoi(each_ln)
			cur_calories += int(tmp_cals)

		}
	}
	file.Close()
	// descending sort, biggest to smallest
	sort.SliceStable(all_calories, func(i, j int) bool {
		return all_calories[i] > all_calories[j]
	})

	fmt.Printf("\nThe 🧝‍♀️ with the most calories has %d calories.\n", all_calories[0])
}
