import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { RouterModule } from "@angular/router"
import { HttpClientModule } from '@angular/common/http';

import { ClassroomComponent } from "./classroom/classroom.component";
import { CourseComponent } from "./course/course.component";
import { RegisterComponent } from "./register/register.component";
import { UserComponent } from "./user.component";
import { UserService } from "./user.service";

@NgModule({
  declarations: [
    ClassroomComponent, CourseComponent, RegisterComponent, UserComponent
  ],
  imports: [
    CommonModule, HttpClientModule, FormsModule, ReactiveFormsModule, RouterModule
  ],
  providers: [UserService]
})
export class UserModule { }
