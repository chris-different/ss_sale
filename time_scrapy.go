package main


import (
	"bytes"
	"fmt"
	"os/exec"
)



func main() {
	in := bytes.NewBuffer(nil)
	cmd := exec.Command("sh")
	cmd.Stdin = in


	go func() {
		in.WriteString()
	}
}
