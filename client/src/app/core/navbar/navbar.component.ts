import { Component, OnInit,AfterViewInit } from "@angular/core";

@Component({
  selector: "app-navbar",
  templateUrl: "./navbar.component.html",
  styleUrls: ["./navbar.component.scss"]
})

export class NavbarComponent implements OnInit {

  constructor() {

  }

  ngOnInit() {

  }

  ngAfterViewInit() {
    // var nav = document.getElementById('navbar');
    // window.addEventListener("scroll", function () {
    //   if (document.documentElement.scrollTop >= 200) {
    //     nav.classList.add("bg-dark");
    //     console.log("event fired")
    //   } else {
    //     nav.classList.remove("bg-dark");
    //   }
    // })
  }
}
