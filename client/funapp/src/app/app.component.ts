import { Component } from '@angular/core';

export interface PeriodicElement {
  groupNo: number;
  receivedTime: string;
  question1: boolean;
  question2: boolean;
  question3: boolean;
  result: number
}


const ELEMENT_DATA: PeriodicElement[] = [
  {groupNo: 1, receivedTime: new Date().toLocaleString(), question1: false, question2: false, question3: false, result: 0},
  {groupNo: 2, receivedTime: new Date().toLocaleString(), question1: false, question2: false, question3: false, result: 0},
  {groupNo: 3, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false,result: 0},
  {groupNo: 4, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 5, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 6, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 7, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 8, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 9, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 10, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 11, receivedTime: new Date().toLocaleString(), question1: false, question2: false,   question3: false,result: 0},
  {groupNo: 12, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 13, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 14, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 15, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 16, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 17, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 18, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 19, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},
  {groupNo: 20, receivedTime: new Date().toLocaleString(), question1: false, question2: false,  question3: false, result: 0},

];

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Youth Code';
  displayedColumns: string[] = ['groupNo', 'receivedTime', 'question1', 'question2', 'question3', 'result'];
  dataSource = ELEMENT_DATA;
}
