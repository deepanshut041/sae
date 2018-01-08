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
  constructor(private _authService:AuthService, private router:Router) { 

  }

  ngOnInit() {
    // const userKey = Object.keys(window.localStorage).filter(it => it.startsWith('firebase:authUser'))[0];
    // const user = userKey ? JSON.parse(localStorage.getItem(userKey)) : undefined;
    // if(user){
    //   this.router.navigate(['provider/dashboard']);
    // }
    this.registerForm = new FormGroup({
      email: new FormControl(''),
      first_name: new FormControl(''),
      last_name: new FormControl(''),
      password: new FormControl(''),
      username: new FormControl('')
    });
  }
  signup(){
    console.log(this.registerForm.value)
    this._authService.registerUser(this.registerForm.value).subscribe((response)=>{
      console.log("User registered")
      console.log(response)
    },(err)=>{
      console.log(err)
    })
  }
}
