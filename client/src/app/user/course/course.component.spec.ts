import { NO_ERRORS_SCHEMA } from "@angular/core";
import { CourseComponent } from "./course.component";
import { ComponentFixture, TestBed } from "@angular/core/testing";

describe("CourseComponent", () => {

  let fixture: ComponentFixture<CourseComponent>;
  let component: CourseComponent;
  beforeEach(() => {
    TestBed.configureTestingModule({
      schemas: [NO_ERRORS_SCHEMA],
      providers: [
      ],
      declarations: [CourseComponent]
    });

    fixture = TestBed.createComponent(CourseComponent);
    component = fixture.componentInstance;

  });

  it("should be able to create component instance", () => {
    expect(component).toBeDefined();
  });
  
});
