import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-truck-map',
  templateUrl: './truck-map.component.html',
  styleUrls: ['./truck-map.component.css']
})
export class TruckMapComponent implements OnInit {

  constructor() { }

  center = {
    lat: 49.641733,
    lng: 20.147554,
  }

  marker = {
      position: {
        lat: 49.641733,
        lng: 20.147554,
      },
      label: {
        color: 'red',
        text: 'Marker label Home' ,
      },
      title: 'My Home',
      options: { animation: google.maps.Animation.BOUNCE },
    }

  ngOnInit(): void {
  }

}
