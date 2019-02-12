import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import {interval, Observable, of, timer} from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';



const endpoint = 'http://192.168.163.129:5000/api/';
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

@Injectable({
    providedIn: 'root'  // <- ADD THIS
})
export class RestService {

  constructor(private http: HttpClient) { }

  private extractData(res: Response) {
    let body = res;
    return body || { };
  }

  getAnswers(): Observable<any> {
    return timer(0,5000).pipe(_ =>this.http.get(endpoint + 'answer')).pipe(
      map(this.extractData));
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      console.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
