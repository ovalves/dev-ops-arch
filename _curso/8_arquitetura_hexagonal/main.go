package main

import (
	"database/sql"

	_ "github.com/mattn/go-sqlite3"
	db2 "github.com/ovalves/go-hexagonal/adapters/db"
	"github.com/ovalves/go-hexagonal/application"
)

func main() {
	db, _ := sql.Open("sqlite3", "db.sqlite")
	dbAdapter := db2.NewProductDb(db)
	productService := application.NewProductService(dbAdapter)
	product, _ := productService.Create("Celular 2", 50)
	productService.Enable(product)
}
