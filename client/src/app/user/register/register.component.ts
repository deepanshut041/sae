import { Component, OnInit } from "@angular/core";
import { FormGroup, FormControl, FormBuilder, Validators, ReactiveFormsModule } from "@angular/forms";
import { UserService } from "../user.service";
@Component({
  selector: "app-register",
  templateUrl: "./register.component.html",
  styleUrls: ["./register.component.css"]
})

export class RegisterComponent implements OnInit {
  
  registerForm:FormGroup
  members:any[]
  currentWorkshops:any[]
  constructor(private fb:FormBuilder, private userService:UserService) { 
    this.registerForm = this.fb.group({
      'workshop':[null, Validators.required],
      'plan':[null,Validators.required],
      'members': this.fb.array([this.createItem()])
    })
  }

  ngOnInit() {
    this.userService.getCurrentWorkshops().subscribe((workshops)=>{
      console.log(workshops)
    },(err)=>{
      console.log(err)
    })
  }
  createItem(): FormGroup {
    return this.fb.group({
      'username': [null,Validators.required],
      'email': [null, Validators.required],
      'contact': [null,Validators.required],
      'college': [null,Validators.required],
      'is_local': [null,Validators.required],
    });
  }
}
