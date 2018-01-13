import { Component, OnInit } from "@angular/core";
import { FormGroup, FormControl, FormBuilder, Validators, ReactiveFormsModule } from "@angular/forms";
import { UserService } from "../user.service";
import { IMAGE_404 } from "../../shared/assets";
@Component({
    selector: "app-register",
    templateUrl: "./register.component.html",
    styleUrls: ["./register.component.css"]
})

export class RegisterComponent implements OnInit {

    registerForm: FormGroup
    members: any[]
    currentWorkshops: any[] = []
    currentPlans: any[] = []
    teamLimit: number
    memberLimits: number[] = []
    err_404 = IMAGE_404
    constructor(private fb: FormBuilder, private userService: UserService) {
        this.registerForm = this.fb.group({
            'workshop': [null, Validators.required],
            'plan': [null, Validators.required],
            'members': this.fb.array([this.createItem()])
        })
    }

    ngOnInit() {
        this.userService.getCurrentWorkshops().subscribe((workshops) => {
            this.currentWorkshops = workshops['workshops']
            console.log(workshops)
        }, (err) => {
            console.log(err)
        })
    }
    createItem(): FormGroup {
        return this.fb.group({
            'username': [null, Validators.required],
            'email': [null, Validators.required],
            'contact': [null, Validators.required],
            'college': [null, Validators.required],
            'is_local': [null, Validators.required],
        });
    }
    onWorkshopSelected(deviceValue) {
        this.currentPlans = []
        this.memberLimits = []
        let workshops = this.currentWorkshops.filter(workshop => {
            if (workshop['id'] == deviceValue) {
                this.currentPlans = workshop['plans']
                return (true)
            }
        })
    }
    onPlanSelected(deviceValue) {
        let plans = this.currentPlans.filter(plan => {
            if (plan['id'] == deviceValue) {
                this.teamLimit = plan['team_limit']
                return (true)
            }
        })
        this.memberLimits = []
        for (let i = 0; i < this.teamLimit; i++) {
            this.memberLimits[i] = i + 1
        }
    }
    onMemberSelected(deviceValue) {
        console.log(deviceValue)
    }
}
