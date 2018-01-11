import { Component, OnInit } from "@angular/core";
import { UserService } from "../user.service";
import { IMAGE_CLASSROOM } from "../../shared/assets";

@Component({
  selector: "app-classroom",
  templateUrl: "./classroom.component.html",
  styleUrls: ["./classroom.component.css"]
})

export class ClassroomComponent implements OnInit {
  
  classroom:any;
  workshops_background = IMAGE_CLASSROOM
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
