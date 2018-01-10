import { Component, OnInit } from "@angular/core";
import { AuthService } from "../auth.service";
import { Router } from "@angular/router";
import { FormGroup,FormControl, FormBuilder, Validators,ReactiveFormsModule} from "@angular/forms";


@Component({
  selector: "app-signup",
  templateUrl: "./signup.component.html",
  styleUrls: ["./signup.component.css"]
})

export class SignupComponent implements OnInit {
  msg:any;
  registerForm:FormGroup;
  err:any;
  email_pattern = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
  constructor(private _authService:AuthService, private router:Router, private fb:FormBuilder) {
    this.registerForm = fb.group({
      'first_name':[null, Validators.compose([Validators.required, Validators.minLength(2)])],
      'last_name':[null, Validators.compose([Validators.required, Validators.minLength(2)])],
      'username':[null, Validators.compose([Validators.required, Validators.minLength(2)])],
      'password':[null, Validators.compose([Validators.required, Validators.minLength(6)])],
      'email':[null, Validators.compose([
        Validators.required, Validators.pattern (this.email_pattern)
      ])]
    })  

  }

  ngOnInit() {
    this.turnOffSpinner()
    this.turnOffSuccess()
  }
  signup(){
    this.turnOnSpinner()
    this._authService.registerUser(this.registerForm.value).subscribe((response)=>{
      console.log("User registered")
      console.log(response)
      this.turnOffSpinner()
      this.turnOnSuccess()
    },(err)=>{
      this.turnOffSpinner()
      let username_err = err.error['username'];
      this.err = username_err[0]
    })
  }

  turnOffSpinner(){
    document.getElementById("form").style.display = "block";
    document.getElementById("spinner").style.display = "none";
  }
  turnOnSpinner(){
    document.getElementById("form").style.display = "none";
    document.getElementById("spinner").style.display = "block";
  }
  turnOffSuccess(){
    document.getElementById("form").style.display = "block";
    document.getElementById("verifyEmailAlert").style.display = "none";
  }
  turnOnSuccess(){
    document.getElementById("form").style.display = "none";
    document.getElementById("verifyEmailAlert").style.display = "block";
  }
}
