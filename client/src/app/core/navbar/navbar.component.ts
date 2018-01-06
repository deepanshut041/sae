import { Component, OnInit,AfterViewInit } from "@angular/core";

@Component({
  selector: "app-navbar",
  templateUrl: "./navbar.component.html",
  styleUrls: ["./navbar.component.css"]
})

export class NavbarComponent implements OnInit {

  constructor() {

  }

  ngOnInit() {

  }

  ngAfterViewInit() {
    var nav = document.getElementById('navbar');
    var inner_nav = document.getElementById('inner-navbar');
    var empty_nav = document.getElementById('empty-navbar');
    window.addEventListener("scroll", function () {
      if (document.documentElement.scrollTop >= 150) {
        nav.classList.add("fixed-top");
        inner_nav.classList.add("container");
        empty_nav.classList.add("do");
        
      } else {
        nav.classList.remove("fixed-top");
        inner_nav.classList.remove("container");
        empty_nav.classList.remove("do");
      }
    })
  }
}
