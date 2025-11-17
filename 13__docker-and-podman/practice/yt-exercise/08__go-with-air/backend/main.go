package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, n *http.Request) {
	fmt.Fprintf(w, "Hello World in golang")
}
func main(){
http.HandleFunc("/", handler)
http.ListenAndServe(":5000",  nil)
}
