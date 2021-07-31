import { Component } from '@angular/core';
import { BackendConnectService } from './services/backend-connect.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular-frontend-app';
  msg: any;
  constructor(private bckConnService: BackendConnectService) {

  }

  ngOnInit(): void {
    this.showMessage();
  }

  showMessage(){
    this.bckConnService.getMessage().subscribe(data => {
      this.msg = data,
      console.log(this.msg);
    })
  }
}
