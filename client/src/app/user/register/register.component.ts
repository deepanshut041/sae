import { Component, OnInit, AfterViewInit } from "@angular/core";
import { FormGroup, FormControl, FormBuilder, Validators, ReactiveFormsModule, FormArray } from "@angular/forms";
import { UserService } from "../user.service";
import { IMAGE_404 } from "../../shared/assets";
@Component({
    selector: "app-register",
    templateUrl: "./register.component.html",
    styleUrls: ["./register.component.css"]
})

export class RegisterComponent implements OnInit, AfterViewInit {

    registerForm: FormGroup
    members: any[]
    currentWorkshops: any[] = []
    currentPlans: any[] = []
    teamLimit: number
    memberLimits: number[] = []
    err_404 = IMAGE_404
    team_members: FormArray
    constructor(private fb: FormBuilder, private userService: UserService) {
        this.registerForm = this.fb.group({
            'team_id': [null, Validators.required],
            'workshop': [null, Validators.required],
            'plan': ['', Validators.required],
            'team_members': this.fb.array([this.createItem()])
        })
        this.team_members = this.registerForm.get('team_members') as FormArray
    }

    ngOnInit() {
        this.clearFormArray(this.team_members)
        this.userService.getCurrentWorkshops().subscribe((workshops) => {
            this.currentWorkshops = workshops['workshops']
            console.log(workshops)
        }, (err) => {
            console.log(err)
        })
    }
    ngAfterViewInit() {
        this.registerForm.controls['workshop'].valueChanges.subscribe((value) => {
            this.currentPlans = []
            this.memberLimits = []
            this.clearFormArray(this.team_members)
            let workshops = this.currentWorkshops.filter(workshop => {
                if (workshop['id'] == value) {
                    this.currentPlans = workshop['plans']
                    return (true)
                }
            })

        });
        this.registerForm.controls['plan'].valueChanges.subscribe((value) => {
            this.clearFormArray(this.team_members)
            let plans = this.currentPlans.filter(plan => {
                if (plan['id'] == value) {
                    this.teamLimit = plan['team_limit']
                    return (true)
                }
            })
            this.memberLimits = []
            for (let i = 0; i < this.teamLimit; i++) {
                this.memberLimits[i] = i + 1
            }

        });
    }
    onMemberSelected(deviceValue) {
        this.clearFormArray(this.team_members)
        for (let i = 1; i < deviceValue; i++) {
            this.addItem()
        }
    }
    // Forms array createItem create new item, add item to form, clear fom values
    createItem(): FormGroup {
        return this.fb.group({
            'username': [null, Validators.required],
            'email': [null, Validators.required],
            'user_contact': [null, Validators.required],
            'user_college': [null, Validators.required],
            'is_user_local': [null, Validators.required],
        });
    }
    addItem(): void {
        this.team_members.push(this.createItem());
    }
    clearFormArray = (formArray: FormArray) => {
        while (formArray.length !== 1) {
            formArray.removeAt(0)
        }
    }

    //register form
    register(){
        console.log(this.registerForm.value)
        this.userService.postEnrollment(this.registerForm.value).subscribe((link)=>{
            console.log(link)
        },(err)=>{
            console.log(err)
        })
    }
}
