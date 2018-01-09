import { NO_ERRORS_SCHEMA } from "@angular/core";
import { ClassroomComponent } from "./classroom.component";
import { ComponentFixture, TestBed } from "@angular/core/testing";

describe("ClassroomComponent", () => {

  let fixture: ComponentFixture<ClassroomComponent>;
  let component: ClassroomComponent;
  beforeEach(() => {
    TestBed.configureTestingModule({
      schemas: [NO_ERRORS_SCHEMA],
      providers: [
      ],
      declarations: [ClassroomComponent]
    });

    fixture = TestBed.createComponent(ClassroomComponent);
    component = fixture.componentInstance;

  });

  it("should be able to create component instance", () => {
    expect(component).toBeDefined();
  });
  
});
