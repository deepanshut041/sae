import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-contact",
  templateUrl: "./contact.component.html",
  styleUrls: ["./contact.component.css"]
})

export class ContactComponent implements OnInit {

  contact_img = "/static/ang/assets/contact.svg"
  
  constructor() { 

  }

  ngOnInit() {

  }
}
