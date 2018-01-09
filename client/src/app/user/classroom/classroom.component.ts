import { Component, OnInit } from "@angular/core";
import { UserService } from "../user.service";

@Component({
  selector: "app-classroom",
  templateUrl: "./classroom.component.html",
  styleUrls: ["./classroom.component.css"]
})

export class ClassroomComponent implements OnInit {
  
  classroom:any;
  constructor(private __userService:UserService) { 

  }
  ngOnInit() {
    this.__userService.getClassroom().subscribe((classroom)=>{
      console.log(classroom)
      this.classroom = classroom
    },(err)=>{
      console.log(err)
    })
  }
}
