import { NO_ERRORS_SCHEMA } from "@angular/core";
import { CoreComponent } from "./core.component";
import { ComponentFixture, TestBed } from "@angular/core/testing";

describe("CoreComponent", () => {

  let fixture: ComponentFixture<CoreComponent>;
  let component: CoreComponent;
  beforeEach(() => {
    TestBed.configureTestingModule({
      schemas: [NO_ERRORS_SCHEMA],
      providers: [
      ],
      declarations: [CoreComponent]
    });

    fixture = TestBed.createComponent(CoreComponent);
    component = fixture.componentInstance;

  });

  it("should be able to create component instance", () => {
    expect(component).toBeDefined();
  });
  
});
