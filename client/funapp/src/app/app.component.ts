import { Component } from '@angular/core';
import { RestService } from './rest.service';
import {map} from "rxjs/operators";

export interface StudentAnswer {
  groupId: number;
  receivedTime: string;
  questionNum: number;
  result: number
}


const ELEMENT_DATA: StudentAnswer[] = [
];

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Youth Code';
  answerList: any = [];
  displayedColumns: string[] = ['groupId', 'receivedTime', 'questionNum', 'result'];

  constructor(public rest:RestService) { }

  ngOnInit() {
        this.answerList = [];
        this.getResultList();
  }

  getResultList() {
    this.rest.getAnswers().subscribe(data => {
      console.log(data);
      this.answerList = data;
    });
  }
}
