import { NO_ERRORS_SCHEMA } from "@angular/core";
import { PaymentComponent } from "./payment.component";
import { ComponentFixture, TestBed } from "@angular/core/testing";

describe("PaymentComponent", () => {

  let fixture: ComponentFixture<PaymentComponent>;
  let component: PaymentComponent;
  beforeEach(() => {
    TestBed.configureTestingModule({
      schemas: [NO_ERRORS_SCHEMA],
      providers: [
      ],
      declarations: [PaymentComponent]
    });

    fixture = TestBed.createComponent(PaymentComponent);
    component = fixture.componentInstance;

  });

  it("should be able to create component instance", () => {
    expect(component).toBeDefined();
  });
  
});
