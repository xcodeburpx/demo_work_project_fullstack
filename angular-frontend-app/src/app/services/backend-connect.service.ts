import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class BackendConnectService {

  private api_url: string = "http://localhost:8000/";
  
  // http options used for making API calls
  private httpOptions: any;
 
  // error messages received from the login attempt
  public errors: any = [];
  
  constructor(private http: HttpClient) {
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'}),
      withCredentials: true
    };
  }

  public login(user) {
    this.http.post(this.api_url + 'api/login/', JSON.stringify(user), this.httpOptions).subscribe(
      data => {
        console.log("User logged in successfully");
        console.log(data);
        this.setUserData(data['data']);
      },
      err => {
        console.log("User could not log in");
        this.errors = err['error'];
      }
    );
  }

  public logout() {
    this.http.get(this.api_url + 'api/logout/', this.httpOptions).subscribe(
      data => {
        if(data['status'] == "OK")
        {
          console.log("User logged out successfully");
          console.log(data);
          this.removeUserData();
        }
        else
        {
          console.log("User could not log out");
          console.log(data);
        }
      },
      err => {
        console.log("User could not authenticate");
        this.errors = err['error'];
      }
    );
  }

  async getTruckList() {
    return await this.http.get(this.api_url + 'api/gps/truck_list/', this.httpOptions).toPromise();

  }

  async getTruckGpsData(truck_name) {
    return await this.http.get(this.api_url + 'api/gps/newest/' + truck_name + '/', this.httpOptions).toPromise();
  }

  public getUserData(): string{
    return localStorage.getItem('userName');
  }

  public ifUserLoggedIn(): boolean {
    if(localStorage.getItem('userName') === null)
    {
      return false;
    }
    return true;
  }

  private setUserData(data): void {
    const userName = data['username'];
    const firstName = data['first_name'];
    const lastName = data['last_name'];

    localStorage.setItem('userName',userName);
    localStorage.setItem('firstName',firstName);
    localStorage.setItem('lastName',lastName);
  }

  private removeUserData(): void{
    localStorage.clear();
  }
}
