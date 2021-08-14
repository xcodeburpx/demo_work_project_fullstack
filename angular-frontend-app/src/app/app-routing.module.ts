import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { TruckMapComponent } from './components/truck-map/truck-map.component';
import { TruckTableComponent } from './components/truck-table/truck-table.component';

const routes: Routes = [
  {
    path:"login", 
    component: LoginComponent,
    data: {title: 'Login'}
  },
  {
    path:"gps/truck_location", 
    component: TruckMapComponent,
    data: {title: 'Truck Map'}
  },
  {
    path:"gps/truck_table", 
    component: TruckTableComponent,
    data: {title: 'Truck Table'}
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
