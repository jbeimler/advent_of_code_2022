package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type Action uint64

const (
	Rock     Action = 1
	Paper    Action = 2
	Scissors Action = 3
)

func (a Action) String() string {
	switch a {
	case Rock:
		return "Rock"
	case Paper:
		return "Paper"
	case Scissors:
		return "Scissors"
	}
	return "Rock/Paper/Scissors"
}

var opponent_col1_map = map[string]Action{
	"A": Rock, "B": Paper, "C": Scissors}

var user_col2_map = map[string]Action{
	"X": Rock, "Y": Paper, "Z": Scissors}

var outcome_col2_map = map[string]string{
	"X": "loss", "Y": "draw", "Z": "win"}

var victories = map[Action]Action{
	Rock:     Scissors, // Rock beats scissors
	Paper:    Rock,     // Paper beats rock
	Scissors: Paper,    //	Scissors beats paper
}

var losses = map[Action]Action{
	Scissors: Rock,     // Rock beats scissors
	Rock:     Paper,    // Paper beats rock
	Paper:    Scissors, // Scissors beats paper
}

func determine_score(user_action Action, opponent_action Action) int {
	if user_action == opponent_action {
		fmt.Printf("Both 🧝 & 🧝‍♀️ selected %s. It's a tie!\n", user_action)
		return 3 + int(user_action)
	} else if opponent_action == victories[user_action] {
		fmt.Printf("%s beats %s! 🧝‍♀️ wins, 🧝 loses!\n", user_action, opponent_action)
		return 6 + int(user_action)
	} else {
		fmt.Printf("%s beats %s! 🧝 wins, 🧝‍♀️ loses.\n", opponent_action, user_action)
		return int(user_action)
	}
}

func determine_play(opponent_action Action, outcome string) Action {
	var return_value Action
	switch outcome {
	case "win":
		return_value = losses[opponent_action]
	case "loss":
		return_value = victories[opponent_action]
	default:
		return_value = opponent_action
	}
	fmt.Printf("🧝‍♀️ wants a %s, playing %s\n", outcome, return_value)
	return return_value
}

func main() {

	var score int = 0

	file, err := os.Open("../input.txt")

	if err != nil {
		log.Fatalf("failed to open")

	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		each_ln := strings.TrimSpace(scanner.Text())
		symbols := strings.Split(each_ln, " ")

		score = score + determine_score(
			determine_play(opponent_col1_map[symbols[0]], outcome_col2_map[symbols[1]]),
			opponent_col1_map[symbols[0]])

	}
	file.Close()
	fmt.Println("Score:", score)
}
