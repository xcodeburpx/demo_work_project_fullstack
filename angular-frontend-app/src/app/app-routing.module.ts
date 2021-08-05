import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { TruckMapComponent } from './components/truck-map/truck-map.component';

const routes: Routes = [
  {
    path:"login", component:LoginComponent
  },
  {
    path:"gps/truck_location", component: TruckMapComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
