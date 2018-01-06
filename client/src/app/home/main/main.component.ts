import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-main",
  templateUrl: "./main.component.html",
  styleUrls: ["./main.component.css"]
})

export class MainComponent implements OnInit {
  header_img = "/static/ang/assets/header.svg"
  about_img = "/static/ang/assets/about.svg"
  news_img = "/static/ang/assets/latest_news.svg"
  
  constructor() { 

  }

  ngOnInit() {

  }
}
