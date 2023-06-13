package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func StartAPI() {
	log.Printf("Server started")

	router := newRouter()

	log.Fatal(http.ListenAndServe(":3003", router))
}

type route struct {
	Name        string
	Method      string
	Pattern     string
	HandlerFunc http.HandlerFunc
}

func newRouter() *mux.Router {
	router := mux.NewRouter().StrictSlash(true)
	for _, route := range routes {
		var handler http.Handler
		handler = route.HandlerFunc

		router.
			Methods(route.Method).
			Path(route.Pattern).
			Name(route.Name).
			Handler(handler)
	}

	return router
}

var routes = []route{
	route{
		"index",
		"GET",
		"/",
		index,
	},
}

func index(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World!")
}
