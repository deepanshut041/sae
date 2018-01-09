import { Component, OnInit } from "@angular/core";
import { Router, ActivatedRoute, ParamMap } from "@angular/router";
import { UserService } from "../user.service";

@Component({
  selector: "app-course",
  templateUrl: "./course.component.html",
  styleUrls: ["./course.component.css"]
})

export class CourseComponent implements OnInit {
  
  workshop_id
  course
  constructor(private route: ActivatedRoute, private router: Router, private __userService: UserService) {
    this.workshop_id = this.route.snapshot.paramMap.get('id');
  }

  ngOnInit() {
    this.__userService.getCourse(this.workshop_id).subscribe(
      (course)=>{
        console.log(course)
        this.course = course
      },
      (err)=>{
        console.log(err)
      }
    )
  }
}
