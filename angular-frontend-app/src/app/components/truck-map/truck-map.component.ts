import { Component, OnInit } from '@angular/core';
import { BackendConnectService } from 'src/app/services/backend-connect.service';

@Component({
  selector: 'app-truck-map',
  templateUrl: './truck-map.component.html',
  styleUrls: ['./truck-map.component.css']
})
export class TruckMapComponent implements OnInit {



  // Initial Google map values
  center = {
    lat: 49.641733,
    lng: 20.147554,
  }
  height = "500px";
  width = "100%"

  // Initial truck_data and truck_list objects
  private truck_data: any = null
  public truck_list: any = null;

  // Initial private variable truck_name
  // Placeholder for truck name from forms
  private truck_name: string;

  constructor(public _bknConnService: BackendConnectService) { 
    this.truck_name = '';
  }
  
  async ngOnInit(){
    const data = await this._bknConnService.getTruckList();
    if (data['status'] == 'OK')
    {
      this.truck_list = data['data'];
    }
    else
    {
      throw new Error("Truck list was not extracted from server!");
    }
  }

  async getTruckGpsData()
  {
    const data = await this._bknConnService.getTruckGpsData(this.truck_name);
    if (data['status'] == 'OK')
    {
      console.log("Setting user data: ");
      console.log(data);
      this.truck_data = data['data'];
    }
    else
    {
      console.log("Data: ");
      console.log(data);
      throw new Error("Truck list was not extracted from server!");
    }

    this.center = {
      lat: parseFloat(this.truck_data['longitude']),
      lng: parseFloat(this.truck_data['latitude']),
    }
  }

  public ifTruckDataExist(): boolean{
    return this.truck_data !== null;
  }

  public ifTruckListExist(): boolean {
    return this.truck_list !== null;
  }

}
