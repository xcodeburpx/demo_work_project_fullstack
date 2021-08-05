import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TruckMapComponent } from './truck-map.component';

describe('TruckMapComponent', () => {
  let component: TruckMapComponent;
  let fixture: ComponentFixture<TruckMapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TruckMapComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TruckMapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
